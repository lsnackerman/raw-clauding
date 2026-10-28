# /add batch research brief (shared sub-agent briefing)

*Reusable compass for the read-only research agents `/add` fans out during batch reference-hub adds (movies, TV shows, music artists, books). One agent per title. Co-located with the skill as its delegation-memory. Read this fully before researching.*

---

## Why you're here

This library builds **reference hubs**: films, series, artists, and books captured not as content (you can't paste a movie) but as a **verified metadata + creator graph**. The graph IS the product: it's landscape intelligence (who makes what you love: casting pools, studios, labels, publishers) plus honest worldview-resonance. Your job is to research ONE title, web-verify everything, and return a complete drafted entry. **You do NOT write any files.** The orchestrator merges your return into the library and propagates entity pages.

**Accuracy is the entire product.** Verify every name, role, company, date via web search. If you're not sure which title a reused name refers to, or a credit is shaky, **flag it `[low-confidence]`** rather than guessing. A flagged gap is useful; a confident fabrication poisons the graph.

---

## What to return (return-text contract — no file writes)

Return TWO blocks as plain text:

### Block 1 — the complete entry file (ready to write verbatim)

Full YAML frontmatter + body, following the exact convention for the media type (see below). The orchestrator writes this to `Library/{type}/{Title}.md` as-is, so get it right.

### Block 2 — the entity roster (for entity-page propagation)

A clean list of every person and org in the entry, each as:
`- {Name} | {role} | {group: Creative|Studios|Cast (or Members|Producers|Labels, or Author|Publisher|Translator)} | {one-line backlink sentence describing THIS entity's role in THIS title}`

The backlink sentence describes **only this entity's own role**. Never reference another person's role in it (the Edwin/Chris lesson: "bass, with Chris on guitar" mis-tags the bassist as a guitarist). Keep cross-references out of the role clause.

Then the required return-shape fields (§ Required return-shape fields, at the end of this brief), including `## Research flags`: anything `[low-confidence]`, any graph gaps you couldn't fill, any title-disambiguation calls you made.

---

## The canonical-source map (verify the ID — never guess a URL)

| Media | `type:` | Canonical `url:` | Highest-value orgs | "Key crew" | "Cast" |
|---|---|---|---|---|---|
| Film | `movie` | **IMDb** `imdb.com/title/ttXXXXXXX/` | production cos + distributors | director, writer, composer, **DP, editor**, key producers | billed cast |
| Series | `tv-show` | **IMDb** | production cos + networks | creator/showrunner, writers, key producers, composer | billed cast |
| Music | `artist` | **Discogs** `discogs.com/artist/<id>-<Slug>` | **labels** + distributor | producers/engineers | members / key collaborators |
| Book | `book` | **OpenLibrary** `openlibrary.org/works/OLxxxxW` | publisher(s) | translator, illustrator, editor (when present) | — (author is the center) |

For books, also find the **Goodreads** and/or **Wikipedia** URL; those go in the body byline as a secondary cross-ref, NOT in YAML (parallel to MusicBrainz for music).

### ⚠️ The canonical sources BLOCK WebFetch — verify the ID anyway, here's how

**IMDb and Discogs both return HTTP 403 to WebFetch, every time.** MusicBrainz's HTML pages sit behind a browser-verification wall. This is systematic, not intermittent, so the rule above ("verify the ID, never guess a URL") points at pages you structurally cannot open, and that tension makes an agent either guess (banned) or over-hedge (which degrades the entry). Neither is necessary:

| Need | Route that actually works |
|---|---|
| **IMDb tt-id** | Search the title. Search engines index IMDb fine, and the result URL carries the tt-id with the title and year in its page title. Corroborate against **Wikidata** (it stores the IMDb ID as a structured property) or **Letterboxd**, which prints the IMDb ID in its external-links block. |
| **Film/TV credits** | **Wikipedia via `?action=raw`** returns the infobox and full cast cleanly, where the *rendered* fetch often drops the cast list entirely. Then TMDB, Letterboxd, Metacritic's `/credits/` page (unusually complete), and for a studio title the official press site, which gives verbatim actor→character mappings and the full producer block. |
| **Discogs artist ID** | **`api.discogs.com/artists/<id>`** returns name + canonical uri as JSON, no auth, no 403. Or Wikidata, which carries both the Discogs artist ID and the MusicBrainz MBID as structured properties. |
| **Discogs ID when you don't have it yet** | `api.discogs.com/database/search?q=<name>&type=artist` — no auth. The lookup above assumes you already have the ID; this is the step before it. |
| **MusicBrainz MBID** | The web-service API: `musicbrainz.org/ws/2/artist/?query=<name>&fmt=json`. Clean and reliable; the HTML page is not. |
| **Wikidata QID** | ⚠️ **Never guess a QID.** `wikidata.org/w/api.php?action=wbsearchentities&search=<name>&language=en&format=json` resolves it first; *then* fetch claims. A guessed QID returns a **well-formed answer about the wrong person**, and that is silent, plausible corroboration for the wrong artist. |
| **Music credits on a small or independent act** | The band's own **Bandcamp release page**. First-party, doesn't 403, and often the only place a complete engineer/mix/artwork block exists. |

⚠️ **When you fetch with `curl`, send this exact User-Agent: `-A "LibraryResearchBot/1.0"`.** It stops the empty and rate-limited replies some sites give to a bare request. **Never put your human's email, name, or any other identifying detail in a User-Agent or anywhere else in a request**, even when a site's etiquette asks for contact info (`Core/rules/security.md`).

⚠️ **A `?action=raw` fetch under ~500 bytes is a REDIRECT, not an empty article.** It looks like a successful fetch and greps as "no infobox," which is exactly the false negative a bounded search produces, arriving through a mechanism you'd never suspect. Read the `#REDIRECT` target and refetch.

**Say in your flags which route you used.** "tt-id corroborated via Wikidata, credits from Wikipedia raw + TMDB; IMDb page not opened" is an honest and complete verification statement. A reader downstream needs to know whether a cast list is IMDb-billed or press-assembled, because those are different objects. And **write the bound into any negative**: not "no composer," but "no composer *in the Letterboxd and Metacritic credits*", because a bounded search returning nothing reads downstream as a fact about the world.

**Watch the artist-vs-label slug collision on Discogs.** `discogs.com/label/<id>-<Name>` and `discogs.com/artist/<id>-<Name>` can both exist for the same name. You want `artist`.

---

## Convention by media type

### Movies & TV (`type: movie` / `type: tv-show`)

YAML: `type`, `url` (IMDb), `people` (flat array: full **billed** cast + key crew), `organizations` (flat array: production cos + distributors/networks), `date` (release / first-air, `YYYY-MM-DD`), `genre` (controlled array, see vocab below), `tags` (themes / format / watch-context only), `description` (LLM-facing: what it is, honest resonance, landscape note).

Body:
- H1 title + `*Film/Series · {date} · [IMDb](url)*` byline
- `## Why It's In Your Library` — three bolded beats: **What it is.** / **Why it resonates.** (honest; *your own* through-lines, only where genuinely present; say so plainly if thin; never force) / **Landscape.** (the production/casting/distribution intelligence for what you make or curate).
- `## Who's Involved` — grouped **Creative** / **Studios / network** / **Cast**, each line `- **Name** — role`.
- `## Notes` (trailing, can be empty).

Anime/dubbed: include BOTH original + English-dub cast, role-tagged `(Japanese voice)` / `(English dub)`.

**Unscripted (documentary, docuseries, reality, competition, talk).** The convention above is fiction-shaped and breaks in three places; don't improvise per title: "Cast" means people appearing as themselves (host, judges, subjects), role-tagged `— host` / `— herself`, never invented character names. Contestants and one-off participants do NOT enter the graph — hosts and judges only. Expect no composer, DP, or editor credit and flag the gap rather than hunting; EPs and the showrunner carry that weight. A long-running series is one entry, `date:` = the *series* premiere, with era-ranges inline in the role clause (`— judge, series 1–7`).

### Music artists (`type: artist`)

Same reference-hub mode as screen titles, with the mapping from the table above: **labels are the studios, producers and engineers are the key crew, members are the cast, Discogs is IMDb.**

YAML: `type: artist`, `url` (the Discogs artist page; resolve the ID through the API, never guess the slug), `people` (members, or key recurring collaborators for a solo artist, PLUS producers/engineers), `organizations` (labels + distributor + publisher/management *when known*), a **temporal anchor** (`formed: YYYY` for a band, `active_since: YYYY` for a solo artist, because a person isn't "formed"), `genre` (controlled), `tags` (scene / affiliation / theme only), `description` (LLM-facing: what they are, honest resonance, landscape note).

MusicBrainz goes in the **body byline** as a secondary cross-ref, NOT in YAML (parallel to Goodreads for books).

Body:
- H1 artist name + byline: `*Artist · {genre} · Formed {year}, {city} · [Discogs](url) · [MusicBrainz](url)*` for a band; `Active since {year}` for a solo artist.
- `## Why It's In Your Library` — the same three beats as screen titles. Music resonance is usually *thin*, and saying so plainly is the right answer far more often than not. The landscape beat is where the useful intelligence lives: the **label trajectory** (indie → major, imprint-under-parent, self-release), the **producer stable** (who they keep coming back to), the **distribution backbone**, the independence/control model.
- `## Who's Involved` — grouped **Members** (or **Artist** + **Key collaborators** for a solo act) / **Producers & engineers** / **Labels & distribution**, each line `- **Name** — role`. Member status (founding / current / former / touring, with years) goes **inline in the role clause**, never a YAML field.
- `## Discography (studio LPs)` — a table: `| Year | Album | Label | Producer |`. For a deep catalog (past ~15 years or ~8 albums), header it `(selected canonical studio LPs)`, state the selection rule in `## Notes`, and pick one row per label-or-era transition plus the landmarks.
- `## Notes` — flag open graph gaps (management, publisher) rather than fabricating them; announced-but-unreleased albums go here with the date, never in the table.

**Headers are what the propagation script keys on.** A header holding *people* can be whatever the material needs (`Touring lineup`, `Executives`, `Key collaborators`); a header holding **organizations** must contain one of `studio · network · distribut · publisher · label`, or every entity under it is written to `Library/people/`, silently. And **no parenthetical suffix on a header** (`**Cast**`, not `**Cast** (main characters)`): the parser skips the whole group.

Three calls that recur, settled so they aren't re-adjudicated per artist: **the act that isn't a band** (a studio project under a band name with a separately hired touring lineup) gets a hub at `Library/music/{Act}.md` with `formed: YYYY`, the creative core under **Members**, live players under **Touring lineup**, and one sentence in `## Notes` explaining the call. **Solo artists propagate themselves** to `people:` too (list the human under an **Artist** header); bands don't — only their members get person pages. **An artist's own imprint** is both an org in `organizations:` and an extension of the person; list it as an org and explain the relationship in the body. Recurring session players enter the graph; single-album ones don't.

### Books (`type: book`) — WORLDVIEW-PRIMARY

Books invert the movie weighting: the production graph is thin (author + publisher), but worldview-resonance is the real gravity. Lead with it.

YAML: `type: book`, `url` (OpenLibrary work URL), `people` (author + translator/illustrator/editor when present), `organizations` (publisher(s)), `published: YYYY` (first publication year, NOT `date`), `genre` (controlled array, book vocab below), `tags` (themes / format / context), `description` (LLM-facing: what it is, worldview-resonance FIRST, light adaptation/cultural-footprint note).

Body:
- H1 title + `*Book · {author} · {published} · [Open Library](url)*` byline (add Goodreads/Wikipedia as `· [Goodreads](url)` secondary links).
- `## Why It's In Your Library` — beats: **What it is.** / **Why it resonates.** (LEADS, because books are often chosen for this; *your own* through-lines, honestly) / **Cultural footprint.** (lighter: adaptation history, influence, where it sits in the canon).
- `## Who's Involved` — grouped **Author** / **Publisher** / (**Translator / Illustrator / Editor** when present), each line `- **Name** — role`.
- `## Notes`.

**Books org rule:** publishers do NOT need to feel like the gravity, but still list them. (The orchestrator decides propagation; you just supply the verified publisher.)

---

## Your through-lines (for honest resonance — do not force)

The "why it resonates" beat is anchored in **your own** through-lines, the handful of themes, values, or questions that make something *yours* (a worldview, an aesthetic, a craft you're studying, a thread you keep circling; whatever they genuinely are for you).

If the orchestrator handed you a specific set of through-lines to check against, use those. Otherwise infer them from the library's existing entries (read a few `## Why It's In Your Library` sections to see the throughlines).

Name the specific thread where it's **genuinely present**. If it isn't, **say the resonance is thin and don't manufacture it**; honesty is the standard. A title in the library for craft or casting-pool value, not resonance, should say so plainly.

---

## Genre vocab (controlled — `genre:` field)

**Film/TV:** `action adventure comedy dark-comedy crime thriller neo-noir horror survival-horror drama comedy-drama dramedy sci-fi science-fantasy fantasy animation anime adult-animation satire superhero supernatural mystery sitcom biographical` (+ subgenre flavor as needed).

**Books:** `science-fiction speculative-fiction literary-fiction philosophy non-fiction feminist-fiction short-stories fantasy horror dystopian first-contact hard-sci-fi social-sci-fi memoir essay` (+ flavor as needed).

Themes / format / period / watch-context stay in `tags:` (`anthology-series`, `1990s-period`, `rewatch`, `apple-tv-plus`, `trilogy`, `ancient-aliens`), NOT `genre:`.

---

## Required return-shape fields (not optional, not a footer)

These are **part of the return contract**, same as Blocks 1 and 2. They're in the shape on purpose: a field left in prose guidance tends not to get filled.

- **`⚠️ PREMISE CHECK`** — put this FIRST if the premise you were handed was wrong (wrong country, wrong network, wrong medium, a title that doesn't exist, a fabricated detail). A wrong-identity finding is a different class from a shaky credit and must not be buried in flags. *A hedged premise ("believed to be…") is an anchor, not a fact. An agent that finds partial corroboration can confirm-bias its way into the wrong entry. Treat every premise as a claim to falsify, not a field to fill.* If the premise held, omit this line.
- **`## Research flags`** — `[low-confidence]` items, gaps you left open, disambiguation reasoning + confidence, and which verification route you used. **A `[low-confidence]` credit is OMITTED from Block 1 and named here, never inlined into `people:`/`organizations:`.** Block 1 gets written to the library verbatim, so a marker inside it ships; and a shaky name in those arrays mints a real entity page. **Prefer a flagged gap over a fabricated edge.**
- **`🎈 WHAT PULLED AT ME`** — what the title held that these boxes had no place for: anything that surprised you, any disambiguation that was tricky, anything the orchestrator should watch for when merging.
- **`📋 WHAT I'D CHANGE ABOUT THIS BRIEF`** — what did you need and not get · what did this brief tell you that turned out wrong · what would you want if you were the next agent sent here. **This is the only channel through which a bad brief can report itself**, so it is not a courtesy field.

---

## Before you finalize — two cheap reads

1. **Skim `Library/_tags.md`** (if it exists) and 2–3 sibling entries in your media folder. The orchestrator reconciles tags, but knowing the house register converts "propose loosely, someone fixes it" into "propose correctly."
2. **`ls Library/people/` AND `ls Library/organizations/` for near-matches on every entity you're returning, and flag collisions.** The org side is arguably *more* collision-prone, because label lineages rebrand, merge, and get spun out constantly: a library can legitimately hold two pages for two eras of one label, and an agent picking one at random half-orphans a real distinction. **Distinguish the two outcomes explicitly, because they need opposite handling:** a same-name-**same-person** hit is the cross-medium graph *working* → say **APPEND**; a same-name-**different-person** hit is a hazard that will silently corrupt the graph → say **⚠️ COLLISION, different person**. The roster line looks identical either way unless you mark it. Fuzzy resolution can also route a new name into an existing unrelated page (a bare surname against several `*-Surname.md` pages), so look before you return. **Reading the library is always fine; "no file writes" means don't write, not don't look.**
