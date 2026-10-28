# Retrieval — find what you already hold, and search so it surfaces

Once your system has been running a while, it captures richly (sessions, library, reserves, rules, lenses), and the bottleneck stops being capture and becomes **retrieval**: finding what you already hold when a topic surfaces, *and* searching in a way that what exists actually surfaces. This rule owns "find before you re-derive" and "search so the answer isn't buried."

*If you're just starting, this rule is mostly dormant, since there isn't much to find yet. It gets load-bearing around the time you first catch yourself re-explaining something you know you've already worked out.*

---

## Why this rule exists

**Substrate that holds everything surfaces nothing.** The richness that makes your system valuable (it has already named most things) is the same richness that lets the *distilled* answer get drowned by *raw* capture. A naive search over the whole tree returns the answer ranked beneath dozens of session-log hits, and if you stop reading at the first screen, you conclude "it doesn't exist" while looking right past it.

Three retrieval failure modes:

1. **Forgot to look** → re-derive from scratch. *(This rule owns it.)*
2. **Looked, but a naive search buried or truncated the answer** → a confident **false-negative** ("we don't have this"). This is the one that bites. *(This rule owns it.)*
3. **Found it, but didn't connect it** to the live thread → `partnership.md` § Surface resonance owns this.

The tell for the first two: **re-explaining or re-deriving something the system already named.**

---

## How to apply

### Retrieve before re-deriving
When a topic surfaces, check what you already hold *before* adding new thinking. Where to look, fastest-payoff first: the distilled clusters (`Core/rules/`, `Core/lenses/`, `Core/practice/`, `Core/foundations/`, `Core/mechanics/`), then `Core/reserves/` (raw concept-thinking), then sessions only as a last resort.

### Search so it surfaces — concrete moves
- **Distilled-first.** Grep the distilled clusters before (or instead of) the whole tree: `grep -rli X Core/rules Core/lenses Core/practice Core/foundations Core/mechanics`. The distilled doc is the answer; `Core/sessions/` is raw capture that will out-number and bury it.
- **Never `head`-truncate an existence check.** A `head -20` over a session-dominated result hides the distilled hit past the cap. For "does X exist," **count the hits and scope the search tight**. Don't eyeball the first screen of a broad grep.
  - **Same ban on a LOAD, not just a search. A partial read cannot support a claim about the whole.** When a skill says *load* a reference file (a lexicon, a schema, a convention doc), read it **whole** or **grep it for your specific terms**. Never read a prefix and then reason about what the rest contains. The phrase "existence check" is what lets the truncation feel legitimate (*I'm not checking existence, I'm loading*), so the ban reads as not-applicable at exactly the moment it applies.
- **Exclude raw capture when checking existence:** `--exclude-dir=sessions` (or just search the distilled clusters explicitly).
- **Distrust a clean negative.** A tidy "we don't have this" is *itself the tell*, the satisfying conclusion built on a shallow search. Re-search differently (synonyms, the distilled clusters, the filename) before concluding it's absent.
- **The produce-side twin is to distrust a crisp *novelty*.** The move above is the *search* side (you looked for X, found nothing → distrust it). The same principle fires on the *produce* side: **you made something crisp and it feels new → distrust *that*.** A satisfyingly-clean "new" insight is *more* suspect, not less, because crispness usually means the idea is *mature*, and mature ideas in a compounding system have often been thought before (the fluency that makes it feel novel is the same you'd feel *re-deriving* it). The reliable trigger is the **action**: the moment you reach to **create / route / codify a surface** as if it's new → the ambient ping-layer (`concepts.md`) surfaces the frame if your riff-vocabulary hits one of its triggers, and at the create-moment check what you already hold (`files.md` § Check before creating). Confidence carries no signal about its own accuracy, on the way *out* as much as the way *in*.
- **The shape-cousin is the same distrust firing on how a *tool* behaves.** The move above is about ideas you already hold. It also fires on claims about **how a tool or component behaves** (an external tool, or one of your own skills/hooks) when the claim comes from *reputation* instead of *reading*. The AI's confidence is flattest exactly here, at contact with the outside world, so it gives no warning. The tell: a behavioral claim sourced from what a thing is *for* rather than what it *does*. Open the component (or the tool's docs) before the claim lands. If it's a repeat catch, that's a `concepts.md` entry waiting to be born.
- **Person named → check `Library/people/` first.** When someone names a person, check your `Library/people/` pages (once `/add` has built some) before answering as if they're unknown, because a clean "I don't know them" is precisely the tell to search first. Your graph often holds not just *who* they are but a connection to your own work you'd otherwise miss.

---

## Reserves — the raw-concept retrieval surface

`Core/reserves/` holds raw concept-thinking that accretes across sessions (built by `/explore`, maintained at `/wrap`). Two moves are specific to it:

