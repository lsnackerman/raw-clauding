# YAML templates for /add

Full examples for each content type. Loaded with /add skill on invocation, not at session start.

Authoritative schema and field rules: `Core/mechanics/yaml.md`.


---

## Examples

**Podcast:**
```yaml
---
type: podcast
people: ["Lenny Rachitsky", "Brian Chesky"]
organizations: ["Lenny's Podcast"]
url: "https://youtube.com/watch?v=..."
video_id: "abc123"
duration: "1:23:45"
projects: ["lab/course"]                           # optional — projects this content feeds
date: 2024-01-15
date_added: 2026-02-08
tags: ["founder-story", "product-market-fit"]
description: "LLM-facing: topics covered, key insights"
---
```

**Article:**
```yaml
---
type: article
people: ["Lenny Rachitsky"]
organizations: ["Lenny's Newsletter"]
url: "https://..."
date: 2024-01-15
date_added: 2026-02-08
tags: ["pricing-strategy", "B2B"]
description: "LLM-facing summary"
---
```

**Recipe:**
```yaml
---
type: recipe
people: ["Angela Liddon"]
organizations: ["Oh She Glows"]
url: "https://..."
category: ["soups"]
date: 2024-01-15
date_added: 2026-02-08
tags: ["vegan", "one-pot"]
description: "Imagine you're about to cook this - what do you need to know?"
---
```

**Lightning Lesson:**
```yaml
---
type: lightning-lesson
people: ["Teresa Torres"]
organizations: ["Maven"]
url: "https://maven.com/..."
duration: "45 min"
date: 2026-01-25
date_added: 2026-02-08
tags: ["product", "discovery"]
description: "LLM-facing summary"
---
```

**Bookmark:**
```yaml
---
type: bookmark
url: "https://..."
date_added: 2026-02-08
note: "Why I saved this"
tags: ["open-web", "tools"]
---
```

`projects:` (optional) applies universally. Add to any type when content feeds specific project work. See SKILL.md § Project tagging for capture flow.

**Migration note:** Older files may use v1 schema (`source_url`, `date_captured`, `saved_date`, wikilinks in people, `needs_tcp`). Mechanical fields migrated via script; `description`, `organizations`, and `projects` added organically.
