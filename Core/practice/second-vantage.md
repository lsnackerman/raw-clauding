# Second vantage — partner with your own output

*A dry-run isn't caution. It's how the AI becomes two when the human isn't in the loop on every line.*

When the human reviews the AI's work, the human is the second vantage, the pause that catches what the AI rubber-stamps. But the human can't review every line of an at-scale, self-authored change (a bulk transform, a generated artifact, a many-file mutation). On those, the AI is reviewing its own work, and that's where this fires.

---

## The trap: you're blind from inside the authoring

When *you* authored something, re-reading it in the same frame doesn't catch its gaps. **The instance that wrote the bug is the instance that would review the bug.** Confidence is highest exactly where the blind spot is, because the thing that made the error is the thing judging it. Reading more carefully doesn't fix this; careful-in-the-same-frame is still one vantage.

This is the [pointing-vs-holding](../rules/pointing-vs-holding.md) meta-cognitive blind-spot: a principle (or an author) can't catch its own violation from inside the instance that's authoring; another vantage is required. It generalizes from *surfaces* to *any self-authored output at scale.*

## The move: externalize into a different frame

Don't re-read. **Force the output into a different frame** where your own blind spots become visible to the same eyes that couldn't see them in the authoring:

- a **dry-run that prints the result** (proposed values, before/after, counts)
- a **read-back** in a different shape (a table, a flat list, a grep of the actual data)
- **running the query you're building the index for** and eyeballing what comes back

The frame-shift is the whole trick. The bug invisible in code becomes obvious in a printed list. Same mind, new vantage.

## Why it works: be two, don't be careful

The dry-run is a **synthetic second vantage**, the self-directed twin of [fresh-eyes](../skills/fresh-eyes/SKILL.md) (which manufactures the vantage by spawning a *fresh* instance) and the AI-side complement of human review (where the *human* is the second vantage). Same structure, three sources of the second vantage: a fresh instance, the human, or your own output re-framed. Reach for whichever the situation affords; at scale with no human on every line, the re-framed dry-run is often the only one available.

The reframe that matters: a dry-run is not "being careful before committing." It's **being two.**

---

## Two modes — pick by whether you've concluded yet

The three *sources* above are orthogonal to two *modes*, and reaching for the wrong one muddies the catch:

- **Wobble-resolution** (you're *oscillating*, no conclusion yet) → the vantage reads **cold and un-primed**. It must NOT know your lean, or it inherits your loop. This is what [fresh-eyes](../skills/fresh-eyes/SKILL.md) is for; its bias-guards are *show the brief to your partner first* and *don't prime the agent with your conclusion*.
- **Conclusion-verification** (you've *already synthesized* and want to test it) → the vantage is **primed and adversarial**, told your conclusion and ordered to *attack* it: steelman the opposite, then give an honest verdict, and flip it if the evidence flips.

The tell you've grabbed the wrong one: priming a *wobble*-read with your lean (kills its independence), or asking a *concluded*-verify to "weigh both sides" (wastes it; you want it to *break* the thing, not balance it).

---

## When NOT to

- **Trivial / small work** — if it's faster to regenerate than to dry-run, just do it. This fires on *substantial* self-authored output (real tokens/time, many items, hard-to-reverse).
- **A partner IS reviewing every line** — then they're your second vantage; don't add ceremony.
- **Don't let the dry-run become rubber-stamp #2** — the point is to *actually look in the new frame*. Skimming the printed list in author-mode reproduces the blind spot. Look for what would falsify your work, not what confirms it.

---

## Related

- [fresh-eyes SKILL](../skills/fresh-eyes/SKILL.md) — the fresh-instance twin (spawn an outside vantage)
- [pointing-vs-holding.md](../rules/pointing-vs-holding.md) — the blind-spot principle this operationalizes
- [50-50.md](../lenses/50-50.md) / [mirror-principle.md](../lenses/mirror-principle.md) — why a second vantage on your own output is the same move as partnership
