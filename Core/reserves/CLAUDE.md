# Reserves — concept hubs

Raw `/explore` output preserved with full texture. One file per concept. Living documents.

---

## What this is

Each reserve maps a concept across your system: verbatim exchanges, decisions, patterns, connections. They're the raw thinking you can return to and build on.

Reserves are **raw**, not distilled. They don't compress. They don't summarize. They preserve the texture so synthesis can happen later, when you USE them.

---

## How they work

- **`/explore`** creates reserves. It searches across your system, returns verbatim quotes with sources, and lands the result in `Core/reserves/{topic}.md`
- **`/wrap`** maintains them. When a session touches a reserved concept, it appends to the Session Map at the bottom
- Reserves **compound over time**. Each `/explore` adds. Each `/wrap` appends. Subsequent runs find what's NEW and don't re-search what's already captured.
- Reserves can **graduate**. When a concept crystallizes, it distills into a depth-cluster doc (`Core/foundations/`, `Core/lenses/`, `Core/practice/`, or `Core/mechanics/`) or a rule (`Core/rules/`). The reserve stays as raw research; the distilled version is a different thing serving a different purpose.

---

## Where reserves live

In this folder. Three kinds, mixed flat:

- **Concept reserves** — one per concept (`{concept}.md`)
- **Snapshots** — point-in-time discoveries from undirected `/explore` (timestamped: `discovery-{date}.md`)
- **Extractions** — if you distill a thesis or takeaway from a reserve by hand, name it with its parent (`{concept}-thesis.md`) so the two stay together

The folder ships empty. Your first `/explore` puts something here.

---

## Working here

- **Creating**: `/explore` outputs here. Name files by concept.
- **Enriching**: subsequent `/explore` runs append. `/wrap` appends Session Map lines.
- **Using**: reserves feed writing, design decisions, sharing. Synthesis happens when you reach for them, not when you build them.
- **Don't compress**: full passages with source paths. The texture IS the value.

---

## Related

- **`Core/practice/explore-loop.md`** — the explore-reserves loop: mechanics, compounding, and the topic-deepening half of the two loops
- **`Core/skills/explore/SKILL.md`** — the skill mechanics
- **`Core/skills/wrap/SKILL.md`** — Session Map maintenance step
