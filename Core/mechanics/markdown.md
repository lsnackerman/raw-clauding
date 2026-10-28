# Working in Markdown

*The syntax you'll use every day, and why it's worth the learning curve.*

---

## What it is

Plain text files with simple formatting. Both you and the AI read it the same way, with no translation layer. Your files live on your computer. No proprietary format, no subscription, no algorithm.

---

## The syntax

```
# Heading 1          (main sections)
## Heading 2         (subsections)
### Heading 3        (sub-subsections)

**bold text**        (emphasis, things you want to find later)
*italic text*        (softer emphasis)
~~strikethrough~~    (crossed out — great for showing what changed)

- bullet point       (brain dumps, lists)
- another bullet
  - nested bullet    (indent with 2 spaces)

1. numbered item     (when order matters)
2. another item

[link text](url)     (clickable links)

> blockquote         (quoting something)

--- (horizontal rule — visual separator)

`inline code`        (for commands or file names)
```

---

## YAML frontmatter

Some files start with a block like this:

```yaml
---
status: active
tags: [course, thinking]
---
```

This is metadata, structured information at the top of a file. The AI reads it to search and find things without opening every file. You don't need to write it from scratch. Your skills will generate it for you. Just know what it is when you see it. See `Core/mechanics/yaml.md` for the full picture.

---

## File naming

Folders are navigation: hyphens, no spaces (`meeting-notes/`, `Lennys-Podcast/`); a folder that holds a single item takes that item's title. Content files are readable, spaces preserved (`Lenny's Podcast - Some episode title.md`, a movie's real title), because the file is the thing and its name should read like it. CAPS files (`AGENTS.md`, `CLAUDE.md`, `ALIVE.md`) are entry points. Not `Meeting Notes (2).md`, a copy nobody meant to keep. The full split lives in `Core/skills/add/SKILL.md` § File naming.

---

## The learning curve

Working in markdown is the biggest hurdle. It's unfamiliar and not pretty like Notion. You'll want to go back to something with more visual polish. Stick with it.

The shift from *working* in markdown to *thinking* in markdown changes your actual thinking. You stop thinking about formatting and start thinking about structure. Headers become how you organize thought, not how you organize a document.

Give it two weeks. That's all it takes for the muscle to start building.
