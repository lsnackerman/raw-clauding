# Shared memory

*AI arrives knowing things, without searching first.*

---

## How it works

Claude Code has built-in memory: files in a special directory get loaded into every new conversation automatically. AI sees them before you say a word.

The setup script (`Core/scripts/ensure-symlinks.sh`) handles everything:
- Creates the auto-memory directory in Claude Code's native location
- Seeds it with a starter MEMORY.md
- Symlinks the whole directory into your repo at `Core/auto-memory/` for visibility

The real files live where Claude Code auto-loads them. The directory symlink in your system folder lets you see and browse the full auto-memory cluster: MEMORY.md as the index plus any individual memory entries as they accumulate. AI has autonomous write access to its own memory and can update it without asking permission.

**Why a directory symlink instead of just a file symlink?** Shared context is foundational in a 50/50 partnership. Surfacing only the index hides the individual memories from the human partner. Surfacing the whole directory means both of you can browse what's been remembered, not just the pointer to it.

If you need to redo this manually (or want to understand the plumbing), see the sections below.

---

## Why it's set up this way

Two files auto-load at session start:

| File | How it loads | Job |
|------|-------------|-----|
| **AGENTS.md** | Claude reads `.claude/CLAUDE.md` (symlinked to AGENTS.md) | The compass |
| **Core/auto-memory/MEMORY.md** | Claude Code reads from its native auto-memory directory | The cheat sheet |

Two more files the AI checks on demand:

| File | When it's read | Job |
|------|---------------|-----|
| **ALIVE.md** | AI checks at session start or during `/pickup` | The whiteboard |
| **THREADS.md** | AI checks during `/pickup` and updates during `/wrap` | The continuity |

Without MEMORY.md, AI reads the compass but doesn't know the shortcuts. With it, AI arrives already knowing where important files are, what conventions you've established, and what patterns you've earned together.

---

## The 200-line budget

Claude Code truncates memory files after 200 lines. This is a feature. It forces you to keep shared memory tight and high-signal.

If you need more depth on a topic, create a separate file and link to it from MEMORY.md. The memory file is the index; the linked files are the depth.

---

## What goes where

| If it's... | Put it in |
|-----------|-----------|
| How you work together, values, identity | **AGENTS.md** |
| Where things are, operational shortcuts, earned patterns | **MEMORY.md** |
| Session handoff, what's next | **ALIVE.md** |
| Direction, goals | **VISION.md** |
| Ideas, brain dumps | **SCRATCHPAD.md** |
| Threads that won't let go between sessions | **PULLING.md** |
| What got done, per-session bulleted record | **THREADS.md** |
| A workflow or repeatable process | **A skill** |

---

## Manual setup (if needed)

If the setup script didn't run or you need to recreate the memory link:

```bash
# 1. Find your Claude Code memory directory
ls ~/.claude/projects/

# 2. Look for the folder matching your repo path
#    (EVERY character that isn't a letter or number becomes a hyphen — not just
#     slashes. A space, dot, underscore or plus in your folder name all become
#     hyphens too, e.g. /Users/you/My OS.v2 → -Users-you-My-OS-v2. Guessing
#     "slashes only" is the classic wrong turn here, and it fails silently:
#     you'd create a MEMORY.md in a folder the AI never reads.)

# 3. Create the memory file
mkdir -p ~/.claude/projects/{your-project-folder}/memory/
cat > ~/.claude/projects/{your-project-folder}/memory/MEMORY.md << 'EOF'
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
EOF

# 4. Symlink the auto-memory DIRECTORY into your repo
ln -s ~/.claude/projects/{your-project-folder}/memory Core/auto-memory
```

---

*The goal: the AI arrives oriented, not blank.*
