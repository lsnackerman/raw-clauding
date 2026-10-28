#!/bin/bash
#
# sync-session.sh — refresh the LOG in the current session's file.
#
# Auto-detects target in two stages — SOURCE pick, then DESTINATION match:
#   1. SOURCE: which session am I? — `$CLAUDE_CODE_SESSION_ID` when the harness
#      provides it (deterministic, concurrency-safe); else the most-recently-modified
#      JSONL in this project's dir (recency — correct only when running solo).
#   2. JSONL filename IS the session_id (by Claude Code convention)
#   3. DESTINATION: find the session file in Core/sessions/ whose YAML session_id matches.
#
# Both stages matter and they fail differently. A wrong DESTINATION match would
# cross-contaminate (splice session A's log into session B's file) — stage 3 prevents
# that. A wrong SOURCE pick is benign but SILENT: it syncs the *other* session
# correctly into its own file and reports success, while yours stays stale. Stage 1's
# env-var preference is what closes that. When in doubt under concurrency, pass the
# path explicitly.
#
# Falls back to "TODAY's most-recent dated session file" if no session_id match (e.g.,
# a session file created before this script was hardened, or an environment where the
# Claude Code JSONLs aren't reachable). The fallback is scoped to today's date so a
# failed match can never silently splice this session into an OLD file — with no
# today-dated file it fails loud rather than guessing. Pass an explicit path to be sure.
#
# Usage:
#   bash Core/skills/sync/sync-session.sh                   # auto-detect via session_id match
#   bash Core/skills/sync/sync-session.sh path/to/x.md      # specific session file
#
# Colocated with /sync skill — script lives in the skill folder that owns it.
# Supporting doctrine in sync/SKILL.md (philosophy + architecture) and sync/edge-cases.md.
#
# Hardened: auto-detect by session_id match, not recency. The earlier "ls -t" version
# could silently extract the wrong JSONL when yesterday's session file was the most
# recent on disk — its cached YAML session_id became the source of truth, and the
# Python script faithfully extracted yesterday's transcript. The fix flips the direction:
# start from the live JSONL (which IS the current session by Claude Code convention),
# find the session file that matches it. Primary-key over heuristic.

set -euo pipefail

# Navigate to system root (three levels up from Core/skills/sync/)
cd "$(dirname "$(readlink -f "$0" 2>/dev/null || greadlink -f "$0" 2>/dev/null || echo "$0")")/../../.." || exit 1

EXTRACT="Core/skills/sync/extract-session.py"
SESSIONS_DIR="Core/sessions"

if [ $# -gt 0 ]; then
  TARGET="$1"
else
  if [ ! -d "$SESSIONS_DIR" ]; then
    echo "No sessions folder: $SESSIONS_DIR"
    exit 1
  fi

  # Architecturally-correct auto-detect: find current session's JSONL, match by session_id.
  # Project slug = pwd with EVERY non-alphanumeric character → -
  # Converting only "/" (the obvious guess) is wrong for any folder with a space,
  # underscore, dot, or plus — and that failure is silent: the computed slug simply
  # doesn't exist, so capture finds nothing and the session log comes out empty.
  # Same rule as Core/scripts/ensure-symlinks.sh.
  PROJECT_SLUG=$(pwd | sed 's|[^a-zA-Z0-9]|-|g')
  PROJECTS_DIR="$HOME/.claude/projects/$PROJECT_SLUG"
  TARGET=""

  if [ -d "$PROJECTS_DIR" ]; then
    SESSION_ID=""

    # SOURCE PICK — prefer the session id the harness hands us. This is the only
    # deterministic option when more than one session is open: recency picks whichever
    # session wrote LAST, which under concurrency is routinely not yours. That failure
    # is benign but SILENT — the destination match below then pairs the other session's
    # JSONL with its own .md and syncs it correctly, so you get a success message while
    # YOUR log stays stale.
    if [ -n "${CLAUDE_CODE_SESSION_ID:-}" ] && [ -f "$PROJECTS_DIR/$CLAUDE_CODE_SESSION_ID.jsonl" ]; then
      SESSION_ID="$CLAUDE_CODE_SESSION_ID"
    else
      # Fallback source pick: most-recent JSONL. Still correct for single-session runs
      # and for environments that don't set the variable (e.g. Cursor).
      #
      # NOTE: the trailing `|| true` on these substitutions is load-bearing under
      # `set -euo pipefail`: a `grep|head` (or `ls|head`) that finds no match exits
      # non-zero, and WITHOUT `|| true` the failing command-substitution kills the
      # whole script at the assignment — BEFORE the fallback + fail-loud message below
      # can run. Symptom: sync exits silently (exit 1, empty output) when no session
      # file exists yet (e.g. a session that never ran /pickup, so no shell was stubbed).
      LATEST_JSONL=$(ls -t "$PROJECTS_DIR"/*.jsonl 2>/dev/null | head -1 || true)
      if [ -n "$LATEST_JSONL" ]; then
        SESSION_ID=$(basename "$LATEST_JSONL" .jsonl)
      fi
    fi

    if [ -n "$SESSION_ID" ]; then
      # Match session file by YAML session_id (handles concurrent sessions correctly)
      TARGET=$(grep -l "session_id: $SESSION_ID" "$SESSIONS_DIR"/20*.md 2>/dev/null | head -1 || true)
    fi
  fi

  # Fallback: TODAY's most-recent session file. Scoped to today so a failed session_id
  # match can never silently splice this session into an OLD file.
  if [ -z "$TARGET" ]; then
    TODAY=$(date +%Y-%m-%d)
    TARGET=$(ls -t "$SESSIONS_DIR/$TODAY"-*.md 2>/dev/null | grep -Ev 'README|INDEX|THREADS' | head -1 || true)
    if [ -n "$TARGET" ]; then
      echo "⚠ Auto-detect: no session_id match — fell back to today's most-recent .md ($TARGET). Pass an explicit path if this is wrong."
    fi
  fi

  # No today-file (e.g. a spanning/multi-day session dated an earlier day): don't silently
  # grab an old file — fail loud, but NAME the most-recent candidate so it's a one-copy fix.
  if [ -z "$TARGET" ]; then
    SUGGEST=$(ls -t "$SESSIONS_DIR"/20*.md 2>/dev/null | grep -Ev 'README|INDEX|THREADS' | head -1 || true)
    echo "✗ No session file to sync. sync-session.sh only *refreshes* an existing session file — it never creates one, and no today-dated file exists in $SESSIONS_DIR."
    [ -n "$SUGGEST" ] && echo "  Most-recent candidate (a spanning session likely lives here): $SUGGEST"
    echo "  Fix: create the session shell first (/wrap creates one — /pickup does NOT), or pass the path explicitly →  $0 Core/sessions/{date}-{hash}.md"
    exit 1
  fi
fi

echo "Target: $TARGET"
python3 "$EXTRACT" "$TARGET"
