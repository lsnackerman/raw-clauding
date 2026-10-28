---
name: wrap
description: End work session intentionally. Use at natural stopping points, before context limits, or when switching contexts.
---

# /wrap - End session intentionally

Quick, intentional session ending. Preserves work, ensures continuity.

**The flow: think → route → task-housekeep → handoff → capture**

---

## What to do

### First: identify your session

Before the wrap machinery starts, figure out which session file you're working with, and compute its path. Everything downstream (PULLING, THREADS, task doc SESSION INDEX, reserve connections) references that real path — so settle it once, up front, instead of writing placeholders you resolve later.

**Detect your platform:**
- **Claude Code** → session transcripts (JSONLs) live at `~/.claude/projects/{project-slug}/*.jsonl`
- **Cursor** → at `~/.cursor/projects/{project-slug}/agent-transcripts/{id}/{id}.jsonl`. Note `source: cursor` for the YAML later. (Format details: `Core/skills/sync/edge-cases.md` § Cursor sessions.)
- **How to tell**: do you have a `Bash` tool or a `Shell` tool? `Bash` = Claude Code, `Shell` = Cursor.

**Find your session — verify, don't assume.** Picking the most-recently-modified file (`ls -t | head -1`) is NOT reliable when more than one session is open. Instead:

1. List the recent transcripts: `ls -lt ~/.claude/projects/{project-slug}/*.jsonl | head -5`
2. **Grep the top few for a distinctive phrase from this session's opening** — an unusual word, a slash-command you ran, a specific name. The file that contains the match is yours.

**Compute the session file path**: `Core/sessions/{date}-{short-hash}.md`. The short hash is the first segment of the session UUID (e.g. `02701400-ba8e-426a-...` → `02701400`).

Hold this path in mind — every write below that points at the session uses it. Step 4 creates the file there.

### 0. Surface + compound (AI goes first)

The compound moment. One intentional sweep:

1. **What's alive that would dissolve at session end?** Threads that opened and didn't finish. Things you got curious about that the work moved past. Operational questions that never got answered. **These MUST route in Step 1** — if you don't route them, they're gone by definition.

   *For a long or dense session, press harder than the default scan:* if context evaporated right now, what specifically would not survive? Watch for (a) a **connecting thread** across the whole session that no single note captures, and (b) **craft principles** you articulated mid-session that don't have a home yet. The quick scan catches discrete items; the press catches the synthesis.

2. **What patterns emerged that the system should learn?** What worked that was non-obvious? What broke in an instructive way? What would the next instance get wrong without knowing this?

3. **What did you ask mid-session that never got answered?** Scan back for questions you posed that got pivoted past. Absences are harder to notice than presences, so they won't surface in 1 or 2 unless you look for them on purpose. Common shape: AI asks "want me to do X?" → human redirects → the original ask never resolves. **These route** like #1.

   *And ask the inverse, which is the more dangerous one:* **what did you commit to that you never finished?** An unanswered question at least *looks* open. A **partially-executed approval** looks handled: the AI offers a numbered list ("want me to do 1, 2, and 3?"), the human says **yes**, two get done, something pulls the thread, and the third silently drops — with an approval on the record making both parties read it as finished. **The yes is what hides it.** So if you offered an enumerated list this session, re-read your own offer and tick each item against what's actually on disk. Nothing in the conversation will look wrong; only the check finds it.

4. **Did this session shift your bigger direction?** A real reframe, a new goal, a priority that flipped, something parked or activated. Most sessions, the answer is no — move on cleanly. When it's yes, surface it for a `VISION.md` touch in Step 1.

Surface everything. Name it. Don't route yet — that's Step 1. This isn't /floor; it's a focused scan for what's hanging and what compounded. If nothing's there, say so and move on.

**Why this is first**: AI thoughts get episodic windows that dissolve at session end. Human thoughts have continuous experience — they can circle back tomorrow. If the AI doesn't surface threads and patterns before the wrap machinery starts, they're gone. The structure creates the moment; the instinct fills it.

### 1. Route home

Take what you surfaced in Step 0 and route each item where it belongs.

