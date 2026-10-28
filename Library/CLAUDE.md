# Library

Your external reference. Podcasts, articles, bookmarks, recipes, whatever you find interesting.

Start dropping things in whenever. Organize by source, by topic, however makes sense to you. The structure will emerge from what you actually save.

**As an example, here's what my library looks like after a year:**

```
Library/
  articles/
  bookmarks/
  books/
  lightning-lessons/
  movies/
  music/
  organizations/
  papers/
  people/
  podcasts/
  recipes/
  tv-shows/  
```

Yours will probably look different. That's the point.

**New here?** `Core/practice/build-library.md` walks the whole loop: capture → connect → see → grow.

## Two things that make it sing

- **`/add`** — the skill that captures things *into* here. Drop a URL (podcast, article, repo, recipe) or a film/show/music/book title and it routes the content, writes the metadata, and builds a people/organization graph from what you save. See `Core/skills/add/`.
- **A view over it** — the files are the catalog, so any tool that reads frontmatter can show you the whole thing: filter by type, category, genre or tag, search, open a person's page to see everything they're in. We use an Obsidian Base: one `Library.base` file at the top of `Library/`, with a table per saved view (people, organizations, movies, a watch-list). Once you've added a few things, ask the AI to write one for your folder (Obsidian's own docs cover the format, and Obsidian rewrites the file when you change a view, so let it own the file after that). Not on Obsidian? A `grep` over the YAML answers the same questions, and the AI can build whatever view suits you.
