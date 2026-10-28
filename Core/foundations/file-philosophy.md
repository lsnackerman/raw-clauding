# File philosophy

Start building your local markdown library now.

---

## Local

Curating your own thinking in your own space.

Plenty of apps will let you arrange your thinking, but what makes it yours is whether the files underneath are on your disk in a format anything can read. When your thinking lives in a hosted workspace in a proprietary format, you can't point an AI at it and say "think with me," and you can't take your architecture with you when you switch. When it's markdown in a folder you own, neither of those is a question.

Local means: your structure, your files, any tool you want to think with. Today it's one thing. Tomorrow it's something else. Your thinking doesn't migrate, your tools do.

---

## Markdown

The universal language of thought-as-file.

Plain text that humans can read and machines can read. No proprietary format. No rendering engine required. No version compatibility. A markdown file from 2015 opens the same today.

Markdown is the file format that gets out of the way. Headers, links, lists, emphasis. Enough structure to organize, not enough to constrain. An AI can read it, grep can search it, git can version it, any editor can open it.

The bet: whatever AI tools exist in five years, they'll be able to read a markdown file.

---

## Architecture

Where you put things signals what you believe about them.

Files are captured thoughts. Architecture is the intentional arrangement of relationships between those thoughts. Not the thoughts themselves, but the *relationships*.

When you move a folder from nested to root-level, no content changes. What changes is what it *means* relative to everything else. A folder called `library/` inside a project says "this project has reference material." The same folder at root says "this is the system's reference layer." The content could be identical. The argument about its role is completely different.

Architecture teaches intent before a single word is exchanged. A new collaborator (human or AI) lands in your file system and immediately learns what matters, what's active, what's archived, what relates to what, all from structure. No manual required.

**Move, don't recreate.** When you reorganize, move the original file. Don't read it and rewrite it somewhere new. Recreating introduces silent errors (wrong formatting, lost metadata, broken links). The file IS the thought. A copy is an approximation. Match the size of the action to the size of the change. (See also: `anti-tribble.md`.)

### The three file shapes

Three orientation-file conventions, each with a job:

- **`AGENTS.md`** — at the root, one per system. Tool-agnostic compass, so any AI reads it. "Who we are, what this is." Already at the root of your starter.
- **`CLAUDE.md`** — in subdirs, as deep as useful. Folder-level orientation. Claude Code auto-loads each one as it reads into the folder, so subfolders can carry their own context without explicit cross-references.
- **`README.md`** — for distribution artifacts only (public repos, packages shipped to others). Universal convention; GitHub renders it, every tool shows it.

**Default: CLAUDE.md solo in subdirs.** Auto-loads, serves both human and AI, no sync drift between two compass files. A README.md only earns its place at the root of a distribution artifact that ships through a surface where humans browse before they clone (a public GitHub repo, an npm package, an open-source release). Anywhere else, CLAUDE.md is the right shape.

**If you land in a subfolder that should have a CLAUDE.md but doesn't, flag it.** Folder-level orientation is what makes a system navigable for any AI that lands in it cold.

### Folders cluster as they grow

A folder is a mental bucket. `Core/skills/` is flat in your starter (fine for a dozen skills). As skills (or anything else) accumulate, the natural move is to group by the bucket you actually reach for: verbs ("things I do"), nouns ("things I work with"), whatever the retrieval instinct teaches. The signal to sub-cluster isn't count; it's friction. When you're scanning a long list to find what you reach for daily, the folder is asking to cluster. Place items where you reach for them, not where their description would file them.

### Maps don't freeze what they map

In a learning system, the map shouldn't freeze what it maps. Production systems have files that move toward a finished state (draft → review → locked), and the instinct is to categorize accordingly: what's done, what's in progress, what's stale. But in a thinking system, files don't finish. An early framing doc isn't "stale" because the position evolved; it's the geological layer the current position stands on. A skeletal file isn't "incomplete"; it's a seed that may or may not grow.

So when you write a map of living content (a `CLAUDE.md`, an index, a compass), orient it on **function and relationship**, not status and completeness. What role does each file play? What does it connect to? Where is the current edge of thinking? Those stay true as files evolve. *"This file is 80% done"* goes stale the moment something shifts; *"this file holds the bigger map of what the project is and why"* stays true regardless.

The test: **would this map still orient someone correctly if three files changed tomorrow?** If yes, you mapped function. If no, you mapped state.

---

## Metadata

YAML frontmatter is how the AI searches and finds things without reading every file. It's a structured index at the top of a markdown file. The AI can answer "what's in progress?" or "where did we discuss pricing?" by scanning fields instead of parsing full documents.

**Every field earns its place by enabling a query.** If a field doesn't help you find things, it doesn't need to be there. Your skills generate the right frontmatter for you; see `Core/mechanics/yaml.md` for schemas and conventions.

---

## Naming

What you call things is the last mile of legibility.

Architecture says where it goes. Naming says what it is. Good names teach. `Core/sessions/` tells you these are thinking archives. `Tasks/` tells you these are active. `Library/` tells you this is reference. You don't need a map because the names ARE the map.

**The name's job is to be navigable. The content's job is to teach.** A folder called `skills/` tells you where to look. The skill inside teaches you how it works. Don't overload the name with what the content should carry, and don't rely on the content to do what the name should have already done.

The test: could someone who's never seen this system navigate it by reading folder names alone? If yes, the naming is working.

**Folders are navigation, files are content.** Folders are structural; you click through them to find things. Hyphens, no spaces: `My-Project/`. Files are what you found. Readable titles, spaces preserved: `How we decided on the API design.md`. Two layers serving different purposes. The folder tells you where you are. The file tells you what you found.

---

## The layers

These five build on each other:

- **Local** gives you ownership — your files, your space, any tool
- **Markdown** gives you portability — readable by anything, durable across time
- **Architecture** gives you meaning — arrangement as argument
- **Metadata** gives you queryability — the AI finds things without reading everything
- **Naming** gives you legibility — the last mile of intent

Together: infrastructure for thought. Not storage. Not organization. A medium where the structure of your thinking is yours to shape, yours to evolve, and yours to share with whatever you think with.
