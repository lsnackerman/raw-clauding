#!/bin/bash
# ensure-symlinks.sh — keep .claude/ symlinks in sync with Core/
#
# Designed to run as a Claude Code hook (SessionStart + PostToolUse).
# Idempotent: safe to run repeatedly, only acts on missing links.
#
# When called from PostToolUse, reads JSON from stdin to check if
# the edited file is in Core/skills/ or Core/rules/. Exits silently
# if not relevant (zero token cost).

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
if ! cd "$REPO_ROOT"; then
  echo "ensure-symlinks: could not enter the system root ($REPO_ROOT)." >&2
  echo "  This is a FAILURE to run, not a clean result — nothing was linked." >&2
  echo "  Run it from inside your system folder: bash Core/scripts/ensure-symlinks.sh" >&2
  exit 2
fi

# Sanity: are we actually in a raw-clauding system? A wrong root would otherwise
# link zero skills and report success — a clean-looking result from doing nothing.
if [ ! -f "AGENTS.md" ] || [ ! -d "Core" ]; then
  echo "ensure-symlinks: $REPO_ROOT doesn't look like a raw-clauding system" >&2
  echo "  (expected AGENTS.md and Core/ here). Nothing was linked." >&2
  exit 2
fi

# --- Mode detection ---
# Terminal stdin (manual run), empty stdin, or a SessionStart payload → full scan
# PostToolUse payload → check the single edited file

MANUAL=0

# `--check` = "set me up and tell me if it worked." Always a full scan, always
# prints the summary. Use it when something other than a human terminal runs this
# (an AI running it for you, a script) — auto-detection can't see a terminal there,
# so without this flag the confirmation would be silently skipped.
if [ "$1" = "--check" ]; then
  MODE="full"
  MANUAL=1
elif [ -t 0 ]; then
  # Terminal — manual run, full scan
  MODE="full"
  MANUAL=1
