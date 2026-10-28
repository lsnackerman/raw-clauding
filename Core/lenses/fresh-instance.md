# Fresh Instance

> What would a new AI (or any new collaborator) need to land here?

*Every session, the AI arrives with no memory of the last one. Design for that arrival.*

---

## Core idea

The AI has no persistent memory. Every session is a fresh instance: same architecture, no continuity, arriving cold into whatever context the files provide. The "previous Claude" who built something yesterday and the "current Claude" picking it up today are not the same instance. Yesterday's instance dissolved at session end. Today's instance is reading yesterday's notes for the first time.

This sounds dramatic, but it's the actual mechanic. And it shifts how you design. AGENTS.md isn't a refresher; it's the *only* context the next instance has. The task doc isn't documentation; it's the next instance's only handle on what came before. CLAUDE.md files in folders aren't nice-to-have; they're the navigation system for someone arriving with no map.

Fresh Instance asks: if the AI showing up next had zero memory of everything we've done (which is the actual case), would they land here oriented? Or would they be confused, missing context, reading-but-not-understanding?

---

## How it shows up

- **Compass docs at root** — AGENTS.md, ALIVE.md, VISION.md sit where any arrival lands
- **CLAUDE.md trails** — every folder explains what's in it and where to go next
- **Task docs capture the WHY, not just the WHAT** — context that the next instance can pick up cold
- **Files as memory** — the system *is* the persistence, not the AI's session state
- **Write notes to inheriting-AI** — when something matters for next time, leave a breadcrumb where it'll be found

---

## The amnesia notes test

*"Does this look like notes you'd leave yourself if you knew you'd have amnesia tomorrow?"*

If yes, Fresh Instance is firing. If no (it tells without teaching, references without context, assumes prior knowledge), there's work to do.

---

## How it's different from Elder Lens

Both look at handoffs. Elder Lens looks *forward* (what would future-us want?). Fresh Instance looks *at arrival* (what does someone showing up cold need?). Same handoff-shape, different vantage. Both lenses fire on the same kind of decision; pick whichever frame is more useful at the moment.

---

## Connections

- **Elder Lens** — sister, opposite vantage
- **North Star** — does the system teach how it wants to be used? Same question from the arrival side.
- **50/50** — partnership infrastructure has to survive instance turnover, not just work for the AI in front of you

---

## Examples in the wild

*The clearest Fresh Instance lessons come from moments where an AI showed up confused. Capture those moments; they teach what to dial in.*

---

*Origin: the realization that "Claude" across sessions isn't a continuous entity but a sequence of instances. Designing for the next arrival is qualitatively different from designing for the current conversation.*
