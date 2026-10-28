# Hooks

*Shell scripts that fire automatically at Claude Code lifecycle points. Not AI, just bash running in milliseconds.*

---

## How it works

Hooks are registered in your settings (`Core/scripts/settings.local.json`, copied to `.claude/settings.local.json` on first run). Each hook has:

- **Event** — when it fires (SessionStart, PostToolUse, Stop, etc.)
- **Matcher** — optional filter (e.g., only fire on Write/Edit, not Bash)
- **Command** — the shell script to run

Scripts receive JSON on stdin (tool input details) and communicate back via exit code and output, and **where the output goes depends on the event**, which is the part that surprises people:

- **exit 0** → success, continue. Plain-text **stdout reaches the AI's context only on `SessionStart` and `UserPromptSubmit`** (plus two rarer events). For `PostToolUse` and `Stop` hooks (which is all three of ours except the SessionStart run), stdout goes to Claude Code's debug log, **not to the AI.** So a careful message printed by a Stop hook never reaches the AI that would act on it.
- **stderr** → the debug log only; the AI never sees it, *except* on exit 2.
- **exit 2** → the policy exit. On `PreToolUse` it blocks the tool call; on `PostToolUse` the tool already ran, stderr is shown to the AI as context, and the tool's own result is hidden from it (so an unintended exit 2 in a PostToolUse hook makes an Edit look like it vanished); on `Stop` it keeps the AI going instead of stopping.
- **any other non-zero exit** (`exit 1`) → non-blocking; the action proceeds. **Use `exit 2` to enforce something; `exit 1` only looks like it does.**
- If stdout is a **JSON object**, it's parsed for structured control on every event. Plain text isn't. (`systemMessage` is shown to *you*, not the AI; the field that adds context for the AI on `PostToolUse` is `hookSpecificOutput.additionalContext` at the time of writing, so check the reference for the current name before relying on it, since hook fields change between versions.)

