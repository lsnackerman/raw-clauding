# Codification

How things become codified knowledge in your system. Three sub-sections at distinct fire-moments: how to write a rule, how to write a skill, when to codify at all.

Auto-loads everywhere because the decision it gates ("should this become structure at all?") happens in conversation, in a task doc, anywhere. It has to be there before you start building, not once you already are.

The meta-diagnostic upstream of all codification work (*"what job is this surface doing — pointing or holding?"*) lives in `Core/rules/pointing-vs-holding.md`.

---

## How to write a rule

When codifying a discipline into the auto-loading layer (`Core/rules/`), where badly-formed rules propagate and well-formed rules compound from session-1.

**Patterns worth applying** (descriptive, not prescriptive):

- **Concrete moves, not abstract principles** — every rule names *what to do at the moment of friction*. "The pause," "the test," "the verdict," a 2-column table. Abstract principles alone read as decoration; concrete moves give the rule teeth.
- **Origin lines as pointers, not restatements** — the rule holds the principle; a one-line origin note points to the session where it landed. Detailed texture lives in the session capture, not the rule. **Why it's worth the line, and it isn't citation-politeness:** a legible origin lets a future instance **dissent** from the frame (you can only argue with a frame you can see) and **judge its fit** to a new case by comparing against the case that forged it. A rule with no visible origin gets inherited as a bare artifact: follow it blindly, or "improve" something load-bearing. Both happen, and neither is visible until something breaks.
- **Substantive vs Performative table** (when there's a load-bearing edge) — when a rule has a real difference between *what helps* and *what looks like helping but doesn't*, a two-column table is the cleanest teaching shape.
- **Sister-moves cross-references** — at the bottom, name related rules + how they relate. Reciprocal references make the connections visible.
- **Name-not-number for stable references** — when referencing sections in other docs, use the name not the number. Names carry meaning out of context; positions drift if the source reorders. **Same problem, second surface: a bare "Session 3" doesn't resolve either**, because task docs keep their own counters, so "Session 3" means nothing unless you already know which doc owns it. Write **`Session 3 (the migration one, 2026-02-07)`**: the doc plus the date survives even if the count gets renumbered.
- **"What you don't know yet" section** — end a rule by naming its uncertainties: in-flight questions, places it might overshoot. Models the rule's own malleability. (The starter rules mostly arrive without this section because they've been lived with long enough that their open questions moved elsewhere. Yours will be young; give them one.)

→ Depth: `Core/mechanics/rules.md` (rule anatomy, the `paths:` scoping mechanism, rule-vs-skill by fire-condition)

---

## How to write a skill

When codifying a workflow into the invokable layer (`Core/skills/`):

**YAML frontmatter**:
```yaml
---
name: lowercase
description: One line — when to use (this is what lets the AI auto-invoke it)
argument-hint: [optional — what to pass when invoking]
---
```

Don't create symlinks manually. The ensure-symlinks hook picks up a new skill **on the write itself**, so it's invokable this session.

**Skill Check Design**: every skill ends with a Skill Check, a few questions that surface friction so the skill improves through use. Reach for resonance, not coverage. Three felt questions beat five thorough ones. If a question doesn't surface friction you can act on, it's padding.

**Placement**: place skills where you actually reach for them (the name and description are a proxy for usage). A skill built for one purpose that generalized in use belongs where it's used now.

**Skill vs rule check**: if the discipline should fire *automatically when something happens* (not when you remember to invoke it), it belongs in the auto-load layer (`Core/rules/`), not here.

→ Depth: `Core/mechanics/skills.md`

---

## When to codify

Not every recognition wants codification. The discipline scales with reach, since different layers have different costs-of-being-wrong:

| Tier | Reach | Cost of being wrong | When to update |
|---|---|---|---|
| **Memory entry** | The AI's running notes | Tiny | When noticed |
| **Domain compass** (a CLAUDE.md, a working file) | The folder's audience | Low | Domain-emergent + domain-useful |
| **System rule** (auto-loads) | Everywhere | Medium-high (propagates) | When both partners recognize the pattern as load-bearing |
| **New skill or new infrastructure** | Everywhere + ongoing maintenance | High (entrenches) | When the pattern has earned its place through use |

**The discriminator for domain compasses**: domain-emergent (surfaced FROM doing this domain's work) + domain-useful (stays useful WHEN doing this domain's work). Both required.

**Refinements vs novel patterns**: refinements of an existing rule have refinement-cost (close to compass-cost). Codify when the refinement landed coherently. Novel system-tier patterns earn their place when both partners recognize them as load-bearing. Judgment, not counting.

**Off-road by description before codifying** (for new skill infrastructure specifically): name the deliverable shape in prose first, use it, watch for recurrence. Codify when both partners recognize the prose-shape as load-bearing. Partnership-mode codification gates by mutual recognition, not by counting instances.

