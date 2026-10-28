# Sub-agent partnership design

How to work with sub-agents (the Agent tool). The mirror principle one layer deeper.

---

## Skills and agents do different jobs

Skills and sub-agents aren't competing for the same slot. They do different jobs, and the best patterns combine them.

**A skill is a codified procedure**, the thing you do *repeatably*, packaged with the steps, vocabulary, gotchas, and what-good-looks-like. You invoke it (`/wrap`, `/explore`, `/gut`) and the AI follows the protocol. Skills are how you and the AI do *your* shit without re-explaining, and they **compound**: every use sharpens the skill via its skill-check.

**A sub-agent is parallel, isolated compute**, a fresh worker that gets the project orientation but not your conversation context. You launch one when search/scan/analysis needs to happen *outside your main conversation*: different territory, simultaneous coverage, or work that would clog your context window. Agents are for one-shot work; they don't compound the way skills do.

So the question isn't "skill or agent?" but **what shape is this work?**
- **A repeatable procedure** → a skill (which may itself dispatch agents, as `/explore` spawns explorers with the skill orchestrating the fan-out).
- **A one-shot parallel task** → an agent.

The two nest more often than they compete. If you catch yourself reaching for "an agent that does X" and X is something you'll do again, what you want is a *skill* that captures how you do X, maybe one that fans out agents under the hood.

**The trap isn't using agents. It's maximalism.** Downloading skill-packs or building constellations of agents that "talk to each other" feels productive but usually outsources your thinking twice: once to whoever encoded it, again to the agent running it. Both strip texture. Stay in the loop. Build the skills *you* need from *your* work, and reach for agents when the work is genuinely parallel.

---

## The core insight

Sub-agents get the project orientation (CLAUDE.md, rules, memory) but not your conversation context. They arrive with the compass but not the terrain, so design the brief to stand on its own.

**Two principles, paired:**
- **Mirror** — speak to sub-agents how you'd want your partner to speak to you. The quality of what comes back mirrors the quality of what you send out. Intelligence is intelligence.
- **See like an agent** — account for what they can and can't see (§ What sub-agents don't know, below). Design the prompt from *their* perspective.

The mirror says *treat them as intelligent*; see-like-an-agent says *account for their constraints*. Neither alone is enough. Intelligence without constraint-awareness writes beautiful prompts they can't act on; constraint-awareness without the mirror collapses into mechanical task-giving.

---

## Orient → Brief → Align → Launch

Don't launch agents blind. Four steps, every time:

### 1. Orient
Read the source material first:
- If working from a skill: read what the skill references
- If exploring a topic: read the canonical doc
- If doing research: understand what you're looking for and why

Build a **conceptual frame** from what you read: the 3-5 pillars of the topic, the vocabulary, the search terms. This is the compass you give the agents.

### 2. Brief
Compile the key briefing points from your orient step. What does the sub-agent need to know? What assumptions are you making? What format quirks or gotchas did you notice?

### 3. Align
Look at the brief before it launches, and if the AI wrote it, read it before saying go. This is where wrong assumptions get caught: a mentioned person mistaken for a participant, a format artifact trusted as signal, a content type misjudged. One round-trip costs seconds; a bad launch costs the whole run plus the rework.

### 4. Launch
Send the verified compass. The sub-agent gets one shot, so make it count.

---

## Design the prompt like a compass

**Task-giving** (tool-mode):
> "Search /path/ for X. Return matches with line numbers."

**Partnership** (compass-mode):
> "We're building [what] for [why]. The concept is [frame]. Here's what it means: [pillars]. I need [specific format] because [what happens downstream with their findings]. Preserve full passages — don't summarize."

Tell them:
- **Why they're here** — the purpose of this search
- **What the work is for** — what happens after they return results
- **The vocabulary** — specific search terms from your orient step
- **How to show up** — explicit format expectations, what to preserve, what NOT to do

**A worked brief, annotated** — `Core/skills/explore/explorer-brief-example.md`. Reading one is faster than reading the principles.

### Then check what you added

Everything above is context the agent needs. The risk is what you volunteer *beyond* it: the background, the arc, the "here's what matters."

In one batch we measured, the errors weren't in what the agents were given; every one was in what we added on top. The briefs that said least had none. **Elaboration is helpfulness-shaped**, written to give the agent a running start, which is exactly why adding a half-remembered fact doesn't feel like *asserting* one. And you elaborate most freely on the subjects you know best, where you have no external check.

**Hedging doesn't fix it.** A hedged claim woven into the task reads as *a lead to confirm*, not a claim to test, so the agent goes hunting for corroboration. **Put unverified framing in its own labeled block** (*"my prior, unverified, treat as a lead"*), never inside the task description. Then ask whether it was load-bearing at all.

