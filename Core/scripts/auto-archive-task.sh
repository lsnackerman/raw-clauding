#!/bin/bash
# auto-archive-task.sh — move tasks to Tasks/_done/ when status changes to done
#
# TWO ENTRY POINTS, and the second one exists because the first has a blind spot:
#
#   1. PostToolUse (Edit|Write)  — reads hook JSON from stdin, acts on that one file.
#      Immediate, but sees ONLY status changes made through the Edit/Write tools.
#   2. --scan / Stop hook        — sweeps all of Tasks/ regardless of HOW a status
#      changed. This is the backstop.
#
#   Why (2) is needed: a `status: done` written by any other path — a shell one-liner,
#   a script, a text editor, an app syncing the folder — is INVISIBLE to (1), so the
#   task silently stays in Tasks/ looking active. The structure only tells the truth
#   if every write path is covered, and a tool-matcher covers exactly one. Widening the
#   matcher to Bash isn't the fix (it would fire on every shell command); a once-per-turn
#   sweep is.

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT" || exit 0

# Archive one task file if it is a done task sitting directly in Tasks/.
# Arg: path relative to REPO_ROOT. Silent unless it acts.
archive_if_done() {
  local FILE_PATH="$1"

  # Only files directly in Tasks/ (not already in _done/, _dropped/, etc.)
  [[ "$FILE_PATH" =~ ^Tasks/[^_/][^/]*\.md$ ]] || return 0

  local FULL_PATH="$REPO_ROOT/$FILE_PATH"
  [ -f "$FULL_PATH" ] || return 0

  # status from YAML frontmatter (between --- markers)
  local STATUS
  STATUS=$(awk '/^---$/{n++; next} n==1 && /^status:/{print $2; exit}' "$FULL_PATH")
  [ "$STATUS" = "done" ] || return 0

  local FILENAME DEST
  FILENAME=$(basename "$FILE_PATH")
  mkdir -p "$REPO_ROOT/Tasks/_done"
  DEST="$REPO_ROOT/Tasks/_done/$FILENAME"

  if [ -e "$DEST" ]; then
    echo "Warning: Tasks/_done/$FILENAME already exists, skipping auto-archive"
    return 0
  fi

  # Report what the move actually did. Announcing success on a failed mv would
  # tell you the task was filed when it's still sitting in Tasks/ — and you'd
  # only find out by noticing a "done" task that never left.
  if mv "$FULL_PATH" "$DEST"; then
    echo "Auto-archived: Tasks/$FILENAME -> Tasks/_done/$FILENAME"
  else
    echo "FAILED to archive Tasks/$FILENAME — it's marked done but still in Tasks/." >&2
    echo "  Move it by hand, or check permissions on Tasks/_done/." >&2
  fi
}

# --- Mode 2: sweep every task (Stop hook / manual diagnostic) -----------------
if [ "$1" = "--scan" ]; then
  # Report a missing dependency, but ONLY when it's missing. This mode doubles as
  # the Stop hook, so unconditional output would print every turn; staying silent
  # on a healthy system keeps the hook rule (say nothing when nothing's wrong)
  # while letting the manual run answer what the setup guide sends you here to ask.
  if ! command -v jq >/dev/null 2>&1; then
    echo "jq           : MISSING — the immediate (on-save) archive path is disabled."
    echo "               This sweep still works, so tasks marked done still archive;"
    echo "               they just wait for end-of-turn. Install jq to restore it."
  fi
  shopt -s nullglob
  for f in Tasks/*.md; do
    archive_if_done "$f"
  done
  exit 0
fi

# --- Mode 1: single file from hook JSON on stdin ------------------------------
# Only read stdin when it's a pipe (the hook feeds JSON in). Run by hand from a
# terminal, an unguarded `cat` blocks waiting for Ctrl+D — the script looks frozen
# and the natural reaction is to assume it's broken. `Core/scripts/CLAUDE.md` tells
# you to run these by hand when debugging, so that path has to work.
if [ -t 0 ]; then
  echo "Nothing to do — this mode expects hook input on stdin."
  echo "To sweep every task by hand, use:  bash Core/scripts/auto-archive-task.sh --scan"
  exit 0
fi

INPUT=$(cat)

# jq isn't installed everywhere. Without it the substitution below produces nothing,
# the 2>/dev/null swallows the reason, and the script exits 0 — so a dead hook and a
# working one look identical from the outside. Check for it and say so instead.
if ! command -v jq >/dev/null 2>&1; then
  echo "auto-archive-task: jq not found — this hook can't read the edit event." >&2
  echo "  Not fatal: tasks marked done are still archived by the Stop-hook sweep" >&2
  echo "  (--scan), just at end-of-turn instead of the moment you save." >&2
  echo "  Install jq to restore the immediate path." >&2
  exit 0
fi

FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty' 2>/dev/null)
[ -z "$FILE_PATH" ] && exit 0
archive_if_done "${FILE_PATH#$REPO_ROOT/}"