else
  INPUT=$(cat)

  if [ -z "$INPUT" ]; then
    # No data on stdin — full scan
    MODE="full"
  elif [ "$(echo "$INPUT" | jq -r '.hook_event_name // empty' 2>/dev/null)" = "SessionStart" ]; then
    # The session-start hook sends JSON with no file path in it. Without this
    # branch it fell through to "nothing to act on" below and the start-of-session
    # scan silently never ran. Full scan, quietly.
    MODE="full"
  elif ! command -v jq >/dev/null 2>&1; then
    # `jq` reads the hook's JSON payload. Recent macOS ships it (/usr/bin/jq) and
    # most Linux setups have it, but don't count on it — if it's missing, fall back
    # to a full scan rather than exiting quietly. Doing nothing silently is the
    # dangerous case: a new skill would never get its symlink and would simply never
    # appear as a slash command, with no error to explain why.
    MODE="full"
  else
    FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty' 2>/dev/null)

    # No file path in the JSON — nothing to act on for this edit.
    [ -z "$FILE_PATH" ] && exit 0

    # Normalize to a relative path
    FILE_PATH="${FILE_PATH#$REPO_ROOT/}"

    case "$FILE_PATH" in
      Core/skills/*|Core/rules/*) MODE="single" ;;
      *) exit 0 ;;
    esac
  fi
fi

# --- Symlink functions ---

LINKED=0
FAILED=0
WARNED=0

# Report the real result of `ln -s`, never assume it worked. A filesystem that
# can't make symlinks (some Windows/exFAT/network drives) fails here — and
# announcing "Symlinked:" anyway would tell you the system is wired up when it
# isn't, which is the hardest kind of broken to diagnose later.
make_link() {
  local target="$1" link_path="$2"
  if ln -s "$target" "$link_path" 2>/dev/null; then
    echo "Symlinked: $link_path -> $target"
    LINKED=$((LINKED + 1))
  else
    FAILED=$((FAILED + 1))
    echo "COULD NOT create symlink: $link_path" >&2
    # Explain once — the cause is the same for every link in a failing run, and
    # repeating it per-file buries the message it's trying to deliver.
    if [ "$FAILED" = "1" ]; then
      echo "  The AI won't see these until the links exist." >&2
      echo "  Most common cause: the system folder sits on a drive that doesn't support" >&2
      echo "  symlinks (a Windows drive, an exFAT or network volume). Move the folder to" >&2
      echo "  your home directory and run this again." >&2
      echo "  Other possibility: .claude/ isn't writable — check its permissions." >&2
    fi
  fi
}

# A real file or folder sitting where a pointer belongs. Usually this means an AI
# "fixed" a broken symlink by copying the files instead of re-pointing the link —
# which leaves you with two copies that drift apart in silence.
#
# Say so. The old version just skipped it: no heal, no message, every session,
# forever. The person then sees duplicate files with no way to know why, and no
# reason to suspect the script that runs on their behalf. A guard that finds the
# fault and stays quiet is worse than no guard, because it reports success.
warn_not_a_link() {
  local link_path="$1" real_source="$2"
  WARNED=$((WARNED + 1))
  echo "NOT A LINK: $link_path is a real file/folder, not a pointer." >&2
  if [ "$WARNED" = "1" ]; then
    echo "  It should point at $real_source. Because it doesn't, you now have two" >&2
    echo "  copies, and edits to one will not show up in the other." >&2
    echo "  To fix: compare them (\`diff -r $link_path $real_source\`)." >&2
    echo "    Identical → delete the copy: \`rm -rf $link_path\`, then run this again." >&2
    echo "    Different → keep the version you want in $real_source first, then delete." >&2
    echo "  Nothing was changed for you — deleting your files isn't this script's call." >&2
  fi
}

link_skill() {
  local skill_dir="$1"
  local skill_name
  skill_name=$(basename "$skill_dir")
  local link_path=".claude/skills/$skill_name"

  if [ -e "$link_path" ] && [ ! -L "$link_path" ]; then
    warn_not_a_link "$link_path" "Core/skills/$skill_name"
    return 1
  fi

  if [ ! -L "$link_path" ] && [ ! -e "$link_path" ]; then
    make_link "../../Core/skills/$skill_name" "$link_path"
  fi
}

link_rule() {
  local rule_file="$1"
  local filename
  filename=$(basename "$rule_file")

  # CLAUDE.md is the folder's compass, not a rule. It already fires the right way
  # — by being read when the AI opens Core/rules/. Symlinking it here would
  # auto-load it into every single session on top of the rules it describes.
  [ "$filename" = "CLAUDE.md" ] && return

  local link_path=".claude/rules/$filename"

  if [ -e "$link_path" ] && [ ! -L "$link_path" ]; then
    warn_not_a_link "$link_path" "Core/rules/$filename"
    return 1
  fi

  if [ ! -L "$link_path" ] && [ ! -e "$link_path" ]; then
    make_link "../../Core/rules/$filename" "$link_path"
  fi
}

clean_orphans() {
  # Remove symlinks that point to nothing (source renamed/moved/deleted).
  # Without this, renaming Core/rules/X.md → Y.md and editing creates the
  # new Y.md symlink but leaves orphan X.md symlink behind.
  local dir="$1"
  [ -d "$dir" ] || return
  for link in "$dir"/*; do
    if [ -L "$link" ] && [ ! -e "$link" ]; then
      rm "$link"
      echo "Removed orphan symlink: $link"
    fi
  done
}

# --- Execute ---

if [ "$MODE" = "full" ]; then
  # Full scan: check all skills, rules, and CLAUDE.md
  mkdir -p .claude/skills .claude/rules

  # Clean orphan symlinks (renames/moves leave dangling links otherwise)
  clean_orphans .claude/skills
  clean_orphans .claude/rules

  # Hooks config — the automation (symlink sync, task archive) is wired
  # here. If this file already exists we must not clobber it (it may hold permissions
  # you've approved), but we also can't just skip silently: a settings file with no
  # hooks means none of the automation ever runs, with nothing to indicate why.
  HOOKS_OK=1
  if [ -f "Core/scripts/settings.local.json" ]; then
    if [ ! -f ".claude/settings.local.json" ]; then
      if cp "Core/scripts/settings.local.json" ".claude/settings.local.json"; then
        echo "Copied: .claude/settings.local.json from Core/scripts/"
      else
        HOOKS_OK=0
        echo "FAILED to install .claude/settings.local.json — no automation will run." >&2
      fi
    elif ! grep -q "ensure-symlinks.sh" ".claude/settings.local.json" 2>/dev/null; then
      HOOKS_OK=0
      echo "NOTE: .claude/settings.local.json already exists and has no hooks in it." >&2
      echo "  Your skills and rules are wired, but the background automation is NOT." >&2
      echo "  That file wasn't overwritten because it may hold permissions you approved." >&2
      echo "  To wire the hooks, merge the \"hooks\" block from Core/scripts/settings.local.json" >&2
      echo "  into it — or ask the AI to do it for you." >&2
    fi
  fi

  # CLAUDE.md → AGENTS.md (the compass)
  if [ ! -L ".claude/CLAUDE.md" ] && [ ! -e ".claude/CLAUDE.md" ]; then
    make_link "../AGENTS.md" ".claude/CLAUDE.md"
  fi

  # MEMORY.md — lives in Claude Code's own storage for this folder, symlinked in here.
  #
  # Finding that storage location is the delicate part. Claude Code turns your
  # folder's path into a directory name under ~/.claude/projects/ using a rule that
  # is THEIRS, not ours — and any guess we make about that rule is wrong the moment
  # your folder name has a space, a dot, a capital, or anything else we didn't
  # anticipate. A wrong guess is silent and nasty: we'd create a MEMORY.md that
  # looks perfectly correct and that the AI never reads, because it's reading a
  # different directory.
  #
  # So don't guess. Every session transcript records the folder it ran in, as a
  # plain `cwd` field. That's a fact rather than an inference, so we search for the
  # directory whose transcripts say they came from HERE.
  ABS_REPO_ROOT="$(cd "$REPO_ROOT" && pwd)"

  find_project_dir() {
    local d f cwd
    for d in "$HOME/.claude/projects"/*/; do
      [ -d "$d" ] || continue
      for f in "$d"*.jsonl; do
        [ -f "$f" ] || continue
        cwd=$(grep -m1 -o '"cwd":"[^"]*"' "$f" 2>/dev/null | sed 's/^"cwd":"//; s/"$//')
        if [ "$cwd" = "$ABS_REPO_ROOT" ]; then printf '%s' "${d%/}"; return 0; fi
        break   # one transcript per directory is enough to identify it
      done
    done
    return 1
  }

  PROJECT_DIR="$(find_project_dir)"

  if [ -z "$PROJECT_DIR" ]; then
    # No transcript claims this folder yet — normal before your first session, which
    # is exactly when setup runs. So this branch is what EVERY fresh install takes,
    # and the guess had better be right.
    #
    # Claude Code's rule, determined by running it and reading what appeared:
    # every non-alphanumeric character becomes "-", and case is preserved.
    #   /Users/x/My OS_test.v2  ->  -Users-x-My-OS-test-v2
    #   /Users/x/Kit+OS (v2)    ->  -Users-x-Kit-OS--v2-
    # Converting only "/" (the obvious guess) is wrong for any folder with a space,
    # underscore, dot, or plus — and that failure is silent: MEMORY.md gets created
    # somewhere real that the AI never reads. (Claude Code's own docs describe the
    # rule as replacing path separators only; the lines above are what the tool
    # actually produced when run. If a future version changes it, the transcript
    # search above finds the real folder on the next SessionStart and self-heals.)
    PROJECT_DIR="$HOME/.claude/projects/$(printf '%s' "$ABS_REPO_ROOT" | sed 's/[^a-zA-Z0-9]/-/g')"
    RESOLVED_BY_GUESS=1
  fi

  MEMORY_DIR="$PROJECT_DIR/memory"
  MEMORY_FILE="$MEMORY_DIR/MEMORY.md"

  # Self-heal: if Core/auto-memory already points somewhere else, this folder moved
  # or was renamed since setup. Left alone, your accumulated memory stays visible in
  # your system and invisible to the AI, while a blank one loads in its place — and
  # nothing errors. Carry the old file forward and re-point.
  if [ -L "Core/auto-memory" ]; then
    OLD_MEM_DIR="$(readlink "Core/auto-memory")"
    if [ "$OLD_MEM_DIR" != "$MEMORY_DIR" ]; then
      echo "Your auto-memory was pointing at the wrong place (folder renamed or moved,"
      echo "or set up before your first session, when the location wasn't knowable yet)."
      # Carry the old file forward BEFORE touching the symlink — and only drop the
      # symlink if that succeeded. The symlink is the one visible pointer to your
      # accumulated memory; removing it after a failed copy would strand the file
      # somewhere you can no longer see, while this script cheerfully reported
      # having moved it. Fail here and we change nothing.
      MIGRATED=1
      # If BOTH locations have a MEMORY.md, don't silently pick one. Re-pointing
      # without a word would drop the old one out of view — it stays on disk, but
      # nothing in your system points at it any more, and you'd have no reason to
      # go looking. Say where it is and let the human decide.
      if [ -f "$OLD_MEM_DIR/MEMORY.md" ] && [ -f "$MEMORY_FILE" ]; then
        echo "  NOTE: there's a MEMORY.md in both the old and new location." >&2
        echo "    keeping: $MEMORY_FILE" >&2
        echo "    also at: $OLD_MEM_DIR/MEMORY.md" >&2
        echo "    Nothing was deleted. Merge anything you want from the old one." >&2
      fi
      if [ -f "$OLD_MEM_DIR/MEMORY.md" ] && [ ! -f "$MEMORY_FILE" ]; then
        if mkdir -p "$MEMORY_DIR" && cp "$OLD_MEM_DIR/MEMORY.md" "$MEMORY_FILE"; then
          echo "  Carried your MEMORY.md forward — it would otherwise have gone unread."
        else
          MIGRATED=0
          echo "  COULD NOT copy your MEMORY.md to the new location." >&2
          echo "  Leaving everything as-is so nothing is lost. Your memory is at:" >&2
          echo "    $OLD_MEM_DIR/MEMORY.md" >&2
          echo "  Copy it to $MEMORY_DIR/ by hand, then run this again." >&2
        fi
      fi

      if [ "$MIGRATED" = "1" ]; then
        rm "Core/auto-memory"
        echo "  Re-pointed Core/auto-memory at the location the AI actually reads."
      fi
    fi
  fi

  if [ ! -f "$MEMORY_FILE" ]; then
    mkdir -p "$MEMORY_DIR"
    cat > "$MEMORY_FILE" << 'MEMEOF'
