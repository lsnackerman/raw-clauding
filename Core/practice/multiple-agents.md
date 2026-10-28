# Multiple agents on one document

The technique: two (or more) AI instances working on the same markdown file. Not at the same time but alternating, with the file as the meeting place.

---

## The pattern

You open two terminals, each with its own AI session: Agent A, Agent B. They don't talk to each other directly. They meet in a shared markdown file.

```
You + Agent A → think, write to file
   ↓
You switch terminals
   ↓
You + Agent B → read what A wrote, react, write back
   ↓
You switch back
   ↓
Agent A reads what B added, follows up
   ↓
...repeat as long as it's useful
```

You're the conductor. The file is the score. Each agent reads what's there when its turn comes; each agent writes back into the same place.

This is what *intelligence meeting intelligence in markdown* looks like at scale: the agents don't share a context window, but they share the file. The file IS the connective tissue.

---

## Why this works

- **Files outlive sessions.** Agents are ephemeral; the markdown is durable. The thinking accumulates in the file even as instances come and go.
- **Different agents bring different texture.** One Claude shaped by your engineering context, another shaped by your strategy context. Each shows up with what its conversation taught it. The file gets the benefit of both.
- **You stay the conductor.** You're not orchestrating an autonomous swarm; you're guiding a conversation across multiple intelligences. You decide what each agent reads, what each agent writes, how their work composes.

---

## When to reach for it

- **Splitting roles**. One agent does the thinking-partner work, another does the engineering / writing / research execution. Plug each into a different role; let the markdown carry the spec between them.
- **Cross-context combining**. Working in two different projects that suddenly want to share material. Agent in Project A drafts; agent in Project B adapts; you carry it across via the file.
- **Parallel angles**. Same source, two different lenses. One agent writes a thesis pass; another writes an FAQ pass. Both into the same file (or sibling files).
- **Bigger-than-one-context work.** When the work would blow out a single conversation's context, splitting across instances keeps each one focused.
- **By territory, in parallel.** Several sessions at once, each on a different task (one explores, one drafts, one routes). Each keeps its own context, with no bleed. That's parallel thinking, not chaos to manage. (`/explore` does a smaller version inside one session: several sub-agents, one reserve.)
- **For fresh eyes.** A second instance reads the same file cold, to catch what the first can't see from inside its own loop. That's `/fresh-eyes` as a skill.

**Before you split, ask: could a single agent + signposting do this?** Many agents isn't more-AI-is-better; it's structural separation, and structure has overhead. It earns its place when one thread genuinely can't hold the whole shape, when the angles would collapse into each other if one instance held both. If you'd just be switching tabs for its own sake, stay single and signpost instead.

---

## The constraint

**Not at the same time.** Two agents writing to the same file simultaneously will clobber each other (or hit file-lock conflicts). Alternate. While Agent A is writing, Agent B is idle (or reading). Switch turns explicitly.

The way you enforce this is just by being the conductor. You're the one switching tabs, you're the one telling each agent when to engage. There's no need for fancy locking; the human-paced rhythm IS the lock.

**Save after every edit you make yourself.** The file on disk is the shared state; both agents read it from there. An edit sitting unsaved in your editor is invisible to both of them, and if an agent writes to the file while your change is unsaved, you collide. Save before you switch turns, every time.

---

## A concrete example

Building a small app from scratch with no engineering background:

- **Window 1 — Thinking partner.** This Claude knew the *what* and *why*. You talked through what you wanted, what good looked like, why it mattered. Writing happened in the shared markdown: specs, decisions, constraints.
- **Window 2 — Engineer.** This Claude knew the *how*. It read the markdown, built code, wrote back what got implemented and what was still open. You'd point it at the spec and say "build this part."
- **You** — switching tabs, carrying signal across, asking each agent to read the latest before responding.

Neither agent ever talked to the other. The markdown was the meeting room. You were the conductor.

---

## Practical notes

- **Tell each agent what role it's in.** Don't assume. Say it explicitly: "You're in the thinking-partner role for this work; the engineer is in the other window. Read what they wrote, react to that, don't redo their work."
- **Use file structure to mark turns.** Section headers, dated entries, "Agent A added:" tags, whatever helps you (and them) see who said what last.
- **One source of truth per piece of work.** Don't have agents working on parallel copies "to merge later." That's where conflicts and lost texture happen. Same file, different turns.
- **If it gets confusing, take notes between turns.** If you're losing track, capture what you want each agent to focus on next in a small note, even just at the top of the file ("Next: Agent B, please add error handling"). This is the same principle as `/wrap` between sessions, scaled down to a single sitting.

---

## What this isn't

- **Not autonomous orchestration.** No agent calling another. You're always in the loop.
- **Not a multi-agent framework.** No special tooling needed. Two terminals, one file.
- **Not a scaling strategy for big teams.** This is a thinking technique, not a production architecture.

---

## Related

- **`Core/rules/sub-agents.md`** — when you DO want sub-agents (parallelizable research within ONE conversation), how to brief them well. Different shape: sub-agents run inside your session; the multiple-agents pattern uses separate sessions sharing a file.
- **`Core/skills/sync/SKILL.md`** — capture each session that participates so the conversation that happened in each window survives.
