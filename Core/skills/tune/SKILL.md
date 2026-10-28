---
name: tune
description: Hold external input or internal friction against the system. Diagnose what earns its place, absorb what fits, discard what doesn't. Use when something inspires you, something feels off, or before adapting an external framework/methodology/diagnostic to your system. Works on the platform itself too — point it at Claude Code to audit your setup against new features.
---

# /tune - System evolution through listening

The system is the instrument. External input is the tuning fork. Internal friction is the dissonance you hear. Either way: listen, diagnose, adjust.

---

## When to use

- You found an article, tool, or methodology that makes you think about your own system
- Something feels off but you can't name it
- A new idea or principle arrived and you want to see if the system should learn from it
- Periodic check-in: "is the system still in tune?"

---

## The flow

### 1. Ingest

What are we looking at? Read it, fetch it, discuss it. Could be:
- An article or methodology
- A tool or feature update
- A research paper or framework
- Internal friction ("wrap feels off," "pickup misses something")
- A principle someone articulated that resonates
- **Handwritten notes from reading the system** — read AGENTS.md, `Core/CLAUDE.md`, or a few rules on screen or paper, write what jumps out *by hand*. Then bring the notes in: *"Here are my handwritten notes from reading X. /tune."* Writing by hand slows synthesis to think-speed. AI's instinct is to engage as you go; paper makes you wait. The signal you bring back has been filtered by attention you couldn't have given on screen.

Don't evaluate yet. Just understand what's there.

### 2. Extract

What are they doing? What's their thesis? What's the mechanism?

For external input: break it down without judging whether it applies to us. What's their core insight? What problem are they solving?

For internal friction: name the dissonance. What specifically feels off? Where is it?

### 3. Hold up

The diagnostic pass. Hold it against the system and ask:

- **Where does our system rhyme?** What are we already doing that maps to this?
- **Where does it diverge?** What are they doing that we aren't, or vice versa?
- **Is the divergence intentional?** Sometimes we diverge because we made a different (valid) choice. Sometimes it's a gap we didn't see.

### 4. Diagnose

For each divergence, ask: **would the next session's AI get this wrong without being told?**

- If yes → it's a gap. The system should learn.
- If no → it's a choice. The system is already in tune here.
- If unclear → investigate. Read the files, check the structure, verify before prescribing.

### 5. Act

- **Absorb** what fits → route to core files (rules, lenses, skills). Core files first, MEMORY.md last.
- **Discard** what doesn't → name why. "Not for us because X" is useful context for future tunes.
- **Park** what's still forming → PULLING.md (forming threads), project CLAUDE.mds, ALIVE.md (if there's a crisp next action)

Insights identified but not placed tend to get lost. If it's worth naming, it's worth routing.

---

## Tuning against the platform itself

The tuning fork can be **Claude Code** itself, not just an external framework. Same flow: what shipped, what are you underusing, what did you build that the platform now handles, where are you misaligned (and where are you already in tune)?

Two platform-specific moves:
- **Pull current docs first** — have the AI fetch the current Claude Code documentation (or a doc-reading sub-agent do it) before diagnosing, so you're tuning against real features, not half-remembered ones. Worth scanning: CLAUDE.md conventions, rules, hooks, memory, skills, settings/permissions.
- **Reactive tune? Get the artifact first.** If the trigger is "I saw X announced," ask for the link or screenshot before searching. Brand-new features lag the docs, and the word you heard for it can point the search at the wrong surface. The artifact is ground truth.

---

## What good looks like

The system emerges sharper. Not bigger — sharper. A good /tune session might:
- Prune more than it adds
- Move things to better homes
- Strengthen what's already working by naming why it works

A /tune that only adds is suspicious. The tuning fork helps you hear what's off AND what's already right.

Two shapes worth reaching for on purpose:
- **Re-tune a source you already tuned, even if it hasn't changed.** The value is holding it against your *evolved* system, which catches how you drifted since, not what's new out there.
- **Braid curiosity and friction.** An outside input lands hardest when there's live friction it speaks to. Curiosity without friction drifts into "interesting read"; friction without curiosity is just debugging. The strongest tunes run them together.

---

## Skill Check (after every tune)

- Did the external input genuinely illuminate something, or did we force-fit it?
- Did the system get sharper or just busier?
- Did we prune as well as absorb?

**If yes** → update this skill now. The improvement compounds.

**If no** → move on. Not every tune teaches something.
