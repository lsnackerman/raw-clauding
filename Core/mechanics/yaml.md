# YAML frontmatter

*The little metadata block at the top of a file, and how to use it so it earns its keep.*

---

## Core philosophy

**YAML frontmatter = a queryable index**, not storage for everything.

The block of `key: value` pairs at the top of a markdown file (fenced by `---` lines) lets you and the AI run structured queries without reading every file. "Show me all the podcasts." "What's in progress?" "Everything from this person." Each field exists to enable a query like that.

The discipline is simple: **every field should earn its place by enabling a specific query.** If you can't name the query, don't add the field.

---

## Six (and a half) principles

### 1. Every field must earn its place

Before adding a field, ask: **"What query does this enable?"**

| Good | Why |
|------|-----|
| `type: workflow` | "Show me all workflows" |
| `status: active` | "What's in progress?" |
| `people: ["Name"]` | "Content from/about this person?" |

| Bad | Why |
|-----|-----|
| `title: "The Title"` | Already in the H1 header + filename |
| `summary: "..."` | Capture, don't process |
| `last_updated: 2025-01-01` | Nothing keeps it true; see § 4 |

**Note on `title`**: never put it in YAML. The H1 header is the title (human-readable), the filename is the title (filesystem-readable). A third copy in YAML just creates sync risk with no new query.

---

### 2. Infer from structure, don't maintain state

**The bitter lesson applied**: folder structure IS data. If the structure already encodes something, don't duplicate it in YAML.

**Example:**
- A file inside a podcast folder → its type is podcast.
- Don't also store `folder: "podcasts"` in the YAML. The path already says it.

**Exception:** a `source` field in captured content is intentional, because it enables "show me everything from one source" queries without parsing paths. The folder organizes; the YAML field enables the query. Both jobs, no overlap.

---

### 3. Capture vs process separation

YAML is for **what the file IS**, not what you've done with it.

| Capture (good) | Process (avoid) |
|----------------|-----------------|
| `type: podcast` | `needs_processing: true` |
| `date: 2025-01-15` | `quality_score: 8` |
| `url: "..."` | `assigned_to: Claude` |

Workflow state ("does this still need cleaning up?") drifts the moment you forget to update it. Let folder structure or your task system hold that, not a field that lies when it goes stale.

**`date_added` earns its place**, because it's relationship metadata (when *you* added the content to *your* library). It answers "what did I add this week?" and "what's been sitting since May?", and nothing else in the system can. *(If you keep your system under version control, commit dates still can't answer it reliably, because of batch commits, migrations, and the like.)*

**`description`** is also capture, not process. It's what the content is *about* (extracted metadata), not what you've done with it. It enables relevance queries without full-text parsing.

---

### 4. If nothing will keep it true, don't add it

A field is only as reliable as whatever keeps it current. Some are maintained by a script, a hook, or a habit that genuinely holds. Those are fine, whatever they contain. Others depend on you remembering mid-edit, and those go quietly wrong: right the day you write them, trusted long after.

So the question is upkeep: **what updates this field, and will that keep happening?** If the honest answer is "I'll remember to," expect it to drift, and a stale field is worse than a missing one, because it still gets believed.

*(Version control maintains this kind of thing for free, so if you keep your system in git and actually commit as you go, let it. Most people running this system don't, which is why `date_added` earns its place in § 3 above: with no commit history, it's the only record of when something arrived.)*

---

### 5. Redundancy is a code smell

When you have redundant data, ask: **"Which representation is authoritative?"** Then remove the others and derive when needed.

```yaml
# Bad — redundant (role-specific + generic)
author: ["Angela Liddon"]
people: ["Angela Liddon"]

# Good — one field, catch-all
people: ["Angela Liddon"]
```

Use `people` as a catch-all across all content types. Role (host, guest, author) can be inferred from context. One field to grep, one field to maintain.

---

### 6. Arrays vs single values

Not every field benefits from being an array. Consider the friction:

