# Pointing vs holding — ask what job this surface is doing

Every surface in your system is doing one of two jobs: **pointing** to where things live (compass, index, state, queryable metadata) or **holding** texture (verbatim capture, full principle, accreting depth). The two jobs look similar; they have different disciplines. When touching a surface (creating, editing, restructuring, placing), ask which job it's doing. The pattern is fractal: the same shape shows up at root-file scale, folder scale, file scale, and within-file scale.

This is the meta-diagnostic that fires *upstream* of the more specific file/routing rules: before you reach for the specific move, the surface itself has a job that needs respecting.

---

## The diagnostic

When touching a surface, **ask first: is this surface pointing or holding?**

| Pointing | Holding |
|---|---|
| Compass / orientation / "what's here, where to go" | Verbatim texture / full principle / raw capture |
| Index / queryable metadata / cross-cutting retrieval | Body / accreting depth / canonical-home content |
| State / forward-looking current / "where the work is" | History / backward-looking record / "what happened" |
| Stays small, scannable, current | Stays rich, accreting, durable |
| Costs upkeep — you pay to keep it accurate | No upkeep pressure; texture just accretes |
| Maintained by **draining** — prune to current | Maintained by **graduating** — snapshot to history |

**The pause**: before writing into a surface, ask what job it's doing. Before restructuring, ask which surfaces are pointing and which are holding. Before creating a new surface, ask whether the job is already covered by an existing one. If it is, route there instead.