# MEMORY

Operational shortcuts. AGENTS.md has the compass — this file has what would clutter it.

## Orientation
- ALIVE.md is the handoff: `## FOLLOW-UPS` then `## NEXT - {AREA}` sections, read top-down, on-deck at the top of each
- PULLING.md holds threads that won't let go between sessions
- THREADS.md is the per-session bulleted record of what got done

## Key Files
- (add paths as you discover them)

## Patterns
- (add patterns as you earn them)
MEMEOF
    echo "Created: $MEMORY_FILE"
  fi

  if [ ! -L "Core/auto-memory" ] && [ ! -e "Core/auto-memory" ]; then
    make_link "$MEMORY_DIR" "Core/auto-memory"
    [ -n "$RESOLVED_BY_GUESS" ] && echo "  (best guess for now — it self-corrects after your first session.)"
  fi

  for skill_dir in Core/skills/*/; do
    [ -d "$skill_dir" ] || continue
    link_skill "$skill_dir"
  done

  for rule_file in Core/rules/*.md; do
    [ -f "$rule_file" ] || continue
    link_rule "$rule_file"
  done

elif [ "$MODE" = "single" ]; then
  # Clean orphan symlinks first — catches renames/moves done mid-session.
  # Cost: walks the few symlinks in .claude/, microseconds.
  clean_orphans .claude/skills
  clean_orphans .claude/rules

  # Single file: just handle the one that was written
  if [[ "$FILE_PATH" =~ ^Core/skills/([^/]+) ]]; then
    skill_name="${BASH_REMATCH[1]}"
    mkdir -p .claude/skills
    link_skill "Core/skills/$skill_name"
  elif [[ "$FILE_PATH" =~ ^Core/rules/([^/]+)$ ]]; then
    mkdir -p .claude/rules
    link_rule "$FILE_PATH"
  fi
fi

# --- Report ---
# On a manual run, always say what happened. "It printed nothing" is ambiguous —
# it could mean "already set up, nothing to do" or "silently did nothing at all,"
# and those need very different reactions from you.
if [ "$MANUAL" = "1" ]; then
  # Count what we linked AND what should have been linked. An absolute count can't
  # tell "12 of 12" from "11 of 12" — and a single skipped skill reads exactly like
  # success. Compare against the source of truth, or this isn't a check at all.
  skills_linked=$(find .claude/skills -maxdepth 1 -type l 2>/dev/null | wc -l | tr -d ' ')
  rules_linked=$(find .claude/rules -maxdepth 1 -type l 2>/dev/null | wc -l | tr -d ' ')
  skills_expected=$(find Core/skills -maxdepth 1 -mindepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
  rules_expected=$(find Core/rules -maxdepth 1 -name '*.md' ! -name 'CLAUDE.md' 2>/dev/null | wc -l | tr -d ' ')

  echo ""
  echo "Setup check: $skills_linked/$skills_expected skills and $rules_linked/$rules_expected rules wired."

  problems=0

  # Python is what /sync and /wrap run to save your session. Without it, everything looks
  # fine all session and capture breaks at the end — on the step you can't afford to lose.
  # The setup guide's Python step checks this; this is the backstop for anyone who skipped it.
  # (Name the step, never number it: the Mac and Windows guides number it differently.)
  if ! command -v python3 >/dev/null 2>&1; then
    echo "⚠️  python3: MISSING — /wrap and /sync cannot save your sessions." >&2
    echo "   Fix: your setup guide's Python step (Core/mechanics/setup-mac.md or setup-windows.md)." >&2
    problems=1
  fi

  if [ "$FAILED" -gt 0 ]; then
    echo "⚠️  $FAILED link(s) FAILED — see the errors above." >&2
    problems=1
  fi

  if [ "$WARNED" -gt 0 ]; then
    echo "⚠️  $WARNED slot(s) hold a real file/folder instead of a pointer — see NOT A LINK above." >&2
    echo "   This is the one that hides: you have two copies of something, and edits" >&2
    echo "   to one won't reach the other. Nothing was deleted for you." >&2
    problems=1
  fi

  # Under-count and over-count are different problems with different fixes — saying
  # "did NOT get wired" when there are MORE links than sources sends you hunting for
  # the wrong thing entirely.
  if [ "$skills_linked" -lt "$skills_expected" ] || [ "$rules_linked" -lt "$rules_expected" ]; then
    echo "⚠️  Some skills or rules did NOT get wired (see the counts above)." >&2
    echo "   Usually something already occupies its slot in .claude/. Look for a real" >&2
    echo "   file or folder where a symlink should be, remove it, and run this again." >&2
    problems=1
  elif [ "$skills_linked" -gt "$skills_expected" ] || [ "$rules_linked" -gt "$rules_expected" ]; then
    echo "Note: .claude/ has more links than Core/ has skills or rules." >&2
    echo "   Left-overs from something you renamed or removed. Harmless, but they'll" >&2
    echo "   load every session — delete the extras from .claude/skills or .claude/rules." >&2
  fi

  if [ "$skills_expected" = "0" ] || [ "$rules_expected" = "0" ]; then
    echo "⚠️  Found no skills or no rules to wire — is this the right folder?" >&2
    problems=1
  fi

  if [ "$HOOKS_OK" != "1" ]; then
    echo "⚠️  Background automation is not wired (see the note above)." >&2
    problems=1
  fi

  if [ "$problems" = "1" ]; then
    echo "" >&2
    echo "The system is NOT fully set up. Fix the above and re-run." >&2
    exit 1
  fi

  if [ "$LINKED" = "0" ]; then
    echo "Nothing new to link — you were already set up. You're good to go."
  else
    echo "You're set up. Start a new session so the AI picks everything up."
  fi
fi
