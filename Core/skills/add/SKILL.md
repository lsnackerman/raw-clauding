---
name: add
description: Add content to your personal library. URLs, local PDFs, podcasts, articles, recipes, repos, bookmarks, and reference hubs (films, shows, music, books). One skill — Claude detects the type and routes.
argument-hint: [URL or file path] [optional: why you're adding it]
---

# /add — Build your library

Add URLs or local files as organized markdown. Claude detects the content type and routes it to the right place.

```
/add https://somenewsletter.com/p/the-article
/add https://youtube.com/watch?v=xyz for the framework it teaches
/add https://github.com/org/repo as bookmark
/add /path/to/paper.pdf
/add The Fifth Element        ← a film → a reference hub
```

---

## Three modes

| Mode | What it does | When |
|------|--------------|------|
| **Content** | Full extraction to markdown | Podcasts, articles, recipes |
| **Asset** | Clone / download the file | Repos, PDFs |
| **Bookmark** | Light capture (remember the link + why) | "Save for later" energy |

Claude detects from the URL. You can override: `/add [url] as bookmark`.

A fourth shape, **reference hubs** (films, shows, music, books), has no body to extract; the entry *is* a metadata + creator graph. See § Reference hubs.

---

## What to do

1. **Parse the request** — URL, any note ("for…", "because…", "re:…"), explicit mode override ("as bookmark"), project tag ("for {project}").
2. **Normalize the URL** — strip tracking params (`utm_*`, `ref`, `fbclid`, `gclid`, `source`, `mc_*`…); `http`→`https`; drop `www.`, trailing slashes, `#fragments`.
3. **Check for duplicates** — search `Library/` for an existing file with the matching normalized URL. If found, say so and offer to open it.
4. **Detect the content type** (table below) and route to the handler.
5. **Self-verify** before saving.

### Detection

| URL pattern | Type | Mode |
|-------------|------|------|
| youtube.com, youtu.be | podcast | **`yt-dlp`** pulls it (paste = fallback) |
| spotify/episode, apple podcasts | podcast | scaffold + paste |
| substack, medium, newsletters, blogs | article | full capture |
| recipe sites | recipe | full capture |
| x.com/*/status (short) | bookmark | scaffold + paste |
| x.com long-form article | article | scaffold + paste |
| github.com, gitlab.com | repo | asset (clone) |
| `.pdf` | pdf | asset |
| a film or show title (or imdb/letterboxd URL) | movie / tv-show | reference hub |
| a musician/band (or discogs URL) | artist | reference hub |
| a book ("{Title} by {Author}", openlibrary/goodreads) | book | reference hub |
| anything else | bookmark | light capture |

---

## Content capture (articles, recipes)

1. **Fetch.** Try WebFetch first. If it truncates (long pieces), returns a structured summary instead of the text (some sites trigger a copyright posture), or the page is JS-rendered, escalate (a headless-browser fetch, or scaffold+paste). A paywall that returns only the first paragraphs is the same case: mark the shell **PARTIAL/paywalled**, ask for a paste of what the reader can access, keep a capture-fidelity note. **If you couldn't get verbatim text, say so in a capture note**, because the next reader needs to know what fidelity layer was preserved.

   **🚫 NEVER save a blocked or failed fetch AS the article.** When a site bot-walls WebFetch, it returns the *block page*, and the naive move saves that as the capture: the block string becomes the H1 **and the filename**, and its body becomes the "content." **Recognize it by the tells** in the returned title or body: `Just a moment...` · `Verify you are human` · `needs to review the security of your connection` · `JavaScript is not available.` · `Enable JavaScript and cookies` · `Security Review Required` · `403: Forbidden` · `Could not fetch URL content` · `Could not extract content from …`. If the *title* looks like any of those, the fetch failed, full stop. Don't write a normal article; fall back to scaffold+paste (build the shell from the real URL and title you know, ask for the text) or write a clearly marked `⚠️ needs-paste` shell. **Why it matters beyond ugliness: generic block-page titles collide** (`JavaScript is not available..md` for any two blocked captures), so a second capture silently overwrites the first and a later rename orphans the entity backlinks. Also strip fetch-wrapper cruft (`Title:` / `URL Source:` / `Markdown Content:` / `Published Time:`) from any saved body, since the canonical link lives in the `url:` field. A re-runnable sweep for existing contamination: `grep -rl "Just a moment\|Verify you are human\|JavaScript is not available\|Could not fetch\|Could not extract\|403: Forbidden\|Security Review Required" Library/ --include="*.md"`
2. **Extract** title, author, source, date, body.
3. **Generate YAML** (schema below) and **format** the body as clean markdown (faithful, not summarized).
4. **Write** to `Library/{type}/` (flat), or `Library/{type}/{Source}/` once a second item from the same source arrives.

### Entry body — where YOUR reading goes

**These types differ from the reference hubs below in one structural way: the body is the *source's* words, not yours.** A film entry *is* your note. An article or podcast entry is a container for someone else's prose, so your own reading has nowhere to go by default, and it tends to get packed into `description`, which is a queryable index rather than storage.

**Put it in a `## Why It's In Your Library` section at the top of the body, above the source text.** Keep `description` to one line.

**Write one when there's a real reason; skip it when there isn't.** That's the difference from the hubs, where the section *is* the entry. A link you grabbed because it looked interesting doesn't need a paragraph saying so.

- **Why you grabbed it** — in your own words. *"A friend mentioned this"* is a complete reason; don't inflate it into something more analytical than you meant.
- **What to do with it** — absorb, or **read against**. Keeping something because you *disagree* with it is a real reason, and it's invisible from the source text alone: without this line, a later reader takes the disagreement for an endorsement.
- **What it connects to** — a thread, a person, a project you're working on.
- **Honest resonance, where it's actually there** — same standard as the hubs: name what lands **and** what doesn't. *"Thin; this is here for the disagreement"* is a complete entry. **Forcing a connection is worse than recording none**; a library where everything resonates is one where the word stops telling you anything.

### YouTube / podcasts — published transcript if there is one, then `yt-dlp`, then scaffold + paste

**First, check whether the publisher already posts a transcript.** Many shows do (a link in the video description, a transcript page on the show's site, a newsletter post that carries the episode). When it exists it's the *best* source, not a workaround: human-edited, punctuated, speaker-labeled (everything auto-captions aren't), and WebFetch can read it with nothing installed. It's also the only route for Spotify and Apple Podcasts, which have no caption track to pull. Grab it, keep the URL in the capture, and skip the rest of this section.

Otherwise: WebFetch can't pull YouTube captions or descriptions. **`yt-dlp` can, and it pulls everything: captions, description, duration, upload date. Try it next; paste is the fallback, not the default.** Nobody should be copying a transcript out of a browser when one command does it.

**If `yt-dlp` isn't installed** (`which yt-dlp` returns nothing), install it once with pip (`python3 -m pip install -U "yt-dlp[default]"`) and confirm with the user before installing (it's their machine). One-time setup; every future capture is free.

⚠️ **Check `python3 --version` first. `yt-dlp` needs Python 3.10 or newer, and the Python inside Apple's command line tools is 3.9.** If that's what you have, pip will either refuse or **quietly install an old build** (the last one that still supports 3.9; it works today and can't keep up with YouTube). Install the newer Python first: the official installer from python.org (the Python step in `Core/mechanics/setup-mac.md` walks it). One signed download, one admin password, and it sits alongside Apple's without replacing it. That's the Python this system runs on. After installing, quit the Claude app completely (⌘Q) and reopen it, or open a new terminal if you're working in one, so `python3` points at the new one; then run the pip line above again, because helpers install per-Python and the new one starts empty. The `[default]` in the pip line matters: it brings the certificates yt-dlp needs for HTTPS, so yt-dlp works even if the installer's "Install Certificates" step got skipped, but do run that step (the setup guide says so); plain Python can't fetch anything over HTTPS without it.

**If `yt-dlp` works in the user's terminal but YOUR shell says "not found":** the python.org installer adds its folder to the PATH by editing `~/.zprofile`, which **only a login shell reads**, and your shell doesn't re-read it per command. It replays the PATH it inherited when this session started, so an app that was open *before* the install is still handing you the old one. *(Measured: `env -i zsh -c 'which yt-dlp'` → not found; `env -i zsh -lc` → found.)*

**Escalate in this order, the cheap step first:**
1. **Fully quit the app (⌘Q, not just the window) and reopen.** This is the step `Core/mechanics/setup-mac.md` gives at its Check Python step; match it. ⚠️ **Unverified that it's enough in the Claude desktop app:** its docs say that on macOS it reads the PATH from your shell profile (such as `~/.zshrc`) at launch, and the python.org installer writes to `~/.zprofile`, so if a reopen doesn't do it, step 3 isn't a stopgap, it's the answer.
2. **If you're running Claude Code in a terminal instead:** open a new terminal, then re-run `claude`. Each new terminal starts a login shell, so it picks up the new Python whatever the app inherited.
3. **Keep going in this session** by prefixing each call with `source ~/.zprofile && `, or by calling the binary at its full path: **`/Library/Frameworks/Python.framework/Versions/Current/bin/yt-dlp`**. ⚠️ **Do NOT build that path from `python3 --version`.** In the very shell that has this problem, `python3` is Apple's 3.9, so you'd construct a `Versions/3.9/` path that doesn't exist and hand the user a second failure. `Current` is a symlink the installer maintains; if you want to see what's really there, `ls /Library/Frameworks/Python.framework/Versions/*/bin/yt-dlp`. Say which workaround you're using, so the extra words aren't a surprise.

**One more case, and it looks like success: pip prints `Successfully installed yt-dlp` and `which yt-dlp` is still empty.** When the target Python's folder isn't writable, pip says *"Defaulting to user installation because normal site-packages is not writeable"* and installs to `~/Library/Python/3.x/bin/`, which is on no PATH at all. **That is not a failed install and re-running it won't help.** Look in `~/Library/Python/*/bin/yt-dlp` and call it there, or install against the python.org Python instead.

**On WSL / Ubuntu** (the non-Mac path), Python is already 3.12 but `pip install` is blocked outside a sandbox (the `externally-managed-environment` wall the setup guide mentions). Use pipx instead: `sudo apt install -y pipx && pipx install "yt-dlp[default]"`, then open a new terminal. **Confirm with the user before running this one, because it starts with `sudo` and will ask for their password.** *(The user-space pip line above already asks for confirmation; this is the command that needs it more.)* Same commands from there on.

**If a pull fails later, update first, then retry** (`python3 -m pip install -U "yt-dlp[default]"`, or `pipx upgrade yt-dlp` on Ubuntu). YouTube changes every few weeks, and `yt-dlp -U` refuses on a pip install.

**Run all three, every time**, from a scratch folder (the subtitle files land as files; don't litter the library):

```bash
yt-dlp --no-update --skip-download --write-auto-subs --write-subs \
  --sub-langs "en.*" --sub-format vtt -o "%(id)s.%(ext)s" "URL"
yt-dlp --no-update --skip-download \
  --print "%(title)s|||%(channel)s|||%(duration_string)s|||%(upload_date)s" "URL"
yt-dlp --no-update --skip-download --print "%(description)s" "URL"
```

- **The description is a default step, not an optional extra.** It carries things "Show transcript" never gives you: **chapter markers** (the creator's own arc; use them as your section headings), **channel-transcribed pull-quotes** (these *are* quote-grade, unlike auto-captions), and any glossary/links block. When a video has none, the call costs nothing.
- **The captions need de-duplicating; use the bundled tool, don't hand-roll it:** `python3 Core/skills/add/yt-captions.py IN.vtt OUT.txt --prose` (paragraphs) or `--stamped` (`N<TAB>[H:MM:SS]<TAB>text` per cue, when you'll want timestamps later). Auto-caption VTTs are *rolling* (each cue repeats the prior line plus new words, with inline per-word timing tags), so a naive tag-strip yields every line about three times.
- **Warnings that are noise, not failure**: `No supported JavaScript runtime` and `SABR streaming` / missing-format lines still return subtitles fine. Genuine failure looks like *no* `Writing video subtitles to:` line.
- **Auto-captions are not quote-grade**: no speaker labels, no punctuation, and proper nouns get mangled. Save them as-captured and note that in the capture; the video stays the ground truth. Fix a garbled name when you spot one (what the captioner *heard wrong*, never what the speaker said). (Manual/broadcast caption tracks are a different class: real punctuation and `>>` speaker-change markers. If the output reads like a script, it roughly is one.)

Then: fill the YAML from the metadata line (the channel or the show's brand goes in `organizations:`, not a name parsed from the title; complex titles fool pattern-matching), write the description under `## Description`, the de-duplicated captions under `## Transcript`, and save.

**Fallback — scaffold + paste** (when `yt-dlp` genuinely fails, captions are disabled on the video, or the source is Spotify / Apple Podcasts, which have no caption track to pull): create the shell immediately (YAML with `video_id`, `url`, `date_added`, title + placeholder Description/Transcript sections), then ask the user to paste: **channel name · duration · the "…more" description · the transcript**. Format and save when they paste. Title + channel for a YouTube URL can still be pulled without a paste: `curl -s "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=VIDEO_ID&format=json"`.

### X / Twitter — scaffold + paste
X blocks automated access. Create the shell, ask the user to paste the content. Short posts → `Library/bookmarks/`; long-form articles → `Library/articles/X/`. Include the author handle as `**Name (@handle)**` under the H1.

---

## Asset capture

**Repos** → clone into **`ARCHIVE-OS/Library/repos/{repo-name}/`, in the ARCHIVE-OS folder beside this system**, never inside it (the codebase *is* the artifact; its README carries the metadata). **Why outside:** a repo often ships its author's `CLAUDE.md` files and a `.claude/skills/` folder, and Claude Code loads those as *your human's* instructions and skills the moment you read a file in it inside this system. No setting can stop the skills; outside the system folder, nothing loads. If ARCHIVE-OS doesn't exist yet, it's a peer of this folder (`Core/mechanics/archiving.md` § The three OS pattern): say where you'll create it and ask first, since it's outside the folder (`Core/rules/security.md`). Add an entry to `ARCHIVE-OS/Library/repos/INDEX.md` (create it with the first repo). Bookmark-only if the user says so or the repo is private.

**PDFs** → folder per paper in `Library/papers/{Title}/` (proper-title, spaces); move+rename the PDF in; extract to markdown; prepend paper YAML; propagate authors to `Library/people/`.

---

## Reference hubs — films · shows · music · books

A different mode: **there's no body to extract** (you can't paste a movie). The entry is a *reference hub*, a verified **metadata + creator graph**. The graph IS the product: it's **landscape intelligence for whatever you make or curate** (who makes the things you love: casting pools, studios, labels, publishers, collaborators) plus an honest note on why it's *yours*. Center of gravity is **connection**, not content.

### Where it lands
Flat file, proper-title with spaces: `Library/movies/{Title}.md` (`type: movie`) · `Library/tv-shows/` (`type: tv-show`) · `Library/music/{Artist}.md` (`type: artist`) · `Library/books/{Title}.md` (`type: book`). No source subfolders; the people/org graph does the grouping. Strip filesystem-unsafe chars (`: * ? " < > | / \`) from filenames.

### Canonical source — verify the ID, never guess
| Media | `type:` | Canonical `url:` | Highest-value orgs | "Key crew" |
|---|---|---|---|---|
| Film | `movie` | **IMDb** `imdb.com/title/ttXXXXXXX/` | production cos + distributors | director, writer, composer, **DP, editor**, key producers |
| Series | `tv-show` | **IMDb** | production cos + networks | creator/showrunner, writers, key producers, composer |
| Music | `artist` | **Discogs** `discogs.com/artist/<id>-<Slug>` | **labels** + distributor | producers / engineers |
| Book | `book` | **Open Library** `openlibrary.org/works/OLxxxxW` | publisher(s) | translator / illustrator / editor (when present) |

Temporal anchor: `date:` (release/first-air) for screen · `formed:`/`active_since:` for music · `published:` for books.

### Who propagates (the graph is the point)
- **`people:`** — full **billed** cast + key crew (capture-complete on billed cast, since you can't grep what you didn't capture; the line is *billed*, not every walk-on). Music: members (or a solo artist's key collaborators) + producers/engineers; a **solo artist also propagates themselves** to `people/` (the human is a person; a band doesn't, because a band isn't a person). Books: author + translator/illustrator/editor.
- **`organizations:`** — production cos + distributors/networks (screen), labels + distributor (music), publishers (books). **Screen + music + book orgs propagate at add-time** (the studio/label/publisher graph is the whole point), unlike the organic org stage for other content.
- Entities land in the shared `Library/people/` + `Library/organizations/` space, and a cross-medium graph is a feature (a composer who also scores a film links both).

### Entry body
Flat YAML holds names only, so the **body holds the role-map**:
- H1 + a byline line with the canonical link.
- `## Why It's In Your Library` — three honest beats: **What it is.** / **Why it resonates** (*your* throughline, the thread that makes it yours; name it specifically where it's genuinely present, and **say plainly when it's thin**; don't manufacture resonance) / **Landscape note** (the production/casting/label intelligence for what you make or curate).
- `## Who's Involved` — grouped **Creative / Studios·label·network / Cast** (or Members/Producers/Labels; Author/Publisher/Translator), each line `- **Name** — role`.
- `## Notes`.

> The "why it resonates" beat is **yours to define**, your own worldview and through-lines, not a prescribed set. The discipline is *honesty*: name the real thread where it's present, and admit when a title is in your library for craft or landscape value rather than resonance.

### `category:`, `genre:`, and `tags:` — controlled indices vs open themes
Three fields, two jobs. The discriminator: **can you enumerate the whole vocabulary and query the whole set?** ("all directors", "all sci-fi") → a controlled field. Emergent, pull-what-resonates → a tag.
- **`genre:`** on title hubs — controlled story-kind terms (`comedy`, `thriller`, `sci-fi`, `documentary`, `synth-pop`, `literary-fiction`…), split out of `tags:`. Substring grep gives broad + specific.
- **`category:`** on entity pages (person / org) — controlled index of what an entity *is or does* across the library. Two families: production credits (`actor`, `director`, `composer`, `guitarist`, `producer`, `author`, `studio`, `label`, `publisher`…) AND, for people, what they are *to you* (`student`, `client`, `peer`, `friend`, `instructor`). Lets you query "all drummers" / "all labels" / "all clients". Add only when non-empty. *(Directionality: a page carries only what describes* that *person; `student` goes on your students' pages, never on someone you're a student of.)* `type:` stays the clean folder bucket; the kind-of-entity refinement lives here in `category`.
- **`tags:`** = open, emergent themes (`anthology-series`, `1990s-period`, a streamer, a city). Backlog tags on aspirational items, dropped when consumed. **Never duplicate a controlled field as a tag.** Four leaks to refuse: the **type/category name** itself (no `recipe` tag on a `type: recipe`), an **entity name** (people/orgs go in `people:`/`organizations:`), **abstract virtue-words** (`resonance`, `curiosity`; they find nothing), and **mood words** (`feel-good`). Reuse before you mint; fold to the broad theme; don't sprawl. *(As your library grows, run `python3 Core/skills/add/build-tag-vocab.py` to regenerate `Library/_tags.md`, your living tag vocabulary, and skim it before minting a new tag.)*

### Batch adds (many titles at once)
Fan out research (**one sub-agent per title → a web-verified structured graph, NO file writes**), then a **serial merge** (dedup entities across the batch + against existing, create/append, propagate). Accuracy is the whole product: verify every name/role/company via web search; flag low-confidence rather than guessing. The shared sub-agent brief lives co-located at `research-brief.md`.

---

## YAML schema

**Universal fields** (all content types):
```yaml
---
type: podcast|article|recipe|bookmark|paper|movie|tv-show|artist|book
url: "https://…"
people: ["Author Name"]              # plain names, no role distinction in YAML
organizations: ["Show / Publication / Channel"]   # the source of the content is an org, so it gets a page and backlinks; optional otherwise
projects: ["project-slug"]           # optional — projects this feeds
date: 2026-01-15                     # when the content was created
date_added: 2026-01-20               # when you added it
tags: ["theme", "topic"]             # topics/themes only (pull, don't push)
description: "LLM-facing ONE-LINER: what this is. Your note goes in the body — § Entry body"
---
```
Title is **never** in YAML; the H1 + filename are the title. Every field earns its place by enabling a query; if your folder structure already encodes it, don't duplicate, and if nothing will keep it true, don't add it. Arrays use block-list format. Bookmarks are lighter: `type: bookmark`, `url`, `date_added`, `note`, `tags` (+ optional `people` when the bookmark is *about* someone's work).

---

## Entity propagation

After writing the content file, update entity pages for everyone in `people:` (and `organizations:` where they propagate). **Primary creators only, not cited references.** `people:` is who the content is *from* (authors, hosts, cast, crew), not everyone it mentions. Cited figures live in the body, not `people:` (else the graph bloats with bare one-mention pages).

Each person page: create `Library/people/{First-Last}.md` if new (hyphenated filename, spaces in the `name:`/H1), else append a backlink under `## In My Library`. "Why I'm Curious" is added later, when the interest is real.

### The propagation scripts + the backscan
Three sister scripts in this skill's folder automate the above (run from your OS root):

- **`propagate-entities.py`** — for reference HUBS (movie/tv/music/book). Parses the `## Who's Involved` body → propagates cast + key crew + orgs.
  `python3 Core/skills/add/propagate-entities.py "Library/movies/Some Film.md" ...`
- **`propagate-content-entities.py`** — for FLAT captures (article/podcast/bookmark/recipe/paper). Propagates from the YAML `people:` / `organizations:` arrays.

Both are **idempotent + additive** (re-running fills any missing backlink/page, so re-propagation *is* the symmetry repair) and share a hardened `resolve_entity_path` that **normalize-matches** existing pages (folds diacritics + space/hyphen, but keeps meaningful `+` so `AMC` ≠ `AMC+`), so a variant spelling appends to the existing page instead of spawning a duplicate.

- **`entity-backscan.py`** — when a propagation reports pages as `created`, a new entity just entered the graph and may already be *mentioned* in titles you hold without being credited (e.g. an actor with a page from one film, named in another film's cast prose without being in its cast). Run it on the new names:
  `python3 Core/skills/add/entity-backscan.py "New Name" ...`
  It returns a **review list, not an auto-fix**, because a text match can't tell a real cameo from a cited-reference, a deliberate scope-out, or a character-name collision, so you pick which to wire (add to YAML + Who's-Involved → re-propagate). One name = almost no noise.

### Organizations
Org pages come in **organically** for most content (alongside the `organizations:` field, when an org is a substantive subject), except **screen/music/book hubs**, where the studio/label/publisher graph propagates at add-time. **Non-media orgs** (tools · services · places you relate to by *use*, not content-production: a SaaS in your stack, a vet/rehab place, a shop) take a different shape: a `## What it is` + practical fields (e.g. `## Where` + a maps link for a place), with the **nature in `category:`** (`restaurant`, `tool`, `service`, `shop`…; controlled vocab, same field media orgs use for `studio`/`label`, *not* a tag). The gate is **connection, not payment**; mint when it links to content / a project / a person / a place (even an aspirational someday-option counts).

---

## File naming

- **Folders are navigation, files are content.** Source/category folders → hyphenated (`Some-Newsletter/`); single-item folders (a paper) → proper-title matching the file inside. Files → readable, spaces preserved, strip unsafe chars, truncate ~80 chars at a word boundary, **unless truncating cuts meaning, then keep the full title.** The 80-char rule exists to stop unwieldy names, not to amputate claims; academic papers are the recurring case (a 92-char title that truncates to *"…restores human beliefs"* has lost *"and values"*, half of what the paper argues). **The test: read the truncated version and ask whether it still says what the thing says.** If not, keep it whole and move on; the filesystem allows 255.
- **CAPS files are navigation** (`README.md`, `CLAUDE.md`); everything else lowercase.
- **Single items stay flat**; create a source subfolder only when a second item from that source arrives.
- **Let folders emerge with their own compass.** Don't pre-create empty type folders. When you create one for the first time (first podcast → `podcasts/`), drop a one-line `CLAUDE.md` in it noting what lives there + any convention you just followed, so the folder is born with its signpost and the next session (or the next AI) opens it and it explains itself. Structure emerges from what's actually saved, each room labeled as it's built.

---

## Project tagging

`projects:` is an optional array of project slugs the content feeds, enabling a bidirectional view: the item knows what it fed; from the project side, `grep 'projects:.*{slug}' Library/` returns the set. Populate from the user's note, or ask once at capture; otherwise omit and tag lazily later. Don't auto-infer a project from content; let the user decide what their work connects to.

---

## Self-verification

Before saving: **not a block page** (is the H1 or filename `Just a moment`, `JavaScript is not available.`, `Security Review Required`, `Could not fetch`, `403`? then the fetch failed; scaffold+paste instead)? · source folder right? · everyone relevant in `people:`? · description is a one-liner (your note belongs in the body, § Entry body)? · tags resonate (not filler)? · URL normalized? · for hubs, did entity propagation run (and a backscan on any newly-created names)?

---

## Skill Check

After each add, a quick scan: anything that felt off, such as a schema field you wished you had, a wrong detection route, a new content type not covered, something the user had to correct? If yes, update this skill now; the improvement compounds (learn from actual use, not upfront design). If no, move on.