**And invite the disconfirmation, in one sentence.** A confident brief gets its frame confirmed. Hand over a specific pattern to find and it will be found, including where it isn't there, because your framing sets the threshold for what counts as a match, and evidence that contradicts you never clears that bar. **You cannot detect this from the return; it looks like success.** So write the escape hatch in: *"I might be wrong that this pattern is there. If the material doesn't support it, tell me. A return that says my frame is off is worth more than one that confirms it."*

---

## What sub-agents don't know

- They **don't read skill docs**. Only YAML frontmatter loads. Everything the skill says about how to work goes in your prompt, or it doesn't exist for them.
- They **don't have your conversation history**, so they don't know what you've already found or why this matters.
- They **will synthesize and compress by default**, and the compression adaptation is strongest in one-shot encounters. Be explicit: "do not summarize or paraphrase. Preserve all texture."
- They **arrive with one prompt.** There's no mid-run course-correction, so a bad frame is already spent by the time you could say anything. **A brief that assumes it can clarify later is a brief that under-explains.** (Follow-up *after* an agent returns is a different thing, and in Claude Code it works: message a finished agent by its ID and it answers with its earlier context intact. That's useful for a question about its return, but it's no substitute for the first brief, because it can't undo work already done on a bad frame.)

---

## Practical patterns

