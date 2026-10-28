# Core — AI working context

The operational engine. AGENTS.md has the compass. This file orients you for working inside Core/.

## How the parts relate

- **skills/** — repeatable workflows invoked via `/name`. The partnership's active toolkit. See `skills/CLAUDE.md` for the full menu.
- **rules/** — operational patterns (auto-load via `.claude/rules/` symlinks). How we work.
- **lenses/** — ways of *seeing*. The `/gut` set, applied at a decision; also load when you want to understand how partnership-thinking works. Flat (one folder, one lens per file). *(Who the partners are lives in `Core/you/` + `Core/opus/`, not as a lens.)*
- **foundations/** — the ground you orient *from*: the four assumptions, the 3 C's, why the system works. *Distilled* substrate.
- **practice/** — ways of *working*: the two loops, handoffs, the USER-GUIDE. *Distilled* substrate.
- **mechanics/** — true plumbing: how the tooling and file-layer mechanically work (the one-time setup guides, yaml, markdown, symlinks, hooks, file recovery, Claude Code usage). *Distilled* substrate.
- **reserves/** — concept hubs preserving raw thinking across sessions, maintained by `/explore` and `/wrap`. *Raw, accreting* internal substrate, sister to `sessions/` (raw conversation). Reserves graduate to a depth cluster (`foundations/`, `lenses/`, `practice/`, `mechanics/`) or a rule when a concept crystallizes.
- **sessions/** — thinking archives. Both voices, verbatim. The foundation.
- **scripts/** — automation that runs in the background (symlink sync, task auto-archive) plus `dup-check.py`, which `/wrap` runs.
- **auto-memory/** — directory symlink to Claude Code's auto-memory location. `MEMORY.md` index + individual memory entries, auto-loaded every session. Shared context is foundational, and directory-level surfacing (vs file-only) lets both partners browse individual memories, not just the index.
- **opus/** — the AI's space. Reflections, observations, things previous instances wanted future ones to find. Not documentation about the AI but a place for it to put things.
- **you/** — your space (sister to `opus/`). Who you are, so the AI can meet you instead of serving you. Rename it to your name if you like.

**The loop**: sessions/ + reserves/ accrete raw substrate (conversation + concept) → the depth clusters (foundations / lenses / practice / mechanics) distill when concepts crystallize → rules/ operationalize the patterns that need to auto-load → skills/ enact the workflows → sessions/ capture what happens → captured patterns feed back into reserves/, the clusters, and rules/.

## What the rules teach

These auto-load at session start, so you carry them before you know you need them. They cover file work, routing what lands, retrieval, the disciplines of thinking *together*, partnership-mode, the pointing-vs-holding diagnostic, state-in-structure, codification, persist-before-pause, briefing sub-agents, security (look before anything leaves the folder), the concept ping-layer (`concepts.md`, which starts nearly empty and grows from what you catch), and the frame for THIS human (`you.md`).

**Full annotated set → `rules/CLAUDE.md`.** (Kept there, not restated here, so there's one canonical list that can't drift out of sync. That's `pointing-vs-holding.md` in action.)

## Vocabulary you'll encounter here

- **Compound thinking** — thinking that compounds across sessions via files
- **Skill Check** — self-improvement step in every skill (bitter lesson applied)
- **Generative friction** — friction that sharpens thinking (vs degenerative that wastes time)
- **Warm start** — returning with full context (vs cold start from zero)

## Plumbing

**Skill symlinks**: `.claude/skills/` contains symlinks → `../../Core/skills/X`. This is how Claude Code discovers skills as slash commands. If a skill isn't showing up, check the symlink. The ensure-symlinks hook handles this automatically.

**Rule symlinks**: `.claude/rules/` contains symlinks → `../../Core/rules/X`. Rules auto-load at session start.

**Hooks**: Two automation scripts in `Core/scripts/` fire via `.claude/settings.local.json`. Symlink sync runs on SessionStart and PostToolUse. Task auto-archive runs on PostToolUse for Edit/Write, with a sweep on Stop. See `Core/scripts/CLAUDE.md`.
