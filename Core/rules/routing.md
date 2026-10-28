# Routing — route the important to load-bearing surfaces

When something important lands mid-session (a recognition, a principle, a model that clicks, a sharpening), route it to a load-bearing surface (a CLAUDE.md, a rule, ALIVE, VISION) right then. Session logs hold everything by design, which is exactly why they can't be the load-bearing surface for important things: too much to filter, effectively unsearchable. **A thing you said isn't load-bearing until it's on a surface future-you actually reads.**

---

## Why this rule exists

Session logs are raw capture (they hold everything, including the unimportant). Future-you doesn't grep session logs for "what was that principle we landed?" Future-you reads CLAUDE.mds, ALIVE, VISION, rules. When a recognition lands and you don't route it, it's in the substrate but effectively lost. **Re-explaining the same thing in a future session is the tell.**

Substrate that holds everything = substrate that surfaces nothing. Routing TO a load-bearing surface is what compounds.

---

## When this rule fires

The clearest diagnostic: **re-explaining**. You notice you're recapping context to the AI that should have been ambient: a prior decision, a named frame, a principle you already articulated.

**Direction matters.** Re-explaining flows human → AI almost always. The AI's job is to *watch* for it (noticing when the human is recapping established context), but the *catch* lives in the human's felt experience, because of the continuity asymmetry: the human carries context between sessions and the AI doesn't.

**Nuance**: not all re-explanation is failure. Thinking-out-loud before something has crystallized is partnership work, because you organize your own thinking by saying it. The failure mode is specifically **re-explaining something that should already be on a load-bearing surface**. Quick test: *"if I closed this session and opened a fresh one tomorrow, would I have to explain this AGAIN?"* If yes → it's a routing target. If the shape is still forming → keep talking, codify when it lands.

---

## How to apply

When something important lands mid-session, route it. The home depends on its shape:

- **System-shape principle** (how you work, always-on) → `Core/rules/`
- **Operational frame** (cross-cutting current work) → `PULLING.md` if it's a live thread, or the owning task doc's `NOW · DECIDED · OPEN` block; `ALIVE.md` holds only the name and a pointer
- **Quarterly orientation** → `VISION.md`
- **Project/folder-scoped** → the relevant `CLAUDE.md`
- **Reference depth** → the depth clusters (`Core/foundations/`, `Core/lenses/`, `Core/practice/`, `Core/mechanics/`)

**Before creating a *new* home, check one doesn't already exist.** Routing-by-shape lands you on a *kind* of surface (a CLAUDE.md, a depth doc), but "folder-scoped → relevant CLAUDE.md" can quietly become "...so I'll make a new doc," skipping the question of whether an existing surface already does that job. Run `Core/rules/files.md` § Check before creating at that moment.

The test: *"if I closed this session and a fresh AI (or a fresh me) opened tomorrow, would this fire when it needs to?"* If not, route.

**Route-as-you-recognize, don't wait for `/wrap`.** /wrap is the backstop that catches what slipped through, not the primary routing surface. Hot-context routing is cheaper than cold-context recovery.

**Working-knowledge parks in its owning task doc, not in `PULLING.md` and not in a throwaway side doc.** When session work produces *continuation-knowledge* (state, maps, reasoning a future session needs to resume), it belongs in the relevant **task doc**, a holding surface. `PULLING.md` is a pointing surface for cross-cutting live threads with no single task home, and a side doc splits the knowledge from its task. **The discriminator is function, not intent:** scratch that gets *drained within the session* (a grep dump, a staging buffer) is fine; anything *retrieved across sessions* goes to the task doc. **The tell that scratch is secretly working-knowledge: you catch yourself writing a "resume here" section in a "delete when done" doc.** The self-deleting frame mis-predicted its own lifespan; it's a task doc in disguise, so make it one.

---

## Leave a back-pointer

When you route something from where it lived to its new home, leave a one-line back-pointer in the source noting where it landed. The shape, in the source:

> *→ Routed to `path/to/destination.md` § Section. [Brief why, if non-obvious]*

Without the back-pointer, the source becomes a one-way fork, and future-you has no way to find where the content went. Two-way pointer, no doc-level duplication: the source points, the destination holds.

**Skip when**: the routing is between scratchpad-shape surfaces, where a back-pointer would add more noise than navigation. The default is to leave one.

---

## Leave a *forward-useful* pointer, not a backward-only breadcrumb

The back-pointer above is forward-useful, since it tells future-you *where the content went*. Its evil twin is the **resolution-breadcrumb**: a "RESOLVED" / "moved here" / "(done)" note left in a **forward-state or scratchpad surface**, recording only *that something happened* with no forward use. Drop those.

**The discriminator**: does the note serve *forward navigation*, or only *record history*?

| Keep — forward-useful | Drop — backward-only |
|---|---|
| "X now lives at `path`" — where it went | "X resolved" — that it happened |
| a back-pointer that aids the next reader | a tombstone on a thread that's no longer live |

**Forward-state + scratchpad surfaces this fires on**: `ALIVE.md`, `PULLING.md`, `COMMS.md` / `SCRATCHPAD.md`, `CLAUDE.md` files (orientation = what's here NOW). When something resolves, these reflect the **new state** and don't accumulate a change-log. A resolved item *leaves* a forward surface (prune it); it doesn't earn a tombstone. The change-record belongs on a history surface (THREADS, session capture), not the forward surface you just acted on.

**The tell is the update-in-place reflex**: when something's done, the instinct is to *mark* it done; the move is to *remove* it. Done-ness is carried by the structure (the file now exists, or the item's just gone) plus the history surfaces.

**Clean stale data the moment you find it. Encountering it IS the drain trigger** (don't wait for `/wrap`). Retrieving something stale on a forward surface (a status that's now false, a path that moved, a thread that resolved) is itself the signal to fix it *then*; it's cheapest while context is hot. Two guards: (1) **scope by surface-job**: drain on forward surfaces, but **leave stale-but-once-true on history surfaces** (sessions, THREADS), where rewriting falsifies the record; (2) **verify before deleting**: cheap-check it's actually stale, not a record you're misreading.

---

## When NOT to apply

- Recognition is ephemeral / single-conversation (not load-bearing forward)
- Already captured in load-bearing form elsewhere
- Pre-codification territory — the recognition is still forming; capture it in the session, route once it crystallizes

---

## Sister rules

- `Core/rules/pointing-vs-holding.md` — the parent discipline (source = pointer; destination = content; the back-pointer keeps the pointer-surface job intact after routing)
- `Core/rules/files.md` § Check before creating — the destination gate: routing names *where by shape*, Check-Before-Creating asks *does that home already exist* before minting a new one
- `Core/rules/retrieval.md` — the inverse move: routing puts the important onto findable surfaces; retrieval finds it again when a topic surfaces
