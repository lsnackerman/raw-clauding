# Rules

*How to write the auto-loading layer (the depth beneath `Core/rules/codification.md` § How to write a rule).*

A rule is a markdown file in `Core/rules/` that shapes the AI's behavior and **auto-loads every session**. Same format as a skill, same compounding-through-use. The one difference is *when it fires*: a skill is **pulled** (you invoke `/gut` when you want it); a rule is **pushed** (it loads every session and shapes behavior whether or not you ask). Some skills never sleep. Those are rules. You write a rule the way you write a skill: live the pattern, codify it, let it improve through use.

*Whether* a recognition should become a rule (and at which tier) lives in `Core/rules/codification.md` § When to codify. This doc is the *how*, once you've decided.

---

## Rule vs skill — which layer?

The discriminator is **fire-condition**:

| | Fires… | Lives | Loads |
|---|---|---|---|
| **Rule** | by **presence** — automatically, every session (or when its `paths:` match) | `Core/rules/` | full contents at session start (like AGENTS.md) |
| **Skill** | by **invocation** — `/command`, when you reach for it | `Core/skills/` | YAML frontmatter at start; full body on invoke |

If the discipline should fire *automatically when something happens* (not when you remember to invoke it), it belongs here, in the auto-load layer. *(Example: routing fires when something important lands mid-session, not when you call it, so it's a rule, not a skill.)*

Because rules load *full* every session, they cost context every session, so they earn their place by firing often enough to be worth carrying, and they stay compact (the body is in the AI's working memory whether this session needs it or not).

---

## Anatomy of a rule

The shape rules converge on. Make these explicit when you write one:

- **A title + one-line statement of the principle** — the thing you'd say in a sentence.
- **The fire-condition** — *when* does this rule apply? Name the moment of friction ("fire when…", "the tell is…"). A rule no one knows when to apply doesn't fire.
- **The concrete move** — what to *do* at that moment. "The pause", "the test", "the verdict", a 2-column table. (See How to write, below.)
- **When NOT to apply** — the boundary. Most rules overshoot without it; naming the non-cases keeps the rule from firing where it shouldn't.
- **Sister rules** — at the bottom, the related rules + *how* they relate. Reciprocal references make the shape of your rule-set visible.
- **Origin line** — a pointer to the session where the rule landed (not a restatement of the case; the texture lives in the session capture you're already keeping). Keeps the rule lean *and* reminds you that rules come from *lived friction*, not abstract design. Early on your archive is thin, so these start sparse; like everything here, the habit compounds as you go.
- **"What we don't know yet"** — end a rule by naming its own uncertainties: in-flight questions, places the rule might overshoot, candidates for refinement. Models the rule's own malleability, since a rule that can't be questioned ossifies. (The starter rules mostly arrive without this section; yours are young and should have one.)

---

## How to write one (the moves)

- **Concrete moves, not abstract principles.** Every rule names *what to do at the moment of friction*. Abstract principles alone read as decoration; concrete moves give the rule teeth.
- **Origin lines as pointers, not restatements.** The rule holds the principle; the origin line points to the session where it landed. Detailed texture lives in the session capture. See `Core/rules/codification.md` § How to write a rule (the origin-lines convention).
- **Substantive vs Performative table** (when there's a load-bearing edge). When a rule has a real difference between *what helps* and *what looks like helping but doesn't*, a two-column table is the cleanest teaching shape.
- **Sister-moves cross-references.** Name related rules + how they relate (reciprocal, so the connection is visible from either side).
- **Name-not-number for stable references.** When pointing at sections in other docs, use the name, not the number. Names carry meaning out of context; positions drift when the source reorders.
- **"What we don't know yet" section.** End by naming the rule's own uncertainties, even one line.

The deeper bar: a rule should make *recognition faster*, not promise *prevention*. A codified rule doesn't stop the error; it gives both partners a handle to catch it faster. Write for the catch, not the fence.

---

## Scoping — `paths:`

By default a rule is **unscoped**: it loads every session, everywhere. Add a `paths:` glob to the YAML frontmatter and it becomes **path-scoped**. It only loads when the AI reads a file matching one of the globs:

```yaml
---
paths:
  - "Projects/**"
---
```

Leave a rule unscoped by default. The trade: scoping saves every-session context cost, at the price of the rule not firing when you're working anywhere outside the scoped paths. So **the honest reason to scope is context budget, not tidiness.** Argue it on those terms, and only after you've checked where the rule needs to fire (next paragraph). "It's a rule about sharing, so it belongs where the shareable work lives" sounds like a reason and is exactly the trap below.

**⚠ Scope by the moment the rule needs to fire, never by the topic it's about.** These come apart, and the failure is quiet. A path-scoped rule loads when the AI **reads a matching file**, so if the rule is a *decision gate*, scoping it to the files you'd create means it arrives **after** the decision it was meant to inform. A rule about writing rules, scoped to your rules folder, only shows up once you're already writing one; the guard against building the wrong thing fires after you've built it.

Ask: *"where will I be, and what will I be looking at, at the moment this needs to fire?"* If the answer is "in conversation" or "anywhere," it can't be path-scoped at all, because the moment leaves no file-read to trigger on. **Topic-scoping is the tempting mistake** because the glob looks obviously right (a rule about X, scoped to where X lives) while quietly guaranteeing the rule can't reach the moment it exists for.

Expect the mechanism to earn less use than it looks like it will. In the system this starter was drawn from, every rule that seemed a natural fit for a scope turned out, on inspection, to be scoped away from its own fire-moment; all of them were lifted, and `paths:` ended up with no users. None of the starter's rules are scoped. It's documented because it's a real capability, not because you should reach for it.

---

## Placement & when to make one

Rules live flat in `Core/rules/` (no clusters, since the set is small enough to scan). The `.claude/rules/` symlink is auto-created by the `ensure-symlinks` hook **on the write itself** (it runs after every Write/Edit, not just at session start). Don't hand-create it. *(A rename is a `mv`, which doesn't trip the edit-hook, so after renaming a rule run `bash Core/scripts/ensure-symlinks.sh --check`.)*

*Whether* a recognition has earned a rule (and the rule-vs-memory, rule-vs-compass tier judgment) is `Core/rules/codification.md` § When to codify (the tier table). Don't re-derive it here; this doc assumes the decision is made and you're writing the rule.

---

## Sister docs

- `Core/rules/codification.md` — the *judgment* layer (when/whether to codify, at which tier) + the operative how-to-write-a-rule summary that points here. This doc is its depth.
- `Core/mechanics/skills.md` — the peer: how to write a skill (the *pulled* primitive to this *pushed* one).
- `Core/mechanics/hooks.md` — the peer primitive at the automation layer (deterministic bash, fires at lifecycle points; not AI behavior, but the same "always-on" family).
- `Core/rules/codification.md` § How to write a rule — the origin-line convention these rules follow.