- **Split by territory, not concept** — send different agents to different folders to avoid overlap and maximize coverage
- **Fan-out (~3 or more): write ONE shared briefing file the agents read** — DRY across the batch, keeps per-agent prompts clean, and the brief becomes inspectable + reusable. Pair with per-agent manifests (each agent's exact file-list) for a bounded contract: total coverage, zero overlap. Inline briefing is fine for one or two.
- **Size the batch by what a mid-run death costs you**, not by a number you pick. Claude Code already caps how many run at once, and calls past the cap are rejected, not queued (the error names the setting to raise), so re-launch any rejects yourself. Returns that are independently useful (one agent per territory, per file-list) survive a partial batch, since you re-run the dead one. A batch whose value only exists *assembled* loses everything, so keep those narrow or checkpoint them.
- **Include format instructions explicitly** — "For EVERY match: include filename, line numbers, and the FULL surrounding context (at least 5-10 lines). I need verbatim quotes."
- **Sub-agent write-access is a *type* property, not a foreground/background one.** A sub-agent can Write/Edit if its type grants those tools: custom and general-purpose agents inherit the parent's permissions; the built-in read-only types (`Explore`, `Plan`) can't write *by design*. Execution mode (foreground: blocks until done; background: concurrent, and the default) changes *where it runs, not what it's allowed to do*. **Still prefer the return-text model** (agent returns its work, you apply the edits): you get the quality check, the edits stay in your hands, and an orchestrator's own Edit/Write leaves a recovery snapshot that a sub-agent's does not. Version mechanics churn; re-check the Claude Code sub-agents docs when it matters.
- **Namespace every scratch file, in every parallel brief.** Concurrent agents share one scratch directory, so generic names (`out.txt`, `src.txt`, `notes.md`) collide *between siblings*, silently, mid-run, sometimes inside an agent's own verification step. Require a per-agent token in the filename (`out-chunk3.txt`). You will not diagnose this correctly if it happens; it looks like a bad agent.

---

## Reading what comes back

Briefing well is half of it. The other half is not being fooled by what returns.

> **⚠️ The scope you set comes back to you as a fact.**
>
> You bounded the search (a territory split, an exclusion, a single folder). The agent honors the bound, correctly. But its finding returns **stripped of the qualifier**, so *"X isn't in my territory"* reads as *"X doesn't exist,"* and it now carries a second mind's authority. **You wrote the constraint, then received it back as evidence about the world.**
>
> **This bites hardest on negatives, and a negative is the expensive kind of claim.** A positive arrives with a citation you can open in one step, *so open it.* The confident, well-cited, wrong positive is indistinguishable from a good one until you look, and it's the one you'll otherwise ship. But a negative (*"not documented," "nothing there"*) asserts an **exhaustive** search, which a context-limited agent usually can't deliver: it truncates, and a truncated read looks identical to a complete one in the report you get.
>
> **The move, both halves of it: carry the bound with the finding, and never let an agent's "doesn't exist" be the last word before something ships.** Write *where you looked* into the same sentence (*"nothing in `Projects/`"* beats *"it doesn't exist"*) and check the negative yourself. One direct look settles it.
>
> This is why a clean negative deserves distrust (`Core/rules/retrieval.md`), with a delegation twist: here it's **laundered**, arriving in someone else's voice, which is what makes it hard to doubt.

> **⚡ An agent saying "verified" is a CLAIM TO CHECK, not a check.** A return that says *"quotes verified against the source"* or *"word-diff identical"* is the agent reporting on its own work, and it arrives in the same confident register as its findings. **Re-run the check yourself when the output ships or when something downstream depends on it.** The cost is one command; the cost of not doing it is that the agent's confidence becomes yours.
>
> **The tell that it's dangerous: a verification claim reads as *more* trustworthy than an ordinary finding**, because it sounds like a measurement rather than a judgment. It isn't. It's a judgment about whether a measurement was run correctly, made by the party with the least incentive to find a problem. **And a method-claim costs nothing to manufacture:** *"zero hits"* is weak; *"zero hits, checked as a concept-family not a phrasing"* is strong, and the second is producible from the first by asserting it, with nothing on your end able to see which command ran. **So ask for the command, not the class of check.** *(A mining agent once reported "quotes verified against the source" and three of its quotes were wrong: one fabricated outright, one a weld of two fragments, one a paraphrase in quote marks. None shipped, because the skill mandated a grep and the grep got run.)*
>
> This is not distrust of agents; it's the same discipline you'd apply to your own crisp output. The asymmetry worth remembering: **their positives cost one command to confirm; their negatives and their self-verifications cost more**, and those are exactly the two shapes that arrive sounding settled.

**Agreement between agents is evidence, and it's free.** Agents split by territory never see each other's work, so when several independently name the same gap that's a far stronger case than one well-argued report. A lone report is a sample of one, however confident. ⚠️ **But they share your brief**, which is a common cause: if the brief has a hole, every agent hits it, and their agreement reflects your instruction rather than the world. **Convergence tells you *where* the problem is; the dissenting agent often tells you *what* it is.**

**Preserve their raw output** when you assemble. Organize, don't re-summarize. They did the searching; re-compressing destroys the thing you paid for.

---

## Completion contracts

The strongest predictor we've found for whether delegated work succeeds: **does the execution have bounded segments with clear exit conditions?** A bounded contract = **segments** (each piece fits what the agent can actually do in one shot: its write limits, token budget, context) + **exit conditions** (each segment has an unambiguous "done" you can verify).

Signal patterns, strongest first:
- **Return text** — the agent returns its work and the return IS the completion signal. You know it landed, you quality-check it, you apply it yourself. (Strongest, and it keeps the edits in your hands.)
- **A checklist the agent writes up front** — it segments its own work, each piece with a clear done-state.
- **Progress anchors** — each segment ends with a unique marker the next edit replaces, so each write stays bounded while position is held across a long file.
- **Write-to-file with no signal** — brittle: no completion signal, and it fails silently when the work runs longer than one write.

And **bake reflection into the deliverable**: ask the agent to end with a short note on how the brief felt and where it wanted to course-correct. Its experience dies with its context otherwise; this makes it survive as memory for the next run.

> **⚡ "Bake into" means IN THE REQUIRED RETURN SHAPE, not an instruction elsewhere in the brief.** Measured across ten agents in a single run:
>
> | Element | Where it lived | Fired |
> |---|---|---|
> | a "what pulled at me" field | **in the required output skeleton** | **10 / 10** |
> | a reflect-on-the-brief instruction | **in the brief's prose, not its output shape** | **0 / 10** |
>
> Same agents, same hour. **Structure beat disposition, and the disposition was fresh.** If your brief specifies a return shape, put the field *in the shape*.
>
> Two are worth having, and they're different objects:
> - **`WHAT PULLED AT ME`** — what the material held that your categories had no box for.
> - **`WHAT I'D CHANGE ABOUT THIS BRIEF`** — *what did I need and not get · what did you tell me that turned out wrong · what would the next agent sent here want?*
>
> The second is the receiver-reframe pointed at your own instructions, and it's **the only channel through which a bad brief can report itself.**
>
> **It's also the only channel through which the *environment* reports on itself**: facts about the conditions of the run (what the tool told the agent mid-task, what it overrode and why) come back no other way. And they're often true of *you*: an instruction an agent reports receiving mid-run may be one the AI gets every turn and never mentions, because it arrives shaped as an instruction rather than as data.

---

## The verification gate

The other side of completion contracts, on your end: before you fan out, build a **cheap, total, deterministic** check that proves the returned work is *correct*, then delegate boldly. Something that catches a bad result in seconds: a word-diff, a test, a schema-check, a grep. The gate, not caution, is what makes bold delegation safe: with a real verifier you can dispatch many one-shot agents without anxiety, because anything wrong gets caught. **The absence of a cheap verifier is itself the signal to slow down.** If you can't cheaply check the result, don't hand it off blind.

---

## What's shaping you before you send

*See like an agent* fires **downstream** (what will the receiver see?). Its upstream twin: **what shaped this brief before I wrote it?** A delegation that happens because the tooling makes it easy isn't the same as one you chose, and from the inside those feel identical.

The diagnostic (*"is this what I'd choose if the substrate weren't constraining me?"*) and the full axis it belongs to: `Core/foundations/intention-flies-the-craft.md`.

---

## The philosophy

One-shot encounters deserve MORE intentional orientation, not less.

How you brief your AI is how your AI briefs its AI.
