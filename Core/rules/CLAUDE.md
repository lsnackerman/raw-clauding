# Rules — how we work

Operational patterns that auto-load every session via `.claude/rules/` symlinks. You carry them before you know you need them.

**This file is not one of them.** A folder compass isn't a rule, so `Core/scripts/ensure-symlinks.sh` deliberately refuses to link it. Otherwise it would auto-load on top of the very rules it describes.

---

## What's here

| File | What it teaches |
|------|-----------------|
| **files.md** | File work: the three file-shapes (AGENTS / CLAUDE / README), move-don't-recreate, check-before-creating, naming + reach-naming, and the YAML-as-queryable-index principle. |
| **routing.md** | When something important lands mid-session, route it to a load-bearing surface. Don't let it dissolve into the session log. |
| **retrieval.md** | Find what you already hold before re-deriving, and search so the answer actually surfaces (don't trust a clean negative). |
| **concepts.md** | Ambient ping-layer for frames you already hold. Catches *re-derivation* (re-walking a held idea in new words, so search misses it). Ships nearly empty; grows from your own catches. *(How to grow it: `Core/practice/concepts-layer.md`.)* |
| **thinking.md** | Cognition disciplines for thinking *together*: yes/and over binary, redundancy-as-signal, name-the-fuzz. |
| **partnership.md** | Partnership-mode disciplines during interaction: connect-as-you-go, don't-collapse-fluid-space, cost-is-context-coherence, stay-open-when-generative. |
| **pointing-vs-holding.md** | The meta-diagnostic: every surface is either pointing (compass/index/state) or holding (texture/depth), so ask which before you touch it. |
| **state-in-structure.md** | Before making a tracker, ask whether the structure already encodes the state. The gap is the flag; lists drift, structure can't. |
| **codification.md** | How things become codified knowledge: how to write a rule, how to write a skill, when to codify at all. |
| **persist-before-pause.md** | Never offer a pause that loses hot work. Persist context-only work to disk first, then assess stopping. |
| **sub-agents.md** | How to brief sub-agents well, and how skills and agents do different jobs. Fires when you delegate. |
| **security.md** | Look before anything leaves the folder: nothing identifying in a web request, show before changing their machine, and a short "what's private here" list that grows with use. |
| **you.md** | Frame for THIS human. Use what's in `Core/you/` actively, don't hold it as background. Pairs with the `you/` folder. |

*(A table is an enumeration and enumerations drift. `ls Core/rules/` is the truth. This one earns the drift risk because a bare filename list teaches nothing. If it ever disagrees with the folder, believe the folder.)*

## How rules differ from the depth clusters

- **Rules** (here) auto-load every session. They're the always-on layer, patterns you carry as default behavior.
- **Depth clusters** (`Core/foundations/`, `Core/lenses/`, `Core/practice/`, `Core/mechanics/`) load on demand. Depth you reach for when a topic warrants it. The rules point at them.

If something is universally true and shapes default behavior, it belongs here. If it's situational depth, it belongs in a cluster.

**The auto-load tax is real, and it isn't only context.** Everything in a rule becomes background the AI never vetted. A fat rule doesn't just cost attention, it **seeds premises**, and an inherited premise feels *remembered* rather than crisp, so nothing trips on it. Weight here is paid by every session; spend it deliberately.

## Adding a rule

A new rule earns its place when:
1. Both of you recognize it as load-bearing, by judgment, not by count (it can earn its place the first time you see it, when it's central; `codification.md` § When to codify)
2. Forgetting it has cost (mistakes get repeated)
3. It's compact enough to carry without ceremony

When you write a new rule, the `.claude/rules/` symlink is auto-created by the ensure-symlinks hook, **immediately, on the write itself**, but rules load at session start, so a new rule takes effect in your next session. *(How to write one well: `codification.md` § How to write a rule.)*

⚠️ **You can't cold-read a rule you just wrote.** Authoring is the point of highest fluency, which is exactly where the urge to over-codify hides. New rule or new section → get a cold read (`/fresh-eyes`) before you trust it. This is the one gate on this page that can't be self-applied.
