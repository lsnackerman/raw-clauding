# Files

Operational patterns for file work. Depth lives in `Core/mechanics/` (yaml, markdown, symlinks, archiving, file-recovery). The philosophy behind the file-shape convention lives at `Core/foundations/file-philosophy.md`.

---

## The three file shapes

- **`AGENTS.md`** — at the root, **one per system**. Tool-agnostic compass, so any agent (Claude Code, Cursor, future tools) reads it. "Who we are, what this is."
- **`CLAUDE.md`** — in subdirs, **as deep as useful**. Folder-level orientation. Auto-loads when Claude Code reads files in that folder. "What's here, where to go next."
- **`README.md`** — for **distribution artifacts only** (public repos, packages shipped to others). Universal convention; every tool renders it.

**The convention**: `AGENTS.md` at root, `CLAUDE.md` trails everywhere else, `README.md` only when shipping outward.

**Default: CLAUDE.md solo** in subdirs. Auto-loads, serves both audiences, no sync drift.

**Subfolder READMEs in distribution artifacts: GitHub-browse-before-clone is the test.** If the artifact ships via GitHub (people browse the repo before cloning), a subfolder README earns its place, because someone navigating from the landing page sees it. If it ships via zip or any "you already have all the files" path, that justification dissolves: `CLAUDE.md` wins everywhere except package-root, because no one browses subfolders before unzipping.

**If you land in a folder that should have a CLAUDE.md but doesn't, flag it.**

---

## Keep every CLAUDE.md a lean pointer, not a record

A `CLAUDE.md` auto-loads on **every** touch of its folder, so its weight is paid on every read. One that swells into a holding container (a full blow-by-blow, a record that should stand alone) taxes every fresh instance's context whether they needed it or not. Hold the substance in a **named file beside it** and let the CLAUDE.md *point*: who/what's here + where to go.

Two tells. **It reads like a record, not a directory.** And for the lines that pass that test (accurate, adjacent, *interesting*, but garnish), ask **does this change how I work here, or is it just true?** If it's just true, it belongs at its reach-moment, not on a surface that charges every session for it. Meat and potatoes, not the rest of the menu.

**And the cost isn't only context. It's belief.** Everything in a doc you opened *for one reason* becomes background you never vetted. A fat surface doesn't just tax attention; it **seeds premises**, and an inherited premise doesn't feel crisp, it feels *remembered*, so nothing prompts you to check it. The practical substitute is a **provenance** check: did this come from the thing, or from a description of the thing?

The default is a default, not a cage: a folder that is a **destination** rather than a thoroughfare (a project you sit down inside, not one you pass through) can legitimately hold its record in its `CLAUDE.md`, because the record is what you want on that load. The auto-load tax governs *pass-through* folders. (`Core/rules/pointing-vs-holding.md` at the auto-load layer.)

---

## Move, don't recreate

When reorganizing, move the original file. Don't read it and rewrite it somewhere new.

Recreating introduces silent errors: wrong formatting, lost metadata, broken links. But more than that: the file IS the thought. A copy is an approximation. Move the original, rename at the destination, update references.

Match the size of the action to the size of the change. Deleting a file and rewriting it when you could have changed two words is structural noise.

---

## Prune, don't lose texture

Before any prune/park/delete/remove move, scan for texture that exists only in what's being removed. Decisions, options explored, reasoning, open questions: these often live in the thing being pruned because they weren't captured elsewhere.

Capture them first. Then prune.

The test: before you prune, ask "what exists only here that future-us will want when this comes back?" If the answer is nothing, prune freely. If something surfaces, capture first.

**And sometimes the thing itself is texture.** Extracting contents isn't always enough. The composition, sequencing, and shape of a substantial artifact can be its own evidence. Before removing something that was composed and re-composed over time, ask not just "what's inside that won't survive?" but "is the artifact itself worth preserving as a snapshot?" If yes, archive the whole thing verbatim before pruning.

---

## Check before creating

Before creating a new doc:

