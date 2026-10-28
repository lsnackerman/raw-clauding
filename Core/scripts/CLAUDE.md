# Scripts — background automation

Hooks and config that run quietly so the system stays consistent without manual maintenance.

---

## What's here

| File | What it does |
|------|-------------|
| **ensure-symlinks.sh** | Keeps `.claude/skills/` and `.claude/rules/` aligned with `Core/skills/` and `Core/rules/`. On first run, also creates `.claude/settings.local.json` (from the template here), `.claude/CLAUDE.md` (symlinked to AGENTS.md), and `Core/auto-memory/` (symlinked to Claude's native memory location, with a starter MEMORY.md). Idempotent. |
| **auto-archive-task.sh** | Watches Task doc YAML. When a task's `status` changes to `done`, it moves the file to `Tasks/_done/`. |
| **dup-check.py** | Checks that an actionable isn't tracked on two of `ALIVE.md` / `PULLING.md` / `THREADS.md`, the mutually-exclusive rule `/wrap` Step 1 teaches. Report-only; `/wrap` runs it at the end of Step 3, and you can run it by hand any time. Prints how many items it examined (a ✓ over zero items is not a pass) and exits 2 if it found none of the three files. |
| **settings.local.json** | Claude Code settings template. The source of truth for hook config; copied into `.claude/` by `ensure-symlinks.sh` on first run. |

## How hooks wire up

`.claude/settings.local.json` wires two scripts across three events:

- **`SessionStart`** — runs `ensure-symlinks.sh` (full scan: any new skill or rule gets a symlink)
- **`PostToolUse`** for Write/Edit — runs symlink + archive checks (on edits to `Core/skills/`, `Core/rules/`, or `Tasks/`)
- **`Stop`** — runs `auto-archive-task.sh --scan` once per turn as a backstop, in case a task got marked `done` by something that didn't trip the edit hook

The pattern: edit a file in `Core/`, the right thing happens. Add a new skill, it's a slash command right away (a new rule loads next session). Mark a task `done`, it auto-archives.

## Setup

First-time setup runs `ensure-symlinks.sh` from a terminal. After that, the SessionStart hook keeps everything in sync. No manual maintenance needed.

```bash
bash Core/scripts/ensure-symlinks.sh --check
```

**`--check` = "wire me up and tell me if it worked."** It forces a full scan and always prints the summary (`Setup check: 12/12 skills and 13/13 rules wired`) plus a non-zero exit if anything failed. Without the flag the script auto-detects a terminal, which works when a human runs it but *not* when an AI or a script runs it on your behalf, so the confirmation gets silently skipped. When in doubt, pass `--check`.

Safe to re-run any time, since it only ever creates what's missing and never overwrites. It's also the answer to *"is my setup actually wired up?"*, since it reports the counts.

If a hook seems idle, ask its diagnostic flag rather than running it bare (bare `auto-archive-task.sh` just says "Nothing to do"): `bash Core/scripts/auto-archive-task.sh --scan` sweeps (it archives any task marked done) and names `jq` if it's missing; `bash Core/scripts/ensure-symlinks.sh --check` wires up and reports. The task-archiving one is silent when healthy. Silence there means fine, not broken.

## Adding a hook

1. Edit `settings.local.json` to register the new hook
2. Add the script next to the existing ones
3. **Merge the new hook into `.claude/settings.local.json` by hand** (or ask the AI to). Re-running `ensure-symlinks.sh` will NOT do it. It only creates that file when it is missing, so it never overwrites permissions you have approved.
