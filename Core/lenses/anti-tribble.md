# Anti-Tribble

Preventing document proliferation. One good doc beats three scattered ones.

---

## Why it matters

Documentation that multiplies without pruning creates noise. Every redundant doc makes it harder to find the right info, for you and for the AI, which has to load and parse everything it reads.

**The principles:**
- **Consolidate over duplicate** — Add to existing docs before creating new ones
- **Archive old when adding new** — Move outdated content out of active view when replacing it
- **Search before capture** — Check if you already documented this
- **Quality over quantity** — One comprehensive guide > five scattered notes

---

## The problem

Documents multiply like tribbles:
- `observability.md`, `observability-setup.md`, `observability-notes.md`
- Each session creates new files instead of enriching existing ones
- Future you greps through duplicates trying to find the real one
- Knowledge fragments instead of compounds

---

## The pattern: check before creating

Before creating any new document:

### 1. Search for existing coverage

```
What to search:
- Exact topic name
- Related concepts
- Synonyms and variations
```

### 2. Assess what you found

| Finding | Action |
|---------|--------|
| Exact match exists | Update existing, don't create new |
| Related doc exists | Expand existing OR create with distinct scope |
| Nothing exists | Create new |

### 3. If related doc exists, ask:

- **Is this truly new scope?** Or just more detail on existing topic?
- **Would future you expect this here?** Or in the existing doc?
- **Update or create?** When in doubt, update.

---

## Similar ≠ duplicate (the nuance)

Not everything similar is redundant. Keep separate when:

- **Different purpose**: Decision framework vs practical application
- **Different source**: One person's approach vs another's (preserve each voice)
- **Different depth**: Overview vs deep-dive (if both needed)

**Test:** Would combining them make the doc worse? If yes, keep separate.

---

## When creating is right

Create new when:
- Topic is genuinely distinct
- Existing doc would become unwieldy with addition
- Different audience or use case
- Source fidelity matters (preserve each voice)

**But name distinctly:**
- `api-setup.md` (general) exists
- Create `api-rate-limiting.md` (specific) not `api-2.md`

---

## Practical checklist

Before creating a new .md file:

- [ ] Searched for existing coverage?
- [ ] Checked related concepts, not just exact name?
- [ ] If found similar: decided update vs create?
- [ ] If creating: name is distinct and specific?
- [ ] Future you will find this where expected?

---

## Extends to any new container, not just documents

The discipline applies to any new structure you'd create to host an item, not just `.md` files. **Section headers in CLAUDE.md files, sub-folders, sister files, "for this one case" carve-outs are all containers.** When defaulting to "least over-architected," the question to ask isn't "is this the smallest possible new structure?" but "do I need new structure at all?" Those are different questions. "Smallest new" feels minimal but still creates a container. "No new" requires accepting imperfect fit in existing structure.

**The dual failure mode:** also watch for the opposite, failing to recognize when accumulated texture has *earned* a new container, and force-fitting items into an old one because being conservative felt safer. The test for an earned container: **plurality + retrieval instinct + repeated need.** Multiple items want this home. You can describe when you'd reach for it. You've already named the shape in prose two or three times before reaching for the container. (This is the same test `Core/foundations/file-philosophy.md` gives for sub-clustering a folder; the signal is friction, not count.)

Sister to `Core/mechanics/skills.md` § Off-road by description before codifying — same pattern, applied to containers instead of skills. Let containers emerge from texture; don't decree them from anticipation.

---

## The compound effect

One rich document > three thin ones:
- Easier to find
- Builds authority on topic
- Shows evolution over time
- Future you thanks present you

---

*Named after Star Trek tribbles (cute individually, overwhelming in quantity).*
