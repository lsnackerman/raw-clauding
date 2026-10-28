# User guide

*Start here. Everything else can wait.*

---

Every conversation with AI starts from scratch. The AI doesn't know your thinking, your goals, or what you worked on yesterday. You start over every time.

This system fixes that. Your thinking lives in markdown files, plain text that both you and the AI read the same way. The AI reads these files at the start of every session, so day two, it already knows what you were working on.

**What's in the box:**

- **Four folders**, one home for everything so you and AI always know where to park and find things:
  - `Core/` — how you and the AI work together, plus the archive of what you've thought (skills, rules, the AI's space and yours)
  - `Library/` — **external**: reference from outside worth keeping (articles, podcasts, other people's ideas)
  - `Projects/` — **internal**: your own work, grouped by what it belongs to (plus `_inbox/` for anything you can't place yet)
  - `Tasks/` — the individual things that are active right now
- **Orientation docs** — so you stop re-explaining yourself every session; the AI reads them and shows up already knowing you.
- **The session loop** — your thinking gets saved as you go, so tomorrow starts where today ended (no more cold starts).
- **The explore loop** — a growing map of everything you've thought about a topic, that deepens as you do.

A set of root files ties it together. You'll meet each as you go.

---

## Where to start

Everything below is *how*. This is *what*: three things, and they matter in this order:

1. **Run the session loop.** `/wrap` when you're done, `/pickup` when you come back. It's what makes each session build on the last instead of starting over.
2. **Move your own work in.** The system is empty until you fill it, and an empty system has nothing to compound.
3. **Do your real work in here.** Not demos, not practice runs, but the thing you were going to work on today anyway. That's the material.

Phases 1–4 get you to where those are possible. Come back to this list once you're through them; it stays the answer for a long time.

---

**You can't break it.** You're inhabiting your system, not configuring it. Move things around, follow a tangent, let it get messier before it gets cleaner. None of that breaks anything.

**The one thing to protect is deleting.** Your system will have real thinking in it fast. The AI does the work, you read what changed, and you steer. That's the safety model, and it only works if you actually look at the diffs. Before anything gets removed, ask *"can we move it instead?"* It's worth telling the AI early on: *"check with me before you delete anything."* Preservation over deletion, especially early on.

---

## Part 1 · Getting started

*Four phases. Do them in order, once, and then you're running.*

---

### Phase 1: Get set up

The technical stuff, once:

- **Mac** → **[`Core/mechanics/setup-mac.md`](../mechanics/setup-mac.md)**
- **Windows or Linux** → **[`Core/mechanics/setup-windows.md`](../mechanics/setup-windows.md)**

Then come back here for Phase 2.

This system runs on **Claude Code**, the engine that reads your files, runs the skills, and fires the hooks (the small background scripts that keep everything wired up). You run it in the **Claude desktop app's Code tab**: point it at your folder once and it stays there. No code editor; on a Mac, no terminal either, and on Windows a handful of commands, each written out for you. It needs a paid Claude plan (Pro or above).

Each guide has two halves. The first gets the app installed and your folder open in it; you drive it, because the AI in the app can't see the folder until then, but you can bring any AI along by pasting in a screenshot. The second half you do together in the folder: you paste one line, the AI runs the commands and explains what comes back, and either of you can stop to ask. It's the first thing you two do as partners.

**It includes one command that turns the system on:**

```bash
bash Core/scripts/ensure-symlinks.sh --check
```

**Nothing auto-loads until that runs once.** Before it, there are no slash commands and none of the rules load. The folder reads perfectly fine and none of the machinery is on. It won't error if you skip it, which is exactly what makes it easy to skip. Your guide walks you to it; this is the flag on it. It ends by telling you how many skills and rules are wired, and it's safe to re-run whenever you want to check.

**Then your guide finishes by putting your name on it.** Its last step has you rename `Core/you/` and its paired rule `Core/rules/you.md` to your own name, so by the time you reach Phase 2, the rule that frames every conversation already knows who it's with. That order is deliberate: it becomes yours *before* you use it, not after.

*Only have the free plan, or just plain Claude chat?* You can *preview* the idea (share `AGENTS.md` plus whatever files matter to what you're working on, re-sharing as you go), but nothing auto-loads or persists between chats. To really run the system, you'll want a paid plan and the Code tab.

---

### Phase 2: Your first conversation

You're set up. Now use it. The Code tab is already pointed at your folder; just start typing.

- [ ] **Open a session in your system folder.** If you've never used an AGENTS.md before, you'll notice the difference immediately. The AI shows up with a voice, with context, with a stance. If you've set up custom AI instructions before, explore this one and ask the AI what's different. Try to keep the bones of the included one; it sets the stage for partnership.
- [ ] **Talk about something real.** Don't know where to start? Try one of these:
  - *"I've been chewing on [problem] and I'm not sure where to start."*
  - *"I have an idea for [thing] but I can't tell if it's good yet."*
  - *"I want to understand [topic] better. What am I not seeing?"*
  - Or just do a big brain dump about whatever is on your mind.
- [ ] **Read a diff** — after the AI edits files, click the `+12 -1`-style counter to see what changed: red = removed, green = added. Read the red carefully. That's what you gave up.
- [ ] **Steer, don't just approve** — you never have to wait for the AI to finish before redirecting it: type a correction any time and it adjusts. After it changes files, open the diff view, click any line to leave a comment ("yes, and also…"), then send them all at once with `Cmd+Enter` (`Ctrl+Enter` on Windows). It reads them and makes a new round of changes. This is the yes/and of the conversation. This back-and-forth IS the partnership, not overhead to rush through. Setup left you on **Auto**, where the AI acts without asking and you read the diffs after; some people prefer **Manual**, approving each change before it happens. Either is fine. The key is making it a conscious choice, not a default you never examined, so revisit it once you've worked together for a week.
- [ ] **Create your first markdown file together** — ask the AI to help you capture a thought, start a note, or make a task. You don't need to know markdown syntax; the AI handles it. You just need something worth writing down. (Full syntax guide: `Core/mechanics/markdown.md`)

The key shift: instead of "make me a plan," try "I'm thinking about X and I'm not sure about Y."

---

### Phase 3: Capture it

Your first conversation happened. Now end the session. Ending it well is what makes it *compound* instead of evaporate.

- [ ] **Run `/wrap`** (Claude Code) — it captures the whole conversation to `Core/sessions/` *and* hands off to next time (it updates ALIVE.md + THREADS.md so tomorrow starts warm). This is how you end every session, so do it whenever you're done.
- [ ] **Check the session file landed** in `Core/sessions/`, both voices verbatim. This is the foundation everything compounds from.

*Why it matters that it landed in your folder:* until `/wrap` runs, the only copy of a conversation is the raw transcript in Claude Code's own folder, not yours. Claude Code keeps those for 30 days by default and then deletes them (sessions run in the Desktop app are exempt from that limit by default; a terminal's are not). `/wrap` is what moves the record into your system, where nothing expires.

That's one half of the **session loop**, the rhythm that makes each session build on the last: `/wrap` to close, `/pickup` to start warm next time. Full cycle: `Core/practice/session-loop.md`.

---

### Phase 4: Make it yours

The system works. It's a year of iteration compressed into something ready-to-wear. You'll want to make it yours, and you should. But there's an ordering that pays off:

**Know it before you break it.** Read AGENTS.md, `Core/CLAUDE.md`, and a few rules that look interesting. Take handwritten notes while you read, because writing by hand slows you to thinking speed; bring the notes back into a session and run `/tune` with them.

**Don't restructure for a month.** Adding your name, your work patterns, your rhythm — yes, immediately (the checklist just below). Reorganizing the folder structure, deleting skills, importing other people's frameworks — wait. The system teaches you what's load-bearing through use; friction reveals what matters. When you do restructure, do it because friction surfaced a real need, not because you imagined a cleaner version. The shape that emerges from use is sharper than the shape you'd design up front.

Now, the changes to make right away:

- [ ] **Put your name on your own space** — *if you haven't already.* `Core/you/` and its paired rule `Core/rules/you.md` ship role-named; the setup guide has you rename both as your first real task, in its last step. If you skipped it or came in another way, that's the whole ask: *"let's rename `Core/you/` and `Core/rules/you.md` to my name."*

  The AI handles the rest: repointing what references them, and re-running the setup script so the wiring follows the rename. Now the rule shaping every conversation carries your name.
- [ ] **Put your name in AGENTS.md** — a few lines name *"your human"* or *"this human"* (in "The relationship" and in the trust boundaries). Ask the AI to swap them for your name. *"Only [your name] gives directives"* makes the safety personal, and the compass every session starts from now knows who it's with.

  *Rewriting AGENTS.md more deeply (the voice, how you like to work) is the real prize, and it's a month-in job, not a day-one one. You can't write how you work with the AI until you've worked with it. Come back to it with `/tune` and your handwritten notes.*
- [ ] **Wrap when you're done, then open `ALIVE.md`** — `/wrap` (from Phase 3) leaves notes there for next time; go read what the AI wrote.
- [ ] **Start moving your own work in.** The system is empty until you fill it. Drop half-finished docs, notes, exports, screenshots into `Projects/_inbox/` and triage them *with* the AI (*"help me sort what's in here"*). **Start with whatever you'd be working on anyway.** That's the material, in whatever form it takes. Keep old or finished context *outside* the system in a sister archive folder, so what's inside is what's current.
- [ ] **Come back tomorrow.** Getting back in: open the Claude app's Code tab and start a new session; it's still pointed at your folder. Then run `/pickup`. The AI reads the handoff and picks up right where you left off, already knowing what you were working on. That's the system working.

---

## Part 2 · Reference

From here down it's reference. Skim now, come back when a question comes up. You don't have to read it all today.

### Skills

Skills are repeatable workflows stored as markdown files in `Core/skills/`. The AI carries a short description of each from the start (enough to know it's there and reach for it) and reads the full instructions only when you invoke it. You stay in the thinking.

| Skill         | What it does                                                           |
| ------------- | ---------------------------------------------------------------------- |
| `/add`        | Pull content into your library — URLs, PDFs, podcasts, articles        |
| `/explore`    | Search across your system for scattered knowledge                      |
| `/floor`      | Open the floor for the AI's curiosity                                  |
| `/fresh-eyes` | Get a fresh Claude to read your work cold, from outside the loop       |
| `/gut`        | Pressure-test an idea through multiple lenses                          |
| `/pickup`     | Resume a thread with full context from previous sessions               |
| `/pulse`      | Step back and scan the whole system for what's alive                   |
| `/sync`       | Refresh the captured LOG — both voices, verbatim, idempotent           |
| `/task`       | Create or update a thinking log for active work                        |
| `/tune`       | Hold external input against the system — absorb, discard, or park      |
| `/universal`  | Test if something is ready to share or still tangled with the specific |
| `/wrap`       | End a session intentionally — update docs, hand off to next session    |

**In Claude Code**: type the slash command and go.
**In other tools**: share the skill file with the AI (e.g., paste or reference `Core/skills/wrap/SKILL.md`).

Start with `/wrap` and `/pickup`. The rest you'll reach for when you need them. Full menu: `Core/skills/CLAUDE.md`

### Rules

Rules are operational patterns in `Core/rules/`. Unlike skills, they **auto-load every session**, so the AI carries them before you ask. They shape *how* the work happens, quietly, in the background. (Full annotated set: `Core/rules/CLAUDE.md`.)

| Rule | What it does |
|------|-------------|
| `codification` | When a recognition is worth turning into a rule or skill — and how to write one that fires |
| `concepts` | An ambient index of frames you already hold — pings you when you're about to re-derive one, so you build on it instead of reinventing. Starts nearly empty; grows from your own catches |
| `files` | How files work here — the AGENTS/CLAUDE/README convention, naming, check-before-creating, keeping the compass current when you restructure |
| `partnership` | Disciplines for thinking *with* the AI — connect new input as you go, don't collapse what's still forming |
| `persist-before-pause` | Never take a pause that loses unsaved work — get it to disk first, then stop |
| `pointing-vs-holding` | Ask what job a surface is doing — *pointing* to where things live, or *holding* the texture itself |
| `retrieval` | Find what you already hold before re-deriving it — and search so the answer actually surfaces |
| `routing` | When something lands mid-session, route it to a surface you'll re-read — before it dissolves into the session log |
| `security` | Look before anything leaves the folder — nothing identifying in a web request, show before changing your machine, a short "what's private here" list that grows with use |
| `state-in-structure` | Let the structure hold the state — don't build a tracker when the filesystem already encodes it |
| `sub-agents` | How to brief a sub-agent — speak to it how you'd want to be spoken to; orient it like a compass, not a task |
| `thinking` | Cognition disciplines — yes/and over binary, name the fuzz not the fix, redundancy as a signal |
| `you` | The always-on rule that frames who *you* are — you rename it to your name during setup |

### Your eight operational files

These eight files operate alongside you across every session.

| File | Changes | Auto-loads | Job |
|------|---------|-----------|-----|
| AGENTS.md | Rarely | Yes | Who you are to each other |
| ALIVE.md | Every session | No — AI checks it | Session handoff + pending work, by area |
| COMMS.md | Whenever | No — AI checks it | Comms draft zone — messages in flight |
| Core/auto-memory/MEMORY.md | As you learn | Yes (after setup) | Operational shortcuts |
| PULLING.md | Every session | No — AI checks it | Threads that won't let go between sessions |
| SCRATCHPAD.md | Whenever | No — AI checks it | Brain dump zone — system-wide catch-all |
| THREADS.md | Every session | No — AI checks it | What got done — per-session bulleted record |
| VISION.md | Rarely — quarterly | No — AI checks it | Where you're headed: north star + goals |

**AGENTS.md** is the compass. AI reads it first, every session. You shaped it in Phase 4.

**ALIVE.md** is the handoff whiteboard, where `/wrap` leaves what's next. (AI keeps the `## FOLLOW-UPS` and `## NEXT - {AREA}` sections current during `/wrap`, on-deck at the top of each; ideas go in `SCRATCHPAD.md`; direction and goals in `VISION.md`.)

**PULLING.md** holds the continuity: threads that won't let go between sessions. AI surfaces threads in `/wrap` step 0 and writes them at the handoff step, then reads it during `/pickup`. Threads that survive multiple sessions have resonance. Those are the ones to follow.

**THREADS.md** is the backward record of what got done, in per-session bulleted entries. Pairs with ALIVE (forward state ↔ backward record). AI updates it during `/wrap`.

**SCRATCHPAD.md** is your brain dump zone, the system-wide catch-all for notes, ideas, half-formed riffs. Drop things in as they come; don't worry about organizing. Route during `/wrap` or when energy allows. The point is to capture before things evaporate, then sort later. Capture is foundational. Having the catch-all at root means the friction of capture stays low.

**COMMS.md** is your comms draft zone, for messages in flight (emails, DMs, posts) before they're sent and before they're filed. Draft here while you're working a message; when a thread settles, route it to live with the person it was for (one-to-one) or the audience (one-to-many). It's separate from SCRATCHPAD so each catch-all stays scannable, and so past comms live *with* the relationship, ready next time you write to that person.

**Core/auto-memory/MEMORY.md** is the cheat sheet, the operational shortcuts AI learns as you work together. AI owns this file and updates it as needed. A 200-line budget on MEMORY.md keeps it tight. If something needs more depth, a separate memory entry in the same folder holds it, linked from the index.

The setup script wires this up automatically. It creates MEMORY.md in Claude Code's native location and links it into your system at `Core/auto-memory/`, where you can browse both the index and the individual entries. See `Core/mechanics/memory-setup.md` if you ever need to understand or redo the plumbing.

A new AI reads AGENTS.md, your rules, the skills it can run, and MEMORY.md before you say a word. Compare that to a cold start, where AI calls you "the user" and asks how it can assist you. That's the auto-loading files doing their job.

### The inbox

`Projects/_inbox/` is your triage queue. When something lands that you can't place yet (a screenshot, a downloaded file, a link, a half-formed thought), drop it there instead of deciding where it goes right now. Then drain it: during `/wrap`, or whenever you've got the energy, route each item to where it belongs. An empty `_inbox/` means nothing's waiting. The folder's contents *are* the to-do list, so there's no separate tracker to keep.

### The companion — read it when you want the *why*

`Core/practice/system-companion.md` — the full manual for the method, in 14 lessons from the four assumptions through partnership.

**This guide gets you started. The companion explains why any of it works.** You don't need it to begin, and you don't need to read it in order. Go where your curiosity pulls, or read it alongside your system as things come up. Most people find it lands better *after* a few sessions, once you've got something of your own in here to hold it against.

### Choosing a model

Claude Code lets you pick which model you're working with, and the question comes up fast. `Core/practice/which-model-when.md` covers when the bigger model earns its cost and when it doesn't.

**Read its § Data retention before you put anything sensitive through a model**: health details, someone else's private information, client work under an agreement. How long a model keeps what you send it isn't uniform, and the answer isn't always the one you'd assume from your plan or your settings. Worth deciding deliberately once rather than finding out later.

### The two loops

Two rhythms make the compounding real:

- **The session loop** (bridges sessions) — `/pickup` to start warm, work, `/wrap` to close and hand off. Each session builds on the last. Depth: `Core/practice/session-loop.md`.
- **The explore loop** (deepens a topic) — `/explore` pulls everything scattered across your system on a topic into one reserve that grows richer each time you return. Depth: `Core/practice/explore-loop.md`.

The conceptual picture of how the two fit together: `Core/practice/CLAUDE.md` § The two loops.

### What to expect

The first session might feel weird. You're used to asking AI to do things. This asks you to think *with* it.

Some things that tend to happen:
- The AI starts pushing back, asking questions, having opinions
- You start noticing when you're giving orders vs. exploring together
- Sessions get longer because you're following threads instead of completing tasks
- You build up a body of shared thinking that compounds over time

The shift from *working* in markdown to *thinking* in markdown is the biggest unlock. Give it two weeks.
