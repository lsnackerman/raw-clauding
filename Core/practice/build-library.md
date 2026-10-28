# Build your library — capture, connect, see

Your `Library/` isn't a folder of bookmarks; it's a graph that grows with you. Every podcast, article, film, or person you add quietly wires itself into a web you can search, filter, and look across. This is the rhythm for growing it, and how the pieces fit together. (Mechanics live in the docs this points at; here's the *loop*.)

## The loop

1. **Capture** — drop a URL or a title into the conversation and run `/add` (or park it in `Library/ADD.md` for later). The skill pulls the content, writes the metadata, and files it.
2. **It connects itself** — when you add something, the people and organizations in it become their own pages, each one backlinking to everything they appear in. Add three podcasts with the same guest and that guest's page now shows all three. You didn't build the connection; capturing did.
3. **See it** — the files are the catalog, so any tool that reads frontmatter gives you a view over the whole graph: filter by type, category, genre, tag; search; open a person's page to see everything they're in. We use an Obsidian Base over `Library/` (`Library/CLAUDE.md` says how); a plain `grep` works too.
4. **Grow** — the structure emerges from what you actually save. No need to plan folders up front; they appear when the first thing that belongs in them does.

## The moves that make it compound

- **Capture freely, process later.** `ADD.md` is a no-pressure queue. Drop links as you find them, run `/add` on them when you have a minute. Lowering the friction of capture is what makes the library *real* instead of aspirational.
- **Let structure emerge, with its own signpost.** Don't pre-build empty folders. When `/add` makes a folder for the first time (your first podcast → `podcasts/`), it leaves a one-line note in it saying what lives there. The library's shape becomes a record of what *you* collect, each room labeled as it's built.
- **Repos come in whole, and stay read-only.** `/add` with a GitHub URL clones the whole repo into `ARCHIVE-OS/Library/repos/`, beside your system rather than inside it, so you can think alongside someone else's system: their framework, their docs, code you're learning from. (Outside, because a repo's own `CLAUDE.md` files and skills could otherwise load as yours: `Core/mechanics/archiving.md`.) Then point the AI straight at it: *"Read the README in `ARCHIVE-OS/Library/repos/{repo-name}/` and tell me what jumps out for our setup."* Treat what lands there as reference rather than something to edit; if you want to extend or remix it, fork to your own working space so the original stays a clean copy of theirs.
- **Three controlled fields, then open tags.** `type` (which folder), `category` (what a person/org *is or does*: director, author, instructor, even client/friend), and `genre` (story-kind) are *controlled*, meaning small, known vocabularies you query as a whole ("all directors", "all sci-fi"). `tags` are open, emergent themes. The rule of thumb: **if you'd want to query the whole set, it's a field; if it's just a loose theme, it's a tag.**
- **Reuse your tag vocabulary.** As your library grows, run `python3 Core/skills/add/build-tag-vocab.py` to regenerate `Library/_tags.md`, your living list of tags, and skim it before minting a new one. Folding into an existing tag instead of coining a near-duplicate is what keeps the library searchable instead of sprawling.

## The payoff

The graph *is* the point. Once you've added enough, your library answers questions a folder of files never could: who keeps showing up across the things you love, which studios or labels or publishers make the work that resonates, what you've collected on a theme. It doubles as a lightweight CRM. Look a person *up* and see everything connecting you to them. The more you add, the more it connects; the connecting is automatic.

## Where the pieces live

- **`/add`** — capture + routing + the entity graph → `Core/skills/add/`
- **`Library/ADD.md`** — your capture queue
- **`Library/CLAUDE.md`** — the top-level orientation for the space

*Starter shape. Keep what helps, and let your own rhythm for collecting take over.*