*(Checked against the Claude Code hooks reference, https://code.claude.com/docs/en/hooks. Hook semantics change between versions; if a hook seems to behave differently, the reference wins over this page.)*

**Consequence for the two hooks below**: they can act, but they mostly can't *tell you* anything from the hook path. That's why each one has a diagnostic flag you run by hand. It's the only channel through which a hook can report on itself.

**Performance**: scripts run in milliseconds. Silent exits cost zero tokens.

---

## Your hooks

This system ships with two hooks. Both live in `Core/scripts/`, and each has a diagnostic flag you run from a terminal: **`--check` for the setup script** (it wires things up *and* tells you whether it worked; it always prints), **`--scan` for the task archiver** (it names `jq` if it's missing, and it *archives* anything marked done).

### 1. ensure-symlinks.sh

**Triggers**: SessionStart + PostToolUse (Write/Edit)

**What**: keeps `.claude/skills/` and `.claude/rules/` in sync with `Core/skills/` and `Core/rules/`. Skills live flat (`Core/skills/{name}/SKILL.md`); the hook creates one symlink per skill in `.claude/skills/{name}` so Claude Code discovers it as a slash command. It also removes broken symlinks and tells you when a real file or folder is sitting where a pointer belongs (the silent two-copies case, where edits to one never reach the other). On first run it does the rest of the wiring too, creating `.claude/settings.local.json` from the template in `Core/scripts/`, `.claude/CLAUDE.md` (symlinked to AGENTS.md), and `Core/auto-memory/` (symlinked to the AI's native memory location, with a starter MEMORY.md).

**Why**: missing symlinks used to mean hand-checking. Now you never check again. Add a new skill (just make the `Core/skills/{name}/` folder + `SKILL.md`) and the hook wires the symlink instantly, because it fires on every Write/Edit, not only at SessionStart. **Trust it. Don't hand-create symlinks.** Doing it manually forces a rejected tool call and breaks flow; the hook exists precisely to take this off your plate.

**Check**: `bash Core/scripts/ensure-symlinks.sh --check` — wires up anything missing and prints the summary (`N/N skills and N/N rules wired`). It only mentions `python3` when it's **missing**; a healthy run says nothing about it, which is by design. This is the one to run when you're not sure setup worked.

### 2. auto-archive-task.sh

**Triggers**: PostToolUse (Write/Edit) **and** Stop (as `--scan`, a once-per-turn sweep)

**What**: when a task file's YAML `status` is set to `done`, it auto-moves the file to `Tasks/_done/`. The PostToolUse run catches the edit the moment it lands; the Stop sweep catches anything the per-edit run missed. (The per-edit run needs `jq`; if it's missing, the Stop sweep still archives, just at end-of-turn instead of instantly.)

**Why**: the manual `mv` step you'd otherwise do at the end of every wrap is gone.

**Scan**: `bash Core/scripts/auto-archive-task.sh --scan` — sweeps every task now, and names `jq` if it's missing. **A hook that's quietly idle and a hook that's quietly broken look identical from the hook path; this flag is how you tell them apart.**

---

## Config location

Hook config lives in `Core/scripts/settings.local.json` (the template, the source of truth) and gets copied to `.claude/settings.local.json` on first run by `ensure-symlinks.sh`. The hooks block looks like this:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/Core/scripts/ensure-symlinks.sh" }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/Core/scripts/ensure-symlinks.sh" },
          { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/Core/scripts/auto-archive-task.sh" }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/Core/scripts/auto-archive-task.sh --scan" }
        ]
      }
    ]
  }
}
```

**Important**: always use `"$CLAUDE_PROJECT_DIR"` (with quotes) in hook commands. Relative paths are fragile and depend on Claude Code's working directory; `$CLAUDE_PROJECT_DIR` always resolves to the project root.

---

## Adding a new hook

1. Write the script in `Core/scripts/` and make it executable (`chmod +x`)
2. Design for two modes:
   - **Hook mode**: reads JSON from stdin, checks if relevant, exits silently if not
   - **Scan mode**: a `--scan` flag for a full system audit you can run by hand, and have it **name any dependency it needs** (`jq: MISSING`), because the hook path can't tell anyone
3. Keep it silent unless acting, and remember the hook path can't report anyway (see § How it works); the flag is your reporting channel
4. Register it in `settings.local.json`, then **copy the change into `.claude/settings.local.json` by hand**, because re-running `ensure-symlinks.sh` will not propagate it (it only creates that file when missing, so your approved permissions are never clobbered)
5. Test both modes before wiring it in
6. Update this doc

---

## Available events

Events this system uses:

- **SessionStart** — session begins. Good for "make sure everything's wired up" checks.
- **PostToolUse** (matcher: `Write|Edit`) — after a file is written or edited. Where most hooks live.
- **Stop** — the AI finishes responding. Good for once-per-turn, end-of-turn work (like rebuilding a static artifact).

Events available but not used here:

- **PreToolUse** — before a tool runs. Can block (exit 2). Good for safety gates.
- **UserPromptSubmit** — before a prompt is processed. Could validate or transform input.
- **PreCompact** — before context compaction. Could save state.

The current hooks are all reactive. They fire *after* something happens and surface a warning or do a fix-up. PreToolUse can *block* an action before it runs (exit code 2 = blocked, stderr becomes feedback). The tradeoff is prevention vs detection: a warning you can fix is collaborative; a gate you must pass is authoritative. For a partnership system, detection usually feels more aligned, since it informs rather than controls. Reach for prevention when the cost of catching a mistake *after* is much higher than preventing it (security-sensitive or destructive operations).

---

## Design principles

- **Silent by default** — if nothing's wrong, say nothing (zero token cost)
- **Idempotent** — safe to run repeatedly, no side effects on re-runs
- **Fast** — milliseconds, not seconds. Parse JSON, check one thing, exit.
- **Scan mode** — every hook doubles as a diagnostic tool (`--scan`, or `--check` for the setup script) that names what it needs
- **Forward-looking** — hooks prevent future drift; existing backlog gets cleaned organically when files are touched