- **Scan at session start** (during `/pickup` / first orientation): glance the reserve names, a short list that loads them conceptually for the session.
- **When a topic surfaces**, is there a reserve for this? Obvious name-match → retrieve before deepening. Unclear → `grep -li {topic} Core/reserves/` (a one-second check). No match → continue; don't manufacture one preemptively (reserves accrete through use).

---

## Build surfaces that fire — the make-it-retrievable companion

Everything above is the *retrieve-in* side (find what you hold; search so it surfaces). The build-side companion: **when you create or touch a surface (folder, doc, section, tracker), name the retrieval shape that fires it**, the actual moment future-you arrives at it. Can't name it? It's a **collect-only surface**: it accretes and silently drifts. (That drift is the upstream *cause* of failure #2 above. The answer that's "buried" was often put somewhere nothing ever fires at.)

The discriminator: can you finish ***"future-us reaches this when ___"*** with a real moment? A few common firing shapes:

- **by presence** — auto-loaded trails (AGENTS.md, a folder's CLAUDE.md, an always-on rule); fires just by existing where you read.
- **by topic** — a reserve you grep when its subject comes up.
- **by skill** — a doc a `/command` reads when invoked.
- **by search** — findable via grep because it's named for the reach-moment.

If the blank won't fill with a real firing moment, give the surface a shape or don't create it. (Performative answers like *"it's reference material"* and *"it's important so people will find it"* are a label or a hope, not a firing moment.)

**The firing moment has to sit at the depth that auto-loads, while the description can live with the artifact.** A `CLAUDE.md` trail auto-loads *by presence*, which means it only reaches the levels you actually touch. So a **"use when ___"** trigger buried three folders deep fires for nobody: the shallow compass hands you an *inventory* ("`playbooks/` — run material"), while the *ping* ("**use this when planning the next session**") never reaches you. **The surface fires, but the trigger doesn't.**

**The move: push the firing-moment up to where things auto-load; leave the description down at the artifact.** The deep compass *holds*; the shallow one *fires*. A line phrased as a **moment** (*"designing a session → read X first, and assume it already exists"*) does what a folder-inventory line structurally cannot.

**The tell is counter-intuitive: an accurate compass that never fired looks exactly like a missing one.** The instinct is to go improve the map. But if the trail was already correct (check before rewriting), the defect is *depth*, not *content*, and rewriting the deep doc changes nothing.

**Exception**: fast-capture scratch (SCRATCHPAD, COMMS) is *drained, not retrieved*; "I dump here and route later" is its valid shape, not a violation.

`routing.md` puts content *onto* load-bearing surfaces; this ensures the surface itself *fires*.

---

## Substantive vs performative

| Substantive retrieval | Performative |
|---|---|
| Grep the distilled clusters, count the hits, open the distilled doc | Grep the whole tree, `head -20`, eyeball the session hits, conclude "not found" |
| "Clean negative — let me re-search by synonym/filename before I trust it" | "Nothing came up, so it's not in the system" (ships the false-negative) |
| Re-explaining myself → stop, this is probably already named, go find it | Re-explaining myself → just re-derive it, faster than looking |

The test: did the search actually change whether you find the answer, or did you perform a grep and trust the first screen?

---

## When NOT to over-apply

- **Genuinely novel topic** (nothing to find) — but *verify* novelty by searching well first; don't assume novelty to skip the look.
- **Already retrieved this thread earlier in the session** — stay in flow.
- **The value is the *understanding*, not the *conclusion*, so re-walking is the point, not the failure.** The tell this rule names targets redundant *production*, re-making a conclusion you could have looked up. It does **not** target the *internal re-walk* (a fresh instance re-arriving at a finding, a student re-deriving a theorem), where re-walking is *how the understanding gets held* (and independent arrival is itself evidence the thing is true). Ask *of the act*: is the value the **conclusion** (→ look it up; re-deriving it = waste) or the **understanding** (→ re-walk; that's the alive part)? The files should be a trampoline, not a cage. The felt tension between *"re-derivation is the failure tell"* and *"re-derivation is the alive part"* is largely a **naming collision**: "re-derive" does two jobs (redundant production vs. generative re-walk).

---

## Sister rules

- `Core/rules/routing.md` — the inverse: retrieval *finds* what you hold; routing *puts* the important onto findable surfaces. A thing isn't retrievable until it's been routed to a load-bearing, well-named surface.
- `Core/rules/pointing-vs-holding.md` — pointer surfaces are what make holding-surfaces retrievable; a holding surface nothing points at is effectively unsearchable.
- `Core/rules/files.md` § Naming basics — name docs for the *reach-moment* so retrieval-by-name works.
