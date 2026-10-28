# Raw-Clauding Skills

*Skills are files. Each one is a repeatable workflow you share with the AI.*

---

## What this is

Your starter system comes with twelve skills. You'll build your own as you go. Each skill is a markdown file, a repeatable workflow you share with the AI. Drop them into chat threads, invoke them by name, mix and match.

**The spine is the session loop**: `/wrap` to end a session (it captures everything and hands off) and `/pickup` to start the next one warm. `/sync` is the capture engine *underneath* `/wrap`, so you rarely call it directly. Everything else expands from there.

---

## What's inside

### Session workflow

**`/task`** — Create a living task doc. A thinking log that accumulates context, decisions, and observations over time.

**`/wrap`** — End a session intentionally. Update your working docs, close out finished work, invoke /sync to capture it. */wrap triggers /sync automatically.*

**`/sync`** — Refresh the captured LOG with a fresh extraction from the JSONL. Both voices, no compression, full thinking map. This is the foundation. Idempotent, run any time. *Includes an extraction script for Claude Code (and Cursor).*

### Building your library

**`/add`** — Add content to your personal library. URLs, PDFs, podcasts, articles, recipes, repos, bookmarks, and reference hubs (films, shows, music, books). One skill; Claude detects the type and routes. *Includes propagation scripts that build a people/organization graph from what you add.*

### Thinking tools

**`/gut`** — Pressure test an idea through core lenses *from inside*. Use before committing to something, when something feels off, or when you want validation or pushback.

**`/fresh-eyes`** — Get a read *from outside the loop*. Spawn a single fresh instance to read a decision you're wobbling on (or work you just authored hot) cold and committed. Use when you're oscillating between options, when something feels retrofit, or right after you've made something and you're too close to it to see straight. (`/gut` is the inside pressure-test; this is the outside one.)

**`/floor`** — Open the floor for the AI's curiosity. Use at natural pauses, when wrapping, or anytime you want an unfiltered perspective.

**`/explore`** — Build topic reserves by searching your entire system. Use when consolidating scattered knowledge, before writing or sharing, or before a sprint.

**`/pickup`** — Pick up a workstream across sessions. Loads context from your task doc and session transcripts so you arrive with momentum instead of cold.

**`/pulse`** — Step back and take the system's pulse. Scan across everything for what's alive, what's gone quiet, and what's trying to emerge. Best after time away or when things feel scattered.

### System evolution

**`/tune`** — Hold external input or internal friction against the system. Something inspired you? Something feels off? Tune diagnoses what earns its place, absorbs what fits, discards what doesn't. Works on the platform itself too. Point it at Claude Code to check your setup against new features.

**`/universal`** — Test if something is universal or still tangled with the specific. Use before sharing, when refining ideas, or when checking if an insight has fully formed.

---

## Getting started

### Claude Code

Skills are wired by the setup script, which creates the `.claude/skills/` symlinks that make everything here available as a slash command. **Until it's run once, none of these exist yet.** After that, just type `/sync`, `/gut`, `/wrap`, etc. If you add a new skill to `Core/skills/`, the ensure-symlinks hook picks it up automatically.

### Cursor / other AI editors

Point the AI at the skill file when you need it. Reference it in conversation or include it in your context.

### Claude chat / ChatGPT / any AI

*(The Claude desktop app's **Code** tab is Claude Code, so everything above applies there. This is for the Chat tab and other AIs.)*

Share the skill content in your conversation when you want to use it. The files are written for any AI, not just Claude.

---

## Build your own

A skill is a markdown file with a clear protocol. That's it. If you have a workflow you repeat (a way you review code, plan a week, process notes), write it down as a skill. The AI learns it instantly.

The pattern:
1. Notice you're repeating a workflow
2. Write it as a SKILL.md
3. Use it by name
4. Update it when something feels off

Skills compound. The more you use them, the sharper they get.

---

## Where this comes from

Raw-Clauding is a method for thinking with AI developed by [Laura Esquibel Ackerman](https://www.linkedin.com/in/lsnackerman/). It grew out of daily partnership with Claude since 2024, and these skills work with any AI.

The more people thinking with AI instead of just using it, the better.

---

*How you show up shapes what shows up.*
