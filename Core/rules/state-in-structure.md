# State in structure, not in lists — the gap is the flag

Before creating a task, checklist, or tracker to *remember* something, ask whether the system's **structure** already encodes that state. If the absence, placement, or naming of a thing IS the signal, you don't need a separate list, and the separate list is worse, because lists drift and structure can't.

This is **architecture over configuration** (AGENTS.md Pattern 1) applied to task-tracking: let the structure hold the state instead of a list that narrates it.

---

## Why this rule exists

Lists need maintenance: you check the box, prune the done, and the moment you forget, the list lies. Structure maintains itself. A transcript with no "cleaned" companion file *cannot* misreport whether cleaning ran. The gap **is** the truth. State-in-list rots; state-in-structure is self-truthing.

Most personal systems die in a maintenance death-spiral: the trackers outnumber the work, drift out of sync, and become noise. You avoid that by encoding state structurally wherever you can. "No task needed" is a *correct* call when the architecture already holds the state, not a lazy one.

---

## The test

Before making a tracker, ask: **"If I did this work, would the structure change in a visible way?"**

- **Yes** → the structure is the tracker. Don't make a list. The change (a new file, a renamed file, an emptied folder, an added suffix) is the record.
- **No** → the work leaves no structural trace (a decision rationale, a future-dated reminder, multi-step work invisible to the filesystem). *Then* a task/list is the right tool.

The principle is *prefer structure when structure can hold it*, not *never make tasks*.

---

## What this looks like

- An **`_inbox/` trending toward zero** = the triage queue. The folder's contents *are* the to-do; no separate "things to process" list.
- **Folder presence/absence** = relationship or status state (a light contact is a flat file; an active one earns a folder).
- A **missing companion file** = pending work (a raw file with no processed counterpart = "needs processing"; a glob lists the whole backlog, and it can't lie).
- A **CLAUDE.md "Status" section that reads the filesystem** instead of hand-maintaining a checklist.

---

## Centrality is earned, not default

Everything above is the **state** layer: don't build a **list** when distributed **structure** already carries the state. There's a **location** layer of the same move: don't keep a **central** surface when distributed **gravity** already carries the location. Same parent (architecture over configuration), same skeleton: *don't centralize what distributes, with one earned exception.*

**The default is gravity.** Everything lives with its gravity, the project or domain it belongs to. A **central** surface (a top-level folder, a catch-all `_done/`, an `_inbox/`) is the *exception*, and it has to **earn** it.

**What earns it: a scan-all retrieval shape.** A central surface is legitimate only if you reach for *all of it at once*:
- **Worklist** — held whole *on purpose*, because you scan the whole thing to triage or pick what's next (an active task list you read to decide what to do).
- **Queue** — scanned whole to drain, trending toward zero (`_inbox/`: you sweep it to route, and empty is the goal).

**The tell it *hasn't* earned it:** a central surface that's **neither** worklist nor draining queue is **drift wearing a folder name**. Its contents each belong to a gravity; centrality is just where they piled up. A "misc" folder, a top-level `notes/` that everything falls into, a catch-all you add because you couldn't decide where something went.

**The test**, the moment you're about to create or keep a central surface: *"do I ever reach for all of this at once, to triage (worklist) or to drain (queue)?"* Yes → central is earned. No → it's gravity-distributable, and the centrality is drift.

**Worked example, because this one is genuinely arguable: `Tasks/_done/` in this system.** It's central, and it earns that, because you scan finished tasks *as a set* when you want the history of what you've worked through (see `Tasks/_done/CLAUDE.md`). **But watch it as your system grows.** Once you have several substantial projects, "what did I finish?" stops being one question and becomes *"what did I finish **on this project**"*, and at that point the same test says distribute it, one `_done/` per project. The surface doesn't change; the retrieval shape does. That's the discriminator doing real work rather than handing you a rule to memorize.

---

## Substantive vs performative

| Real structural state | Faux-structural (still a list) |
|---|---|
| Missing companion file = pending; the glob can't lie | A `TODO.md` — a list wearing structure's clothes |
| Empty `_inbox/` = nothing to triage | A "things to triage" doc that mirrors the folder |
| File moved = migration done | A checkbox saying "moved file" next to the file |

The test: does the structure change *as a byproduct of doing the work*? If yes, it's self-truthing. If the "structure" is a doc you have to remember to update, it's a list in disguise, and it'll drift.

---

## When NOT to apply

- **State with no structural correlate** — a rationale, a deadline with no file, coordination across people. Tasks/lists are right here.
- **Multi-step work where the steps aren't visible in the filesystem** — a task doc with a sequence is the tool; don't contort structure to fake it.
- **You're tempted to *invent* structure just to avoid a list** — forcing a naming scheme or folder split purely to encode a tracker is the inverse failure. Let structure carry state when it *already* does; don't bend it.

---

## Sister rules

- **AGENTS.md Pattern 1 (architecture over configuration)** — the parent principle; this is its task-tracking translation.
- `Core/rules/files.md` § Check before creating — the file-layer companion (don't create a redundant doc); this is the state-layer companion (don't create a redundant tracker).
- `Core/rules/routing.md` — the counterweight: routing puts important things *onto* central load-bearing surfaces; § Centrality is earned checks that such a surface actually earns its centrality (else the thing belongs in its gravity).
- `Core/rules/retrieval.md` § Build surfaces that fire — the parent idea (name the firing shape of every surface before you create it); worklist and queue, defined above, are the two *scan-all* shapes, the only ones that justify a central home.
- `Core/lenses/anti-tribble.md` — the same anti-redundancy discipline at the doc layer.