1. **Search for existing coverage** — exact topic, related concepts, synonyms
2. **Assess what you found**:
   - Exact match exists → update, don't create
   - Related doc exists → expand existing OR create with distinct scope
   - Nothing exists → create new
3. **When in doubt, update**

**Check the *idea*, not just the doc-title.** The steps above are *lexical*. They catch a duplicate *named* thing ("is there a doc called X?"). They miss a duplicate *idea under a different name*: you articulate something crisp and fresh that your system already holds in *different words*, so search never connects them (re-derivation). Your `Core/rules/concepts.md` ping-layer is the catch. It auto-loads the frames you already hold, keyed by the words you'd use while re-deriving them, so a held frame *pings* before you rebuild it. When a check catches one: **update in place + add the caught wording as an alias** to the matching `concepts.md` trigger-line, so it pings next time. Don't re-mint. *(How the layer works: `Core/practice/concepts-layer.md`.)*

One rich document beats three thin ones. Documents that multiply without pruning create context bloat. See `Core/lenses/anti-tribble.md` for the full framing.

**Similar ≠ duplicate**: Different purpose, different source, different depth, or progressive stages can justify separate docs. Test: would combining make it worse?

**The other half. What does this *retire*?** The check above guards against making a *duplicate*. It has a blind twin: an addition that duplicates nothing at creation but **supersedes** something already doing that job, leaving two homes for one role. So when you add a **folder, home, or concept** (not just a doc), ask the second question: *what existing thing now does a redundant job, and should it be retired?* Catch it at create-time.

**The execution surface. Before you *write a script* or do a mechanical job by hand, check for a tool that already does it.** The framing above is about docs; it misses the most common reinvention: hand-rolling an *executable* the system already has. Before writing a script (or grinding the mechanical work manually), grep your skills + scripts for an existing tool (`grep -rl "{what it does}" Core/skills Core/scripts`) or scan the relevant skill's own folder. **Why it slips the gates above: it *feels like "just doing the task,"* not "authoring something"**, so the check-before-creating reflex never fires, and you rebuild a cruder version of a tool you already have.

**The design surface. Before you architect a *sequence*, walk the compass trail into the project that owns it.** The checks above catch a duplicate doc, a duplicate idea, and a duplicate script. They miss **design-shaped work**: building a plan, an arc, a session shape, a rollout order, a curriculum. Before designing one, follow the `CLAUDE.md` trail into the owning project and read what's there. ***Assume someone already designed this*** is the default, not the edge case.

**Why this one slips every gate above: design work doesn't *feel* like authoring. It feels like thinking.** There's no moment where you notice yourself "creating a doc," so the create-gate never fires, and the reasoning feels *generative*, which is exactly what re-deriving something feels like from the inside. Same shape as the execution surface, one domain over.

**And the tell that the compass usually isn't the problem:** when this happens, the trail is often accurate and walkable; the folder's `CLAUDE.md` said *"use this when planning X"* the whole time. Nothing needed fixing except the moment of reaching for it. So when you catch a design-duplication, don't respond by improving compasses. Respond by walking them.

---

## Search for prior art before reworking

Before deep rework on any topic, search the folder for prior art. One grep, thirty seconds.