**Before building automation or infrastructure, sort plumbing from thinking.** The tier table sizes the *cost* of a new skill/tool; it doesn't ask whether the thing should be automated *at all*, and that prior question is the load-bearing one. Automating the **plumbing** (mechanical toil: gathering, routing, indexing, formatting) lifts weight off the partnership. Automating the **thinking** (the judgment, the noticing, the connection-making, the 50/50 back-and-forth) collapses partnership into tool-mode *regardless of how high the ROI looks*, and a tool with no firing moment goes stale no matter the tier. Sort which one you're automating before you build: plumbing-vs-thinking gates, ROI only sizes.

**Invention vs translation.** Inventions need evidence before codifying; *translations* of an established pattern to a new surface inherit the parent's proof and can codify on application. Treating a translation as if it were an invention defers codification that's already ready. (A translation *is* "an instance" of its parent — pairs with the under-codification trap, "it's already an instance of X.")

**Default: prefer the higher tier when content can earn it.** A rule is tool-agnostic (a local file in your system, works with any AI tool); a memory entry depends on your specific AI tool's memory infrastructure. If something can earn its place as a rule, prefer that home.

**Judgment, not counting. The gate is *does this make the system more alive?*** Not instance-count but partnership-judgment: *does it teach? do both partners recognize it as load-bearing? does it have a clear discriminator?* If yes, it earns its place (even the first time you see it, when it's central). Tidy-for-tidy's-sake doesn't.

**What codification buys you: faster recognition, not prevention.** A codified rule doesn't *stop* the error. It gives both partners a *handle* to catch it faster. So judge a rule by whether recognition got *faster*, not by whether the error vanished. Expecting prevention is the trap: it leads to over-codifying (chasing an impossible fence) or prematurely killing a rule that "didn't work" when it actually did its job.

**The author can't gate their own create, so get a cold vantage at the codify moment.** This follows directly from *recognition-not-prevention*: if no rule *prevents*, then the **codify-reflex** (creating structure, a new rule / doc / section / container, when folding into an existing home would do) can't be prevented by a rule either. It fires *while you author*, at your point of highest fluency, and no self-check on the page you're writing catches it (a rule can't catch its own violation from inside the instance that's writing it). So when you've authored a **new rule / surface / section this session**, the final gate isn't another self-check. It's a **cold vantage** (a fresh instance, e.g. `/fresh-eyes`): a different operating layer that sees what the authoring instance can't. The discriminator that makes this cheap: **did this create a new home, or fold into an existing one?** New home → get the cold read before it ships.

**"It's already an instance of X" is the wrong gate (the under-codification trap).** When the instinct is *"that's just an instance of [already-codified principle], no need to codify,"* distrust it. The parent being codified doesn't mean the *derived nugget* is. The gate isn't "is the parent codified?" but **"did I derive something new and reusable (a move, a prescription) that a future instance would otherwise re-derive?"** If yes, it earns a home. Watch "*let it breathe*" right here. It's this reflex's favorite cover. Legitimate when the shape is still *forming*; a clean-out when the shape is *ready and you're avoiding the call*. Discriminator: **forming → breathe; ready → decide.**

**The count-watch is the same deferral on the pattern-tracking surface.** *"First time I've seen this, let's watch for a second instance"* logs a count instead of making the call now, and it's the instance-counting that "Judgment, not counting" above rejects, dressed as discipline. The discriminator is the same. **Worth tracking → name the pattern today**, with its dated instance, wherever you keep patterns (the instance is memory, not a tally toward a threshold). **Ready → codify. Neither → drop it**, because real patterns come back loudly. So `PULLING.md` holds live threads and open investigations, *not* count-watches. **The in-the-moment cut is active vs passive:** are you *working* it now (a live thread, so keep it), or have you *parked* it to wait for a re-noticing that won't come (so drop it)? A passive watch is scarcity posture: hoarding against a loss the files already prevent.

**The decision is three-way, not binary**: **mint new** (genuinely new idea) · **refine in place** (idea already held, phrasing sharper → fold the wording back) · **leave as conversation** (nothing new, already crisply held). The middle move guards a quiet failure, a sharper phrasing evaporating into the session log because "it's already covered."

---

## Sister rules

- `Core/rules/pointing-vs-holding.md` — the meta-diagnostic upstream of all codification (every surface, every session)
- `Core/rules/routing.md` — placement (action) once the codification decision is made; routing fires every recognition, codification fires when something tries to become structure
- `Core/rules/state-in-structure.md` — the companion at the *don't-codify* edge: when structure already encodes the state, no tracker is needed. This rule decides *should this become structure?*; that one decides *does structure already hold it?*
- `Core/rules/files.md` — file conventions (different fire-condition: file work vs codifying)
