# Tasks

Your active work. Use `/task` to create one. The AI handles the format.

One folder keeps things simple. YAML fields (`project` or `area`, `tags`, `people`) link tasks to projects without scattering files across the system. A task about your website and a task about a recipe live side by side, findable by searching tags, not by navigating folders.

Completed tasks auto-archive to `_done/`.

---

## Naming convention

Task files follow the format: **`{project or area} - {description}.md`**, lowercase.

Examples:
- `course - design syllabus.md`
- `personal - book dentist appointment.md`
- `system - tune wrap skill.md`
- `client-acme - draft proposal.md`

The prefix groups related tasks alphabetically (`ls Tasks/` shows all `course -` tasks together). The hyphen-space-hyphen separator reads naturally in a file listing. Spaces inside the description are fine, since file names aren't folder paths.

The prefix is whichever YAML field you set, `project:` or `area:`. Both forms exist because file listings sort by name and YAML enables tag-based queries; the prefix and the field serve different retrieval shapes.