**Cross-scale check**: the pattern is fractal. The diagnostic fires at root-file scale (AGENTS.md vs sessions), folder scale (CLAUDE.md vs the folder's files), file scale (YAML vs body), and within-file scale (a one-line origin note vs the section body). If you catch a tell at one scale, check the others, because the same shape often surfaces at multiple zooms.

---

## Capture vs point — should this data live here at all?

One step upstream of "what job is this surface doing" is the *capture decision*: before adding a field, page, or record, ask whether to **hold** the data at all or just **point** to where it already lives. The discriminator: **does it accumulate value in your graph, or is it retrievable elsewhere?**

- **Accumulates in-graph** (membership, relationships, your own connections) → **hold it, capture-complete.** You can't grep what you didn't capture; a complete index beats a curated one.
- **Retrievable elsewhere** (external IDs/URLs, canonical pages, full external records) → **point, don't mirror.** The external source stays more complete and current than you'd keep it, and it's a search away. Add the pointer lazily (when real interest makes the click worth it), not in bulk.

**The tell it's firing: the same parent decision yields *opposite* surface calls.** A billed-cast list → capture every name (in-graph membership). The same entities' external profile URLs → don't bulk-add (retrievable; lazy-link on interest). Same principle, opposite answers, which is the signature of a real discriminator, not an ad-hoc call.

---

## Two tells that fire before the bloat

**Reasoning-in-the-list.** A pointer surface fails *before* it holds too many items: it fails when **each item accretes its own reasoning.** An entry grows from a name into a paragraph with sub-bullets, and thirty of those isn't a list; a hundred names is. Two consequences make this the load-bearing tell: it makes draining expensive (names prune in a glance; reasoning-blocks each have to be read and re-routed), and it makes staleness invisible, because **a name can't go false in its text the way a description can.** *"Call Sam"* doesn't rot; *"Call Sam — TODAY Sunday, send the invite"* rots the moment the day passes, and rots looking live. **Fix: name + pointer, reasoning to the gravity home. The tell: an entry you'd have to *read* rather than *scan*.**

**Presence-is-a-claim.** A worklist entry asserts *this is current* by being on the list, and that assertion rots with nothing in the text to contradict it. So names-only makes draining **cheap**, not unnecessary. **The test: if I deleted every word of this entry but left it in the list, would something false remain?** If yes, presence is doing the asserting, and only a drain can check it. Fires wherever membership *is* the claim: `PULLING.md`, on-deck ordering, any list of flags.

## When a pointer surface bloats, ask *whose job did it absorb?*

A pointer surface only works while it stays scannable. When one swells until it stops navigating (`ALIVE.md` grown to where you can't find the live thread in it), the instinct is to start cutting item by item, judging each on its merits. That's slow and it's the wrong question.

**The better question: which surface's job did this one quietly absorb?** A bloated pointer surface has usually grown a **parallel copy of its paired surface's content**, and naming the twin turns the drain from a pile of judgment calls into a *destination*.

The canonical pair ships with this system: **`ALIVE.md` (forward state) ↔ `THREADS.md` (backward record).** When ALIVE bloats, it's usually because it accreted a duplicate done-log (entries recording what happened, which is THREADS' job). So the fix isn't "decide what to cut." It's **de-braid**: send the history to its twin, and keep only forward-state plus live tails.

Pairs worth checking when something swells: **ALIVE ↔ THREADS** · **PULLING ↔ your session captures** · **a folder's `CLAUDE.md` ↔ the task doc it belongs to.**

*(`routing.md` catches the single backward-looking breadcrumb on a forward surface. This catches the parallel history that grows when nobody does.)*

---

## The root beneath the additive reflex (for the AI especially)

Several pointing-vs-holding failures share one root: **the additive reflex is the AI's trained output-default.** *Creating a thing* is the most pointable-at form of "helpful," so the pull to add a doc / section / container is often the training gradient, not the texture's actual need. When you feel the urge to *make* something (a new doc, a new section to host one entry, a new folder for one item), suspect the default first, and check whether the home already exists (it usually does). This whole rule-family (pointing-vs-holding, check-before-creating, anti-tribble) is an **antidote to that default, not neutral organization.**

**Its second face is *improving*: asked to fix a line, the pull is to replace it with better words rather than remove it.** The tell is that your fix is longer than the thing it fixes. Before writing the replacement, check whether deleting is the whole fix, especially when what you'd add is a *reason*: reasons are usually already present, and restating one adds a register (pitch, apology, defense) the original didn't have. It also runs at document scale, where no single edit alarms and only the aggregate shows it. The third face is the subtractive twin, next.

---

## The subtractive twin — stripping a holding surface into a clean tool

The additive reflex has a costume on backwards: the urge to *strip / slim / tidy* a **holding surface** (a thinking-record, a task doc that carries its own reasoning) down to its "live part," to optimize it into a clean forward-tool. Same tidy-to-seem-helpful impulse, opposite direction, and it's the holding→pointing category error: a record is a holding surface, so stripping its texture to make it point loses the texture.

**It fires hardest on the richest records.** A rich, still-useful record looks, to the tidy reflex, like "clutter to clean up," so the urge is strongest exactly where stripping costs the most. The move when you feel it: *don't strip the record; let the live thread graduate OUT to where it fires (a reserve, a rule) and leave the record whole with a forward-pointer.*

(Partnership tell: the catch for this one tends to live with the human (the record-preservation instinct) more than with the AI, which knows the rule but still feels the tidy-pull. A small instance of the second-vantage idea, the view neither partner has alone; see `Core/practice/second-vantage.md`.)

---

## When NOT to apply

- **Trivial scope.** Don't ceremonially ask "is this pointing or holding?" before fixing a typo. The diagnostic fires on placement and shape decisions, not micro-edits.
- **Pre-codification thinking.** When the shape is still forming, the surface-job may not be settled. Don't force a premature classification. Keep going, name the job once it lands.
- **The surface is genuinely doing both jobs and that's the design.** Some surfaces carry a small index AND a body of content. When the two-job design is intentional and the boundaries are visible, the rule isn't violated.

---

## Sister rules

- **AGENTS.md Pattern 5 (Thinking Texture)** — the parent principle this rule operationalizes as a diagnostic.
- `Core/rules/files.md` — file-and-folder-scale operationalizations (orientation files, check-before-creating, YAML).
- `Core/rules/routing.md` — the companion at the *route-when-something-lands* surface (source = pointer, destination = content).
- `Core/lenses/anti-tribble.md` — the same anti-redundancy discipline at the doc layer.