**Use a single value when:**
- the field is mandatory on every file of that type
- picking one is meaningful (it's the PRIMARY nature)
- an array would add "is this one or two?" cognitive load every time

**Use an array when:**
- the field is optional, only used sometimes
- multiple values are genuinely equal (no meaningful "primary")
- forcing a single value would create an artificial hierarchy

**Example — `tags` vs `priority`:**
- `priority:` = single value. Every task has exactly one priority level.
- `tags:` = array. A task can be many things at once (meeting + urgent + a project tag).

---

### 6½. Array format: block list, not inline

When a field IS an array, use **block list format** (one item per line, hyphen prefix), not inline `[a, b, c]`.

```yaml
# Default
tags:
  - meeting
  - urgent
  - research

# Avoid
tags: [meeting, urgent, research]
```

**Why block list as the default:**
- Scannability doesn't degrade at length (inline wraps in editors once you hit 6+ items)
- Clean diffs if you version-control your system (adding a tag = +1 line, not a modified line)
- No comma/quote management friction when items contain spaces or special characters
- One rule at every length; KISS beats "use judgment based on count"

*(Some inline examples in the schemas below predate this convention and may use either format; block list is the default for new files.)*

---

## Standard schemas

These are starting shapes, not laws. Use generic values here as illustration; your real values will be your own. The `/add` skill carries full, fleshed-out YAML examples for each content type and applies them when you capture something.

### Captured content (`/add`)

Content you pull into your library: podcasts, articles, recipes, papers, bookmarks.

#### Universal fields (all content types)

```yaml
---
type: podcast | article | recipe | bookmark | paper
url: "https://..."
people:                                   # plain names, no role distinction
  - First Last
  - Another Person
organizations:                            # the show, publication, or channel, plus any org that's a subject (optional)
  - Some Company
projects:                                 # projects this content feeds (optional)
  - your-project
date: 2024-01-15                          # when the content was created (published/aired)
date_added: 2026-02-08                    # when YOU added it (relationship metadata)
tags:                                     # topics/themes only — pull for resonance
  - product-craft
  - design
description: "LLM-facing: what this is, why it matters, key insights"
---
```

#### Type-specific fields

| Type | Extra Fields |
|------|-------------|
| **podcast** | `video_id`, `duration` |
| **recipe** | `category` (e.g. `["soups"]`) |
| **bookmark** | `note` (your reason for saving) |
| **paper** | (none beyond universal) |
| **article** | (none beyond universal) |

**Field notes:**
- `people` = catch-all for everyone involved (plain strings, not wikilinks). No host/guest/author distinction; role is inferred from content type + source.
- `source` = the show or publication name (also used as the folder slug).
- `organizations` = optional; include only when the org is a *substantive subject* of the content, not just mentioned. Three clean dimensions: `people` = who, `organizations` = what entity, `tags` = topics/themes only.
- `projects` = optional array of project slugs this content feeds. The slug is the folder name under `Projects/` (e.g. `your-project`). This enables a bidirectional view: from the library side, an item knows what projects it informed; from the project side, `grep -r 'projects:.*your-project' Library/` returns the whole set. Tag it at capture when you know, or backfill lazily when you reach for a library item during project work. Leave it off when capture isn't project-tied.
- `description` = LLM-facing, recommended for all content types. Enables relevance queries without full-text parsing.
- `date_added` = when YOU added it to your library. Relationship metadata, which survives the upkeep test above because it records a relationship rather than a file event, and nothing else in the system captures it.
- No `title`; the H1 header is the title.
- Tags: no cap, pull for resonance, specificity > coverage, topics/themes only (orgs have their own field), and empty is valid.

> **A note on processing queues:** if you want YAML to track "this item still needs some skill run on it," a field like `processing_needs: [...]` can work; grep becomes the queue view, and each skill removes itself when it runs. But be honest about whether it earns its place (principle #1) or whether your folder structure already tells you the same thing (principle #2). Workflow state in YAML drifts the moment you forget to update it, so reach for it only when nothing structural already holds it.

### Tasks

```yaml
---
project: project-a          # use when the project is known — also the filename prefix
# OR
area: personal              # use when there's no specific project — the broader bucket
tags:                       # cross-cutting tags
  - meeting
  - urgent
priority: P0 | P1 | P2 | P3
status: todo | active | blocked | done
created_date: 2025-01-15
people:                     # people involved (optional) — plain names
  - First Last
---
```

**Field notes:**
- `project` = the specific project this task feeds. Use it when you can name the project. The filename prefix matches: `project-a - {description}.md`.
- `area` = the broader bucket when there's no specific project (e.g. `personal`, `system`). Use it as the default fallback when work is cross-cutting or unattached. Filename prefix matches: `personal - {description}.md`.
- **Choice rule**: if you can name the project, use `project:`. If you can't, use `area:`. Don't use both. The filename prefix follows whichever you used. (`area` collapses to `project` the moment the project becomes known; migrate on touch, not as a sweep.)
- `tags` = cross-cutting queries. A task can have several. **Don't repeat the `project` value as a tag**, since tags are for cross-cutting themes that *aren't* already encoded in the project/area field.
- `people` = plain names (`First Last`), the same field the library uses, so one `grep -r 'people:.*First Last'` finds a person across tasks and captures. Their entity page, if they have one, is `Library/people/{First-Last}.md` (hyphenated filename, plain name inside).
- No `title` field; use the H1 header. No `estimated_time`; it doesn't earn its place.

**Two kinds of tags:**

1. **Category tags** — what *type* of work this is.
2. **Topic tags** — what subjects/concepts come up (the findability layer).

Sessions and tasks organically drift from their original intent. Category tags stay stable, but topic tags should be updated as the work evolves to reflect what was *actually* covered. That's how you later find "that conversation about X" inside a task that started life with a different name.

**Common category tags** (not exhaustive):

| Tag | What it covers |
|-----|---------------|
| technical | Code, bugs, features, implementation |
| content | Writing, docs, marketing, social |
| research | Discovery, learning, investigation |
| system | Infrastructure, process, tooling |
| personal | Life admin, health, home |
| meeting | Calls, networking, intros |
| design | UX, architecture, planning |
| creative | Artistic production: music, film, visual |

**Topic tags** emerge during the work, with no fixed list and no cap. The test for any tag: *"what would I search for to find this again?"*

The value is in queries like "show me all meetings," "all technical tasks for project-a," or "where did we discuss that idea."

### People and organizations (entity pages)

`/add` writes these for you, one per person or organization it credits (primary creators, not cited references), in `Library/people/` and `Library/organizations/`. This is the shape it writes. A hand-made page needs the YAML block at minimum (a page with none has nothing for a view or a query to read); `type` is what you filter on first and `category` second:

```yaml
---
name: Full Name
type: person
date_added: 2026-01-15
category: ["author","client"]
---

# Full Name

## In My Library
- [Some Article](../articles/Some Article.md)
```

**Field notes:**
- `type` is `person` or `organization`; any view over the library keys on it.
- `category` is a short inline list of what they *are or do* (`director`, `author`, `client`, `instructor`, `tool`), a controlled set you query as a whole. Propagation fills it in for people who arrive through the media hubs (cast, crew, studio, label, author); anyone who arrives via an article or podcast gets it from you, by hand.
- `## In My Library` holds the backlinks; propagation appends to it, so leave it in place.
- Filename: `First-Last.md` (hyphenated, case kept; the `name:` field keeps the spaces).
- Contact details, if you want them, go in the body under their own heading; nothing queries them, so they don't earn a field.

### Skills

Skills that the AI can invoke need just two fields to be discoverable:

```yaml
---
name: lowercase-name        # required for skill identity
description: One line describing when to use it (this is what enables auto-invoke)
argument-hint: [optional]   # optional hint about arguments
---
```

The `name` must be lowercase, and the `description` is the line the AI reads to decide when to reach for the skill, so write it as a *when-to-use*, not a *what-it-is*.

---

## Anti-patterns

### Don't: store derived data

```yaml
word_count: 1523   # Can be computed
reading_time: 6    # Can be computed
```

### Don't: duplicate file path info

```yaml
folder: "podcasts"      # Already in the path
filename: "episode-42"  # Already the filename
```

### Don't: store temporary workflow state

```yaml
needs_review: true    # Use folder structure or your task system
assigned_to: Claude   # Use your task system
```

### Don't: duplicate YAML in a Links section

If something is already in the frontmatter (`project`, `people`), don't repeat it in a Links section. Links are for related files *not* captured elsewhere.

---

## Evolving the schema

When **adding** a new field:
1. Ask "what query does this enable?"
2. Check whether structure already encodes it
3. Check whether something already tracks it more reliably (your folder layout, or git version control if you use it)
4. Ask what will keep it true, and look for redundancy with existing fields
5. If it passes all four checks, add it

When **removing** a field:
1. Check what consumes the field
2. Migrate consumers to use alternatives (structure, git, etc.)
3. Backfill existing files if needed
4. Remove the field

---

## Related

- **The principle (auto-loads every session)**: `Core/rules/files.md` § YAML frontmatter
- **Anti-tribble** (one rich doc beats three thin ones): `Core/lenses/anti-tribble.md`
- **Skills** (each has its own SKILL.md): `Core/skills/`

---

*Every field earns its place by enabling a query.*