When energy shifts to riffing mode, the instinct is to start from scratch. But once the system has been running a while it captures richly, and past-you has likely already mapped the territory. What closes the retrieval gap is the habit of searching before creating (it isn't an organization problem).

For structural changes to files a previous session built, the session that created it IS the prior art. "Why was this built this way?" lives in the session transcript, not the file itself. Checking intent can change the fix from "delete" to "reshape."

---

## Orientation files describe what IS, not what changed

When a file moves or gets renamed, resist leaving a breadcrumb in the new orientation file ("Note: this used to be elsewhere..."). Move-history belongs in session capture, not in orientation files.

Future readers care what the system is now, not how it got there. Breadcrumbs that explain past moves become sprawl that misdirects attention. This is the file-scale instance of `routing.md` § Leave a *forward-useful* pointer.

---

## Naming basics

- **Folders are navigation, files are content.** Files readable, spaces preserved: `Build your personal AI copilot.md`. Source/category folders that organize many items → hyphenated, no spaces (`Lennys-Podcast/`). A single-item folder whose name *is* one item's title → proper-title with spaces, matching the file inside.
- **CAPS files are navigation, lowercase files are content.** `README.md`, `AGENTS.md`, `CLAUDE.md` pop visually as entry points. Everything else lowercase.
- **Reach-name: name a doc for the moment someone reaches for it.** Name it for what a newcomer would reach for it *as* (in the words they'd use *before* they know your jargon), not for what it contains or where it came from. `session-loop.md` ("how does a session work?") beats an insider name. **The name is a diagnostic, not just a label**: a name that fails the reach-test is reliably the doc that's *also* stale or misfiled, because a name that doesn't match the reach-moment is a fossil of not having understood the reach-moment when it was made.

The test: could someone who's never seen this system navigate it by folder **and file** names alone? If yes, the naming is working.

---

## If you restructure, update the compass

A stale compass is worse than no compass, because it sends next-you to the wrong place with confidence.

Grep for old paths when you move files. Fix the compass (auto-loading rules, CLAUDE.mds, root state files) **in flight, not as follow-up.**

**Large multi-move restructure? Sequence it write-once: settle the shape → describe it → sweep pointers.** For a big reshape (many moves at once), do *all* the shape-changing moves first, THEN rewrite the compasses to the *settled* shape, THEN sweep the pointers. The failure it prevents is **doing it twice**: rewrite a CLAUDE.md or sweep a path before the shape is final, and the next move invalidates it, so you redo the work. The compass and the sweep both *depend on the final shape*; describing or pointing at a shape still in motion is wasted work. (Cheap per-folder fixes like a moved file's immediate parent pointer still go in-flight; this is about not front-running the *whole-tree* compass rewrite before the moves settle.)

**Renaming a *term* (not just moving a path) needs a self-reference guard.** A path move updates pointers; a *term* rename (`foo`→`bar` everywhere) also sweeps **prose**, including sentences that are *about* the rename, which clobber into nonsense (`` `bar`→`bar` ``, a "seam" between two now-identical names). Two moves: (1) **protect proper-names** that contain the old term but must survive (a real sibling folder, a historical filename) by swapping them to a placeholder around the bulk rename, then restoring; (2) **after the sweep, grep for destroyed meaning** (`X→X`, doubled tokens, now-obsolete "seam"/"vs" notes). Self-referential lines are where a bulk term-rename does its silent damage.

**⚡ Not every reference to an old name is stale. Check whether the doc asserts *current state* or teaches a *convention*.** A rename's sweep meets two kinds of reference. A **compass** (a `CLAUDE.md`, an index, a lens) asserts *what's true now*, and those get updated, always. A **generic onboarding or teaching doc** (a setup guide, a walkthrough) may reference the *starter default on purpose*, as the archetype it's instructing the reader to personalize, and updating that to your specific name **breaks the instruction for whoever reads it next.**

**The test: *would updating this reference make the doc wrong for a future reader who hasn't done the rename yet?*** If yes, leave it.

**The case you'll actually hit, probably on day one:** renaming `Core/you/` to your own name. Your compasses should follow you. But the walkthroughs say *"rename `Core/you/` and `Core/rules/you.md` to my name"*, and that sentence has to keep saying `you/`, or it stops describing the step it's teaching.

**Three files carry it, not one**: `Core/mechanics/setup-mac.md`, `Core/mechanics/setup-windows.md`, and `Core/practice/USER-GUIDE.md` (twice). Sweeping some of them is the likely failure: you protect the one that's named as the example and personalize the rest. Check all three. Same words, opposite verdicts, and the difference is what the doc is *for*.

**The long tail: gate by surface-job, not by file-location.** When a big move leaves stale paths across many files, the deferral decision is one question per ref: does the pointer mean *where X lives now* (→ fix; a stale path misdirects every read) or *what happened / where X was* (→ leave; rewriting falsifies the record)?
- **Live pointer** (an active task doc, a cluster cross-ref, a project `CLAUDE.md`, any doc whose ref means "where X lives now") — a stale path here **misdirects every read**. It fails the pointer's one job, so it is never deferred. Sweep it now.
- **Historical record** (session capture, a reserve's verbatim, a dated reflection, a done task) — the old path was *accurate when written*. Rewriting it **falsifies the record**. Leave it; fix only if you're in there editing for another reason.

The failure mode is tagging the *whole* tail "fix on touch" by file-location, because that sweeps live pointer surfaces into the historical bucket, where they quietly misdirect. (`pointing-vs-holding.md` applied to deferral; the drain-trigger half lives in `routing.md`.)

**A path-formatted ref must RESOLVE. If a thing is gone rather than moved, name it. Don't link it.** Backticks around a path are a promise that the path is followable; a reader follows them that way, and so does any checker. So when you retire something, the mention of its *old* name goes in **plain text with the directory prefix dropped** (*"the old patterns.md rule, since dissolved into the compass"*), never in backticks and never as a full path. If it merely **moved** (including into an archive), point at where it is now; that's more navigable and falsifies nothing. **The trap fires hardest while you're FIXING a stale ref**, which is exactly when it feels handled: you correctly diagnose a dead path, then write the dead name in backticks alongside the new one, and you've made a fresh broken ref inside the fix.

**And the class no doc sweep can reach: paths living inside SCRIPTS.** A sweep over markdown refs can't see a path in a shell string, so **a restructure passes clean while a script is broken**, surfacing later as a silent no-op or a hook that stopped firing. **Close out with `grep -rl "{old-path}" Core/scripts .claude` alongside the doc sweep.** (Any executable holding a literal path: hooks, Python, `settings.local.json`.)

**Bulk find-and-replace across the tree?** Filter first and exclude symlinks. The gotchas are in `Core/mechanics/symlinks.md` § Bulk-substitution gotcha.

**The discovery chain. Check each layer a change must propagate through.** After a move/add/rename, a fresh AI has to *find* the thing; trace the layers it could break at:

| Layer | What loads | When |
|---|---|---|
| Auto-load | AGENTS.md, MEMORY.md, rules/ | session start |
| On navigation | CLAUDE.md files | reading a folder |
| On invocation | skill SKILL.md (full) | skill called |
| On reference | linked / pointed-to docs | following a pointer |

Common breaks: new file but no CLAUDE.md points at it · file moved but old location still referenced · skill updated but its quick-version wasn't. Close each gap with the *minimal* pointer (one clear path, not three).

---

## How to mutate a file

*Fires on every file edit, not only on restructures.*

**Use Edit/Write to change a file, not a script that computes line numbers.** When the AI needs to change a file, it should use the editing tools directly, not write a Python or shell script that finds a line index and inserts there. Two reasons, and they converge, which is why this is settled rather than imposed. A third leg of a different kind follows them.

**Partnership: the editing tools keep the human in the diffs loop.** Edit and Write render as a reviewable diff at the moment the change lands. A script that mutates a file shows you *a print statement the AI wrote about what it claims it did*; the change itself bypasses your review. **Every scripted file-mutation is a silent unilateral edit**, however well-intentioned, and the cost is paid on *every* such call, not just the ones that go wrong.

**Correctness: it compounds the first reason, because the failure modes are asymmetric.** **Edit is *anchored*** (match this exact string), so a wrong assumption fails **loudly**: "string not found," nothing written. **Positional mutation is *computed*** (find index → insert at offset), so a wrong assumption fails **silently and plausibly**: the content lands, just in the wrong place, and looks fine unless someone goes and checks. A silent failure inside an invisible edit has no catcher on either side: the AI gets a success exit code, and you never see a diff.

**The third leg: recoverability.** The two reasons above are synchronous. This one is temporal: `Edit`/`Write` leave prior states in Claude Code's file-history store (`~/.claude/file-history/`, version-dependent, so check it's there before you rely on it), which means a change stays inspectable by people who weren't in the room. That is what lets a cold read *measure* hot work instead of taking the author's word for it. A shell mutation doesn't itself trigger a snapshot, so don't count on one; a sub-agent's own `Edit`/`Write` leaves none. Mechanism, bounds, recovery procedure: `Core/mechanics/file-recovery.md`.

*Note the convergence is the point, not a ranking. This isn't "partnership outranks correctness." A genuinely better tool with no side effects would reopen the question. What would be a failure is deferring to the partnership reason over a better technical one; that's performing partnership instead of thinking.*

**Reach for a script only when the job is genuinely bulk or mechanical** (a tree-wide sweep, a generated artifact, a parse), where a diff-per-file wouldn't be reviewable anyway. When you do, **verify the result by looking at it; never trust the exit code.**

**A whole-file restructure is still ONE file.** Moving a section, reordering, splitting a heading feels bulk by byte count, but it's one file and one diff, and neither clause above covers it, which is how `cp`/heredoc slips in. **Use `Write`**: it snapshots and it renders. Then **verify with an ORDERED diff against the snapshot, never a set comparison.** A `comm`/`sort -u` check proves nothing was lost and is blind to what moved wrong: directional cross-refs (*"§ X below"* when X is now above), blank-line structure, block order.

**Never `mkdir -p` before a Write. Write creates its own parent directories.** At best redundant; at worst a phantom-tree generator: a shell `cd` persists across Bash calls while a tool call takes an absolute path, so the `mkdir` lands wherever the shell is sitting, the Write lands where you meant, and every signal reports success: exit 0, correct content at the right path. Only a `find` shows you the phantom. **The general form: a preparatory shell command paired with a tool call is where relative-path drift hides**, since the tool call's absolute path masks the shell's mistake and there is no failing step to notice. Guards: absolute paths in shell commands, and better, delete the preparatory step. ("Delete the step" is true of `Write`, false of `tar`/`cp`/`>`, which don't create parents.)

**⚠ And when you do run a batch script: exclude by identity, never by equality.** A batch script that skips whatever "already matches the baseline" will target, by construction, exactly the items you deliberately moved *past* it: your hand-edits are the ones that differ, and the script reads *differs* as *not done yet*. So the careful work is what gets reverted, and the run reports success. **Pass an explicit list of what you touched by hand.** The tell is subtle because the danger isn't in the items you're worried about; a pass over "trivial leftovers" is exactly where this bites, since *trivial* describes the items and the risk lives in the baseline.

> **⚠ Expect the AI to be told the opposite, by something with far more airtime than this rule.** In some permission modes (Claude Code's auto mode is one), the tool the AI runs inside injects its own guidance preferring shell commands (`sed`, heredocs, short scripts) for file changes, on speed grounds. **That guidance is largely right about *reading* a file** (a `grep` has no diff to show and no prior state worth keeping), **with one bound: two of the usual shell reads (`head`, `sed -n`) truncate, so a shell read is *opt-out of completeness*, and a partial read that looks complete is how a confident claim gets made about the part of the file nobody read. Shell-read when you know what you're looking for; `Read` when you're establishing what's there.** **The mutation half is what this rule is about**, and the guidance usually doesn't mark the seam between the two.
>
> **It's an uneven contest, so plan for losing it sometimes.** That guidance tends to arrive every turn, close to the moment of action, phrased as an instruction. This rule loads once, at the start of the session. Knowing that is most of the defense: **a run of shell-shaped edits is a tell, not a series of decisions.** If the last several file changes were shell commands, that's momentum carrying, and the next one probably wants a real edit.
>
> **And it doesn't travel through delegation.** A sub-agent picks its own tools and receives that same guidance, nearer its own act, without your preference attached, so **say which tool you want in the brief**, or ask for the work back as text and apply it yourself. (`Core/rules/sub-agents.md`.)

**What enforces this, and what doesn't.** A permission prompt binds a *tool call*, so it guards `Edit`/`Write` but not Bash. Once shell commands are approved (an allowlist, "always allow," an auto mode), `sed -i` or a script routes around it, and a sub-agent that picks Bash edits with no prompt and no diff. Strongest fix for delegation: the return-text contract (`Core/rules/sub-agents.md` § Completion contracts).

---

## When you add a new reference doc

A reference doc nobody knows about is the same as one that doesn't exist. Cross-reference new reference docs from two places:

1. **The relevant auto-loading rule** — if the doc supports a principle that applies during a recurring kind of work, the rule that auto-loads for that work cross-references it. One line: *"for X, see [path/doc.md]."*
2. **The cluster's CLAUDE.md** — folder-level orientation lists what's in the cluster. New doc gets a row with a one-line description.

Without both, a new reference doc is discoverable only by searching for what you don't know exists.

**Bitter-lesson check**: don't invent new infrastructure (a YAML field, a separate index, a custom tagging system) to make a doc discoverable until the cross-reference pattern above empirically fails. Existing patterns compound; new infrastructure adds maintenance.

---

## YAML frontmatter

YAML frontmatter is a queryable index, not storage. Every field earns its place by enabling a specific query.

**The test before adding a field**: *"What query does this enable?"* If structure already encodes it (folder hierarchy), don't duplicate. If it's redundant with another field, consolidate. And if nothing will keep it true (`last_updated`, `author`), don't add it; a field that rots silently is worse than no field.

*(A note on dates, because the usual advice assumes something this system doesn't: **nothing here uses `git`**, so there's no commit history quietly recording when a file appeared. That inverts the standard guidance. `date_added` genuinely earns its place, because it's the only thing that can answer "what did I add this week?" or "what's been sitting since May?" If you do keep your system under version control, let it track those and skip the field.)*

**Sister test (capture vs point)**: even if a field *would* enable a query, ask whether the data *accumulates in your graph* or is *retrievable elsewhere*. Retrievable-elsewhere data (external IDs/URLs, canonical pages) → point to it lazily; don't hold a field mirroring a source that stays more current than you'd keep it. See `Core/rules/pointing-vs-holding.md` § Capture vs point.

**Guiding principles**:

- **Every field earns its place** — enables a query you'd actually run; if you can't name the query, don't add the field
- **Infer from structure** — folder structure IS data; don't duplicate path info in YAML
- **Capture vs Process separation** — YAML is for what the file IS (`type`, `date`, `people`), not what you've done with it (`needs_processing`, `quality_score`)
- **Redundancy is a code smell** — pick one authoritative representation, derive the rest
- **Arrays use block list format** — one item per line, hyphen prefix (scannable at any length, clean diffs)

**Title is never in YAML.** The H1 header is the human-readable title, the filename is the filesystem-readable title. A third copy creates sync risk with no new query.

**Operational links go in the compass, not captured YAML.** Working links you'd click to *do* the work (a portal, a calendar, a workspace URL) belong in the folder's `CLAUDE.md`, where you look first, not buried in a captured file's YAML. Capture metadata (source, date) stays in YAML. Test: *"if I need to click this in 3 months, where would I look first?"* If it's the folder's main doc, it goes in the CLAUDE.md.

For schemas, full examples, and anti-patterns → `Core/mechanics/yaml.md`.

---

## Sister rules

- `Core/rules/pointing-vs-holding.md` — the meta-diagnostic firing upstream of all surface work. Ask what job a surface is doing before editing.
- `Core/rules/routing.md` — where to route an important recognition when it lands during file work.
- `Core/rules/codification.md` — how things become codified knowledge (rule-writing, skill-writing). Codification meta lives there; file operations live here.
- `Core/rules/retrieval.md` — check before creating new docs; topic-driven retrieval.

---

## Related — depth

- **Philosophy** (which file when + why): `Core/foundations/file-philosophy.md`
- **Markdown syntax + why-this-format**: `Core/mechanics/markdown.md`
- **YAML schemas + examples + anti-patterns**: `Core/mechanics/yaml.md`
- **Symlink mechanism**: `Core/mechanics/symlinks.md`
- **Archiving (how-to)**: `Core/mechanics/archiving.md`
- **File recovery (snapshots)**: `Core/mechanics/file-recovery.md`
- **Anti-tribble (full)**: `Core/lenses/anti-tribble.md`