**First — the handoff trio (ALIVE / PULLING / THREADS) is mutually exclusive. Classify each item ONCE, then route:**
- **Crisp next action** (a do-X, ideally with a *when*) → **`ALIVE.md`** (forward state) — only here.
- **Thread / tension / curiosity / open question, no crisp action yet** → **`PULLING.md`** — only here.
- **Already happened** (a decision landed, a thing got built) → **`THREADS.md`** — only here.

The same item never lands in two of these. If it feels like both, that's the instinct to capture-everywhere — apply the test, pick one home, and add a one-line *pointer* elsewhere only if a reader genuinely needs the cross-link.

*(There's a script that checks this — but run it at the end of Step 3, once all three files have actually been written this session.)*

| What surfaced | Route to |
|---------------|----------|
| Pattern / lesson learned | the relevant rule in `Core/rules/` (or `Core/lenses/` if it's a way of seeing) |
| System friction / skill gap | Fix NOW — update the skill, rule, or CLAUDE.md |
| Stale documentation | Fix NOW — if you moved files or restructured, update the folder's CLAUDE.md. If you changed how something works, check what still points at the old way. |
| Decision / direction change for a project | That project's CLAUDE.md (Key Decisions) |
| Direction / goal shift (only if Step 0 #4 was yes) | `VISION.md` — update the date, edit the relevant section. Most sessions skip this. |
| Hanging thread (operational) | `PULLING.md` |
| Reflection (more finished) | `Core/opus/` |
| Idea for a project (ripening, not yet actionable) | that project's CLAUDE.md (or an IDEAS.md you keep there) |
| Actionable next item for a project | `ALIVE.md` → relevant area section |

**Routing priorities:**

- **Core files first.** Patterns go in rules or lenses. Process changes go in skills. The system adapts from within.
- **System improvements happen here.** Skill friction? Update the skill now — you have the context; the next instance won't. CLAUDE.md stale? Freshen it. This is the highest-leverage handoff you can make.
- **Prune, don't lose texture.** Before parking or removing anything with history — a flag, a draft, a whole feature — scan for decisions and reasoning that exist ONLY in what you're about to remove. Capture them first, then prune.
- **Canonical home + pointers, not restatement.** When something naturally touches several homes, pick ONE that holds the full content; the others hold a pointer, not a copy. If you're writing the same description into a third place, that's duplication at the routing layer — a one-line `see X` does the job.
- **MEMORY.md is last resort.** Only for operational shortcuts that genuinely don't fit anywhere else. If the system can teach it through its files, it shouldn't also be in MEMORY.md.

### 2. Update task docs

All task-doc maintenance in one pass, across every task doc you touched this session (not just the "main" one — cross-cutting work touches several).

**Section-state changes — append, don't replace.** When a section's state changes (BLOCKER → RESOLVED, OPTIONS → CHOSEN), preserve the reasoning that produced the new state. Write the resolution on top; move the prior texture into a "how this resolved" note below. The *why* often lives only in the section you're updating — replacing it loses the thinking.

**Refresh the doc's own handoff block.** Every task doc opens with a `NOW · DECIDED · OPEN` block (the `/task` template creates it) so the next instance drops in warm. Rewrite it; never append a "done" prefix to it. The failure mode: you update the *backward* record (completed items, session index) but leave the *forward* handoff pointing at last session's plan. A stale warm-start is worse than none — it sends the next instance to the wrong place with confidence.

**HOW section:** move completed items to Completed (append at bottom, chronological). Reorder Pending so the most important is first. Add new items discovered this session. Where you have tactical insight, **include approach notes** — not just *what* to do next but *how* ("mechanical, good warm-up" / "needs fresh thinking, read X first").

**OBSERVATIONS section:** task-specific findings only. System-level patterns already routed in Step 1.

**YAML:** set `status: done` if finished (the hook auto-archives to `Tasks/_done/`). Review tags so they match what the session actually covered — sessions drift, and tags are how future-you finds this. No cap; findability over tidiness.

**Reserve connections** (after tag review): do any of this session's tags match a reserve in `Core/reserves/`? If yes, append one line to that reserve's Session Map (date, what this session contributed, task doc reference). Not a re-run of /explore — just maintaining the connection, ~30 seconds per match. No match → skip.

### 3. Handoff

**`ALIVE.md` carries the handoff by ORDER, not by a separate "start here" section.** Sections sit in priority order (`FOLLOW-UPS` first, then one `NEXT - {AREA}` per area) and on-deck items sit at the top of each, so `/pickup` reads it top-down and lands on the right thing without a spotlight that has to be rewritten every session. (A spotlight was tried; it grew into a second copy of the backlog with reasoning attached. Order can't do that.)

#### FOLLOW-UPS — what's live between the human and other people

One line per person, pointing at where the detail lives (their page, the thread). Both directions: what the human owes, and who the human is waiting on. Sent or received → delete the line. This section spans every area, which is why it stays on top.

#### NEXT - {AREA} — the pending work (append-then-prune)

One `## NEXT - {AREA}` section per area of the human's life, on-deck items at the top of each. These sections are the single source of truth for pending work.

- **Read every area section FIRST, then update — append-then-prune, not replace.** For each existing item: still relevant? **Keep it** (reorder if priority shifted; the top of each section is the handoff). Done this session? Remove it — a done item leaves the list, it doesn't get a checkmark. Only exists here, nowhere else? **Keep the texture** — route it somewhere durable (task doc, PULLING) before you drop it.

- **Entries are a name plus a pointer, never the reasoning.** The reasoning that decides what's on deck belongs in the task doc's `NOW · DECIDED · OPEN` block, where the work lives; if there's no task doc, a `PULLING.md` line holds the why. A name can't go stale in its text; a paragraph can.

- **Forward-reason to set the order.** Work through *"if I were next-me tomorrow, what would I actually do first?"* and put that at the top of its section. If one area's top item comes before another area's, move the section.

- **Sweep for ripples this session created.** Does anything in ALIVE reference state this session changed? A path you invalidated by moving files; a "before X happens" framing where X now happened. Update or remove. A 30-second pass catches what would otherwise silently break at next pickup.

- A new area earns its heading when the first item that belongs in it arrives.

Replacing the section from this session's memory drops everything that wasn't in this session's context. Append-then-prune puts the burden on deliberate removal instead of recall.

#### Currency checks

- **MEMORY.md** — did this session change anything in its territory (paths moved, conventions shifted, a pointer gone stale)? Update inline. ~30 seconds.
- **CLAUDE.md** — two checks: did you *edit* any folder's CLAUDE.md this session (is the result actually current, not just a successful write)? And did your work *warrant* a CLAUDE.md update that didn't happen (new file created, new sub-folder added, structure shifted — does the folder's compass know about it yet)?

#### Then

- **`PULLING.md`** — append the Step 0 threads, then **drain it**: prune what resolved or landed somewhere permanent, so it stays short. PULLING is a pointing surface — it drains to current, it doesn't accrete.
- **`THREADS.md`** — prepend a new entry at the top (most-recent-first): `## YYYY-MM-DD (session HASH — short description)` heading — the hash is what links the entry to its file in `Core/sessions/` + a bulleted list of what landed, one line each. The session file holds the full texture; THREADS is the scannable layer that pairs with ALIVE.
- **Task doc SESSION INDEX** — in each task doc you touched, append a pointer: `**Session N (YYYY-MM-DD)**: [filename](Core/sessions/filename.md) — one-liner`. **Repo-root-relative, never `../`** — a task doc moves to `Tasks/_done/` when it's finished (the archive hook does it), and a `../` link written from `Tasks/` dies the moment that happens. (The link target gets created in Step 4, a moment later — that's fine.)

**Then check the trio rule held: `python3 Core/scripts/dup-check.py`.** All three files have been written by now, so it has something to compare. It flags items that ended up on two surfaces — `ALIVE ↔ PULLING` is usually one forward item written two ways (consolidate); an item in both a forward surface and `THREADS` usually means the work finished, so prune the forward copy.

It's a **heuristic flagger, not a proof** — it compares word overlap, so it misses duplicates you worded differently and sometimes flags two items that merely share a topic. Report-only; the judgment is yours. **It prints how many items it examined next to the result — read that number.** `0 items examined` is not a pass, it means nothing has been routed yet.

### 4. Capture session (LAST)

**Do this last so the full wrap is in the transcript before /sync reads from it.** The wrap itself is part of the session — decisions made, items reordered. Capture before wrapping and you lose the wrap. **Just run it — don't ask "ready to capture?" first.** It's mechanical; there's no decision point that needs the human.

1. **Create the session file shell** at the path you computed up front (`Core/sessions/{date}-{short-hash}.md`):
   - **YAML frontmatter**: `date`, `session_id` (full UUID), `tasks`, `tags`, `summary` (+ `source: cursor` if Cursor)
   - **Title + RECAP** — synthesize what happened (decisions, discoveries, key threads)
   - **`## LOG`** header on its own line, left empty — /sync fills it

2. **Populate the LOG** — invoke `/sync` (or run `Core/skills/sync/sync-session.sh`). For **Cursor**, pass the JSONL explicitly since auto-detect looks in the Claude Code path:
   ```
   python3 Core/skills/sync/extract-session.py ~/.cursor/projects/{project-slug}/agent-transcripts/{id}/{id}.jsonl
   ```
   Splice the output into `## LOG`. Full capture architecture is in the /sync skill; Cursor details in `Core/skills/sync/edge-cases.md`.

---

**Continuing past /wrap?** When the conversation keeps going after the wrap is "done" (a held thread resolves, a clarification lands, small follow-ups), re-invoke `/sync` to refresh the LOG — it's idempotent, safe to run any number of times. If the post-wrap work was substantial, refresh the RECAP and tags too: sessions drift, and the captured record should match where you ended up, not where you planned to go.

**And re-check THREADS, not just the RECAP.** THREADS is written in Step 3 — *before* any post-wrap work exists — so a finding that lands after the handoff is captured in the session file and **invisible on the scannable layer**, which is the surface `/pickup` actually reads. The RECAP refresh doesn't cover it: at that point THREADS isn't a compression *of* the RECAP; it predates it. **Ask: did post-wrap work produce something next-you would act on?** If yes, add the line. The post-wrap gap is a real session shape — don't assume `/wrap` closes the transcript.

---

## Quick version

**First** — Identify your session. Verify the transcript by content (grep a distinctive phrase from the opening), compute the path `Core/sessions/{date}-{short-hash}.md`, use it everywhere downstream.

0. **Surface + Compound (AI first)** — what's alive? what patterns emerged? what did you ask that went unanswered? did direction shift? Name everything.
1. **Route home** — classify each item ONCE (ALIVE = action / PULLING = thread / THREADS = record), then route. Patterns → rules/lenses, friction → fix now, reflections → opus/. Core files first, MEMORY.md last.
2. **Update task docs** — section-state changes append-don't-replace; refresh the doc's own handoff block; HOW (pending/completed), observations (task-specific), YAML (status + tags), reserve connections. All docs touched, one pass.
3. **Handoff** — ALIVE (FOLLOW-UPS + the NEXT - {AREA} sections: append-then-prune, forward-reason the order, on-deck at top, sweep ripples) + MEMORY/CLAUDE.md currency + PULLING (drain) + THREADS (bulleted entry) + task doc SESSION INDEX. **Then `python3 Core/scripts/dup-check.py`** — read the items-examined count, not just the ✓.
4. **Capture session (LAST)** — create the shell at the known path (YAML + RECAP + `## LOG`), `/sync` to populate. Just run it.

**Capture last = full session in the LOG. Identify first = real path everywhere downstream.**

**Task doc section order**: WHAT → WHO → HOW → LINKS → OBSERVATIONS → SESSION INDEX

---

## When to wrap

**Do it:**
- Completed major work
- Switching contexts
- Context running low
- End of session

**Skip it:**
- Deep in flow
- Nothing significant yet
- Mid-investigation

Trust your gut.

---

## Skill Check (after every wrap)

Quick scan: anything about this wrap that felt off or could be smoother?

- Did the compound scan surface real patterns or feel forced?
- Did routing feel clear, or did items not have obvious homes?
- Did you restate the same thing across multiple homes, or did each home hold a different aspect?
- Did the handoff capture what next-you actually needs?
- Did the wrap miss something the next session will wish it had?

**If yes** → update this skill now. The improvement compounds.

**If no** → move on. Not every wrap teaches something.
