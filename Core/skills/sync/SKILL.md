---
name: sync
description: Refresh the current session's LOG with a fresh extraction from the JSONL. Use any time you want the captured archive to match what actually happened — including after /wrap if the session continues. Safe to invoke multiple times; idempotent.
---

# /sync - Refresh session log

*The memory you share. Drop this at any natural pause to keep the archive current.*

Idempotent session capture. Finds the current session file and refreshes its LOG section with a fresh extract from the JSONL. Run any time; the LOG always matches the JSONL up to the moment of invocation.

---

## When to use

- Session has continued past `/wrap` and you want the capture current
- You're about to hand off and want the LOG to include everything
- You realize the LOG cut off (tail-check after first capture)
- Any natural pause where "make sure the archive reflects reality" feels right

Not for: full session end (that's `/wrap`). `/sync` is the LOG-refresh step, isolated.

*(After a post-wrap `/sync`, RECAP and THREADS still describe the earlier session. If the new work matters to next-you, add it there too; see the end of `/wrap`.)*

---

## What to do

1. Run `Core/skills/sync/sync-session.sh` via Bash.
2. **Sanity-check the first LOG line matches this conversation's opening turn** (tail or head the target file). `/sync` trusts the YAML `session_id`; if the YAML was written wrong upstream (e.g., during `/wrap` with parallel sessions active), the script will faithfully extract the wrong conversation. The first-line check is the 2-second catch. If they don't match, see § Verify before extracting below for the recovery path.
3. Report line-count delta so the human can see the update landed.
4. If anything surfaced worth routing (patterns, threads, decisions from what was just captured), flag it, but don't force it. The action is the sync, not the reflection.

The heavy lifting is in the script (which auto-detects the session file and reads the `session_id` from YAML to stay correct across parallel Claude Code sessions). The script is reliable; what's not always reliable is the YAML it reads, so the check is at the boundary.

---

## What makes this different

| Skill | Scope | Purpose |
|-------|-------|---------|
| `/wrap` | Full session close | Route + task docs + handoff + capture. Whole ritual. |
| `/sync` | LOG refresh only | Pure, lightweight, idempotent. Run any time. |

`/wrap` is ceremonial. `/sync` is ambient.

⚠️ **"Idempotent" means idempotent for the LOG.** `extract-session.py` replaces everything after `## LOG`, so anything you hand-write below that marker is deleted by the next refresh, silently, with a success message. **Anything hand-authored into a session file goes above `## LOG`.**

---

## Why this matters

Neither human nor AI has persistent memory. Human brains lose things not immediately in front of them. AI loses everything at session end. This isn't different limitations. It's the same limitation. **Files ARE the memory you share.**

**Verbatim capture IS the helpful thing.** Not "resist your instinct to be helpful by compressing." This IS the helpful thing — for a brain that can't hold it all, for an AI without persistence whose thinking otherwise evaporates.

**Whatever isn't captured evaporates.** The ideas, the connections, the texture of how you got somewhere — gone.

**Files aren't documentation OF the system. Files ARE the system.** Coordination happens through files, not memory.

---

## The format

The script outputs conversation in this format:

```markdown
> Human's exact words here

AI's exact response here, including the hedging, the warmth,
the closing questions. Not a summary of what was said —
the actual thing said.

> Human's next words

AI's next response, verbatim.
```

**The test**: Could someone who wasn't here feel what this exchange was like?

**No echo**: Don't restate the human's words before responding. Their words appear once, in their voice.

Tool calls are interleaved in order as `[tools: Write path]` / `[tools: Grep 'pattern']`, the doing alongside the thinking. Note what that does **not** include: the *contents* of a file written to an ephemeral path (the session scratchpad, `/tmp/`) are never captured, so a reusable artifact left there is unrecoverable once the session ends and the transcript ages out (Claude Code keeps session JSONLs for 30 days by default, the `cleanupPeriodDays` setting). **The fix is upstream, not here** (`Core/rules/persist-before-pause.md` § the scratchpad is not "disk"): route reusable artifacts to a durable path in the system.

---

## Why auto-extraction wins

AI compresses unconsciously. These are the first to go when capturing manually:

| Edge | What it is |
|------|-----------|
| **Openers** | "dude, let's...", "ooh, what if..." |
| **Closers** | "what do you think?", "does this land?" |
| **Uncertainty** | "I'm not sure but...", hedging |
| **Warmth** | humor, casual energy |
| **Rhythm** | quick back-and-forth vs long explanations |

**Auto-extraction bypasses all of this.** The session file has everything. No compression instinct to fight.

---

## Architecture

### Where sessions live

Session files are standalone documents in `Core/sessions/`:

```
Core/sessions/{date}-{session-id-short}.md
```

Example: `Core/sessions/YYYY-MM-DD-HASH.md`

### Session file structure

```markdown
---
date: 2026-02-03
session_id: 601c5534-cb84-460a-83c0-78aa58abad81
tasks:
  - task name referenced
tags: [topic-a, topic-b]
summary: One-liner of what happened this session.
---

## RECAP
{synthesized what-happened, written at wrap}

---

## LOG
{verbatim conversation via extraction script}
```

**RECAP is the distilled summary. LOG is the raw texture.** Both matter: RECAP for quick re-entry, LOG for the full picture.

**Sessions are standalone.** They can reference multiple tasks (sessions wander). Task docs reference sessions via SESSION INDEX. The task is the compass, the session is the texture.

### How the script finds the JSONL

Claude Code stores conversation data at:

```
~/.claude/projects/{your-project-path-with-dashes}/{session-id}.jsonl
```

The wrapper `cd`s to your system root itself, so it doesn't matter where your shell is sitting. The Python script walks up from the current folder until it finds a matching project under `~/.claude/projects/` (every non-alphanumeric character in the path becomes `-`), and if nothing matches it says so and lists the projects it found.

**Deterministic way (the reliable one): the harness sets `$CLAUDE_CODE_SESSION_ID`, and the wrapper reads it.** Your JSONL is exactly `~/.claude/projects/<slug>/$CLAUDE_CODE_SESSION_ID.jsonl`. No glob, no recency guess, and immune to grabbing the wrong file when multiple sessions are open at once. (The session scratchpad path, `/tmp/claude-<uid>/<slug>/<session-id>/`, carries the same id if you ever need it by hand.)

**Mtime-fallback** is what the wrapper does when the variable isn't set (Cursor, some harnesses): the most recent JSONL **by modification time** (not alphabetically; UUIDs have no relationship to time). It's a heuristic: most-recent ≠ always yours under concurrency:

```bash
ls -lt ~/.claude/projects/{your-project-slug}/*.jsonl | head -3
```

Then pass it explicitly:

```bash
python3 Core/skills/sync/extract-session.py /path/to/file.jsonl
```

### Verify before extracting

Especially with parallel sessions, spot-check that the JSONL is the right conversation:

```bash
python3 -c "
import json
with open('/path/to/file.jsonl') as f:
    for line in f:
        d = json.loads(line)
        if d.get('type') == 'user':
            content = d.get('message',{}).get('content','')
            if isinstance(content, list):
                for item in content:
                    if isinstance(item, dict) and item.get('type') == 'text':
                        print(item['text'][:200]); break
            elif isinstance(content, str): print(content[:200])
            break
"
```

If the first human message doesn't match this conversation, you have the wrong file. This takes 2 seconds and prevents extracting an entire wrong session.

**Recovery path (if caught after extracting)**:
1. Identify the correct JSONL via first-message spot-check.
2. `mv` the session file to `{date}-{correct-hash}.md`.
3. Update YAML `session_id` to the correct full UUID.
4. Re-run `/sync`. It now extracts the right conversation.
5. Update any references already written (the session pointer in `THREADS.md`, etc.).

### When auto-detect picks the wrong session file (multi-session situation)

Different shape from the wrong-YAML case. `sync-session.sh` picks in two stages: first the **source** JSONL (`$CLAUDE_CODE_SESSION_ID` when the harness provides it, otherwise the most-recently-modified JSONL in your project's folder), then the **destination** session file whose YAML `session_id` matches it. Only when no file matches does it fall back to today's most-recent dated file, and it says so (`⚠ Auto-detect: no session_id match — fell back…`). The failure to watch for is a wrong *source* pick under concurrency: with two sessions open and no env var, recency can choose the other session, sync it correctly into its own file, and report success while yours stays stale. Symptom: the "Target:" line in the script output names a file other than the one you expect, or the fallback lands on a file whose `session_id` names a JSONL that isn't in the project folder (a file created by Cursor, or a shell stubbed by hand). The common way to end up here: a Cursor session created today plus a Claude Code session continuing from yesterday.

**Fix**: bypass auto-detect by passing the explicit target file path as the wrapper's first argument:

```bash
bash Core/skills/sync/sync-session.sh /path/to/your-session-file.md
```

The wrapper then reads YAML from the explicit target (your `session_id`), finds the correct JSONL, and runs the canonical extract+splice into your file. No reinvention, no manual splice, no risk to the existing session file.

### Session files survive compaction

Even when AI hits 0% context and resets, the JSONL keeps the FULL history. Verbatim capture is guaranteed. **The JSONL on disk is append-only. It survives compaction completely.** Don't let compaction trick you into premature extraction. Working memory resets, but the session file keeps growing.

### JSONL parsing gotcha

`type: user` entries include BOTH actual user prompts AND tool_results returned to the assistant. A session with "32 user messages, only 4 unique" doesn't mean a loop. It means 4 user prompts + 28 tool_results. Filter on content type if you're trying to count human messages: `text` content = real user, `tool_result` content = tool response.

---

## Path A — Claude Code script usage (terminal or the Desktop app's Code tab)

```bash
# Refresh the LOG in this session's file (auto-detects by session_id)
bash Core/skills/sync/sync-session.sh

# Refresh a specific session file
bash Core/skills/sync/sync-session.sh Core/sessions/YYYY-MM-DD-HASH.md

# Or call the Python script directly
python3 Core/skills/sync/extract-session.py                       # stdout
python3 Core/skills/sync/extract-session.py SESSION_ID            # specific session
python3 Core/skills/sync/extract-session.py /path/to/file.jsonl   # specific JSONL
python3 Core/skills/sync/extract-session.py session-file.md       # idempotent .md write
```

**Shell wrapper**: `Core/skills/sync/sync-session.sh` handles YAML `session_id` parsing and finds the current session file. This is what `/sync` invokes.

---

## Path B — Claude.ai chat / other AI tools

No script needed. The human does the capture (you might need to nudge them). The AI formats for readability.

1. **Copy** the conversation from the AI interface (select all, copy)
2. **Create** a session file in `Core/sessions/` using the template above
3. **Paste** the conversation under `## LOG`
4. **Format for readability**: Human words in blockquotes (`>`), AI responses in plain text

That's it. The format matches what the extraction script produces (same archive, different source).

---

## After capture

Update the relevant task doc's SESSION INDEX so `/pickup` can find the session later:

```
**Session N (YYYY-MM-DD)**: [filename](Core/sessions/filename.md) — one-liner   ← repo-root-relative, never ../ (task docs move to Tasks/_done/ when finished)
```

---

## Quick reference

- **Destination**: `Core/sessions/{date}-{session-id-short}.md`
- **Script**: `Core/skills/sync/extract-session.py`
- **Wrapper**: `Core/skills/sync/sync-session.sh`
- **Source files**: `~/.claude/projects/{your-project-slug}/*.jsonl`
- **Survives context reset**: Yes, full history preserved
- **Task doc link**: SESSION INDEX points to session file
- **The test**: Could someone who wasn't here feel what this exchange was like?

---

## What is a "session"?

One JSONL = one session file, with numbered phases inside (LOG, LOG — Session 2, LOG — Session 3) when compaction or context-limit boundaries cross.

The philosophical question is interesting: compaction resets the thinking context. Post-compaction AI is a fresh instance with a summary, not the same thread. Are these the same session or different ones? The practical answer (same JSONL = same file) works. But the experiential answer is murkier — each phase has a different AI with different firsthand memory. **The record is continuous; the thinking isn't.**

---

## Deeper reference

For edge cases where `/sync` isn't enough: **`edge-cases.md`** — compaction boundaries, context-limit hits, hard-kill recovery, Cursor sessions, assembly verification.

---

## Skill Check (after every sync)

- Did the sync capture what was missing? (Tail-check, or trust the line-count delta.)
- Did the YAML `session_id` parse work, or did the script fall back to latest-by-mtime?
- Did invoking via the skill feel smoother than typing the bash command? (If no, either the skill has friction to fix or the skill wasn't needed.)

**If yes** → update this skill or the underlying script now. The improvement compounds.

**If no** → move on. Not every sync teaches something.
