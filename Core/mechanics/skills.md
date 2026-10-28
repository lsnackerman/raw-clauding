# Skills

*How you write a skill, what makes its self-improvement check earn its place, and why you wait before codifying one at all.*

A skill is a codified workflow, a repeatable thing you do (`/wrap`, `/pickup`, `/gut`), packaged with its steps so you never re-explain it. This doc is the plumbing: how to create one, how to design its Skill Check, and the discipline of *not* creating one too soon.

---

## Creating a skill

A skill lives at `Core/skills/{name}/SKILL.md` and gets symlinked to `.claude/skills/{name}` so Claude Code can discover it as a slash command. Skills are flat, one folder per skill, no nesting. **Place a skill where you'd reach for it.** The name you'd invoke it by is the name it should have.

Every skill opens with YAML frontmatter:

```yaml
---
name: lowercase
description: One line — when to use this skill (this is what enables Claude Code's auto-invoke)
argument-hint: [optional — what to pass when invoking]
---
```

The `description` is doing real work: it's the routing logic. When you (or the AI) reach for a skill, the description is what gets matched against the moment. Sharpen it until it names *what makes this skill the right answer to a specific question*, because two skills with overlapping descriptions will collide.

**Don't create symlinks manually.** The `ensure-symlinks.sh` hook picks up a new skill **on the write itself**. It runs after every Write/Edit as well as at session start, so the slash command is available in the session you wrote it. Just write the `SKILL.md`; the plumbing handles the rest. *(A rename is a `mv`, which doesn't trip the edit-hook, so after renaming, run `bash Core/scripts/ensure-symlinks.sh --check`.)* See `Core/scripts/ensure-symlinks.sh`.

When you want to share a skill outward, give it a `/universal` pass first. Strip anything personal to your setup so it stands on its own for whoever receives it.

---

## Placement & naming

Skills are flat, so the work shifts from *where does it go?* to *do its name and description route correctly?* The description half is above; two more:

- **Reach-name it.** Name it for the moment you reach for it, in the words you'd use *before* you know your system's jargon (`/wrap`, `/pickup`, `/gut`). A fresh instance should land oriented from the name alone. Flat makes this, and the description, more load-bearing: there's no cluster to pre-disambiguate, so name and description are the only routing signal.
- **One skill, one job.** A skill doing two jobs is a smell; split it first.

**Why flat, not clustered.** A cluster folder inside `Core/skills/` shows whoever opens it skills-inside-skills, your architecture leaking into their experience. And at a few dozen well-named skills, the name already does the orienting a cluster would. Clusters earn their keep only when the set grows large enough that names alone stop orienting.

**Every restructure has a long tail.** The hook handles the symlink layer (`.claude/skills/`), but narrative references to a skill's path (in your notes, task docs, compasses, anything you've shared) don't update themselves. Grep the old path and fix the live references in the same session. Session files are a record of what was true then, so leave those.

---

## Skill Check design

Every skill ends with a **Skill Check**, a short set of questions that surface friction from the run you just did, so the skill improves through use rather than going stale. The pattern is: ask the felt questions, then "if yes → update now." The questions help you notice WHERE something was off; the fix is usually obvious once you feel the friction.

The strongest skill-check questions are **felt questions**, which ask about the texture of the run, not whether it technically worked:

- **/wrap**: "Did the compound scan surface real patterns or feel forced?" — a felt question
- **/floor**: "Did the space feel genuinely open, or performative?" — an authenticity check
- **/pickup**: "Did your partner have to re-explain something that should've been in the files?" — a partnership signal
- **/gut**: "Was a lens missing that would have helped?" — asks for skill improvement naturally, not prescriptively
- **/add**: "Schema missing a field you wished you had?" — immediate and practical

Questions that **don't** earn their place: ones that just confirm it worked ("did the check reveal a mismatch?") or are too vague to act on ("did anything surprise you?").

**Reach for resonance, not coverage.** The instinct is to cover all angles: extraction quality, naming, failure modes, every future case. But three felt questions beat five thorough ones. If a question doesn't surface friction you can act on, it's padding.

### A worked example — how a skill check evolves

Skill checks improve through use, like everything else. One skill started with three questions and ended with three, but different ones:

Draft:
1. "Did the clean record land in the right place, or did you have to think about where it goes?" — specific and mechanical
2. "Did archiving the file feel like closure or busywork?" — questions the skill's existence, not its improvement
3. "Is there a medium missing from the routing table?" — practical but narrow

Final:
1. "Did any part of this feel clunky or unclear?" — open; catches the routing friction #1 was after AND everything else
2. "Any gotchas the next-us should know about?" — elder lens, catches platform-specific learnings
3. "Anything missing from the flow that should be a step?" — how the skill grows from real usage

What changed: #1 absorbed the old #1 (routing friction is a specific case of "clunky"). Old #2 got cut (questioning whether the step should exist isn't surfacing how to improve it). Old #3 widened from "missing medium" to "missing step" (broader, still actionable). The lesson: a skill check that asks felt, open, actionable questions outperforms one that tries to enumerate every angle.

---

## Off-road by description before codifying

The reflex when something works is "that worked, codify it now." The discipline is the opposite: describe the shape in prose, let it prove itself by recurring, and codify only when it earns its place through use. This is the bitter lesson applied to your own infrastructure. Don't encode a rule the first time a pattern appears; let usage tell you what's actually load-bearing. (See `Core/lenses/bitter-lesson.md`.)

Three beats, before any new skill:

1. **Name the deliverable shape in prose.** When a one-off custom shape works for a specific moment, *describe* it ("a doc that captures what landed for the listener, with their reactions as evidence"). Don't elevate it to a skill yet. The single instance is still useful; it's good practice at extracting a shape. It just doesn't earn skill-infrastructure on its own.

2. **Watch for recurrence.** If a similar shape comes up again, that's signal the pattern might be real. One instance is an exercise; a recurrence is a candidate.

3. **Codify when the pattern earns its place.** When you recognize the prose-shape as repeatedly useful and worth elevating to infrastructure, the skill earns its frontmatter. **Judgment, not count.** The recognition is what matters, not a tally. You're not waiting for "three instances"; you're waiting until you genuinely see the shape as load-bearing.

Off-roading-by-description IS the bitter-lesson approach: prose-describe first, let the pattern prove itself, codify when it's clearly worth the infrastructure.

**Scope: this discipline is for *new skill infrastructure*, the high-cost end of codification.** It is not a universal gate on every note you write. A one-line mention in a folder's CLAUDE.md earns its place the moment it's useful (single instances are fine there); a small refinement to an existing rule earns its place when the refinement lands coherently. The wait-for-evidence discipline scales with the cost of being wrong: a new skill is expensive to create and maintain, so it waits for the pattern to prove itself; a compass note is cheap, so it doesn't. For the full picture of how codification gates by cost, see `Core/rules/codification.md`.

---

## Sister docs

- `Core/rules/codification.md` — how things become codified knowledge (rule-writing, when-to-codify, the cost-aware gating that the off-road discipline above is one end of)
- `Core/lenses/bitter-lesson.md` — patterns over rules; let existing structure carry what's load-bearing, don't encode prematurely
- `Core/scripts/ensure-symlinks.sh` — the hook that wires new skills into `.claude/skills/` for you
