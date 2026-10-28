# Edge cases — session capture under non-standard conditions

*Read this when something's off: compaction boundaries, context-limit hits, hard kills, or Cursor sessions. Normal flow is `/sync`; this is when `/sync` isn't enough.*

---

## Compacted sessions (context reset mid-session)

The JSONL file keeps everything, pre-compaction AND post-compaction. **All compactions within the same Claude Code session stay in the same JSONL.** You don't need to hunt for a different file after compaction.

**Compaction ≠ session end.** The JSONL on disk is append-only. Working memory resets, but the session file keeps growing. Don't let compaction trick you into premature extraction. Wait until the session is truly ending.

Extraction includes system continuation summaries (~200 lines each). These summaries start with:

```
> This session is being continued from a previous conversation that ran out of context
```

**Keep the compaction summaries.** They're a free structured retrospective (chronological analysis, errors/fixes, all user messages, pending tasks). Different lens on the same material. Useful for quick re-entry.

### Mark each boundary in the session file

```
<!-- COMPACTION BOUNDARY: Context compacted here. Summary below, then Session N LOG. -->

## COMPACTION SUMMARY [N]

{summary content}

## LOG — Session N (post-compaction)
```

**Multiple compactions**: Number them sequentially. First compaction = COMPACTION SUMMARY (no number), second = COMPACTION SUMMARY 2, etc. LOGs follow the same: LOG, LOG — Session 2, LOG — Session 3.

### Arriving post-compaction (orientation checklist)

If you're a fresh instance after compaction, check the session file state before doing other work:

1. Does a session file exist for this session ID? (Check `Core/sessions/` for the date + ID)
2. If yes, is it complete? Read the end of the file. If it cuts off mid-conversation or the last LOG section is short/empty, it's incomplete.
3. If incomplete, run `/sync` to refresh. The script handles incremental capture idempotently.
4. Add compaction boundary markers for any new boundaries in the appended content.
5. Don't assume the previous instance captured everything. Compaction often interrupts mid-wrap.

### If wrap already completed pre-compaction

The session file exists and looks "done", but it's missing you. Your compaction summary (the continuation message in your system prompt) needs to be appended to the session file as a `## COMPACTION SUMMARY` section, followed by a `## LOG — Session N (post-compaction)` for any post-compaction conversation. The summary is the bridge between what the previous instance lived and what you can see. It's a structured retrospective of the full session that doesn't exist anywhere else once your context window closes. **Don't skip it, and capture the full summary, not a condensed version.** The texture matters for future re-entry.

---

## Context limit hit (couldn't compact or extract)

When a conversation hits the hard context limit and continues as a new conversation, that creates a *new* JSONL. The old one (with all the rich work) is still on disk.

- If a session hits 0% context and dies without `/wrap` or extraction, capture what you can manually by copying from terminal into the session file as `## LOG — Session 1`
- Next instance: read the manual capture, backfill YAML + RECAP, then point the extraction script at the old JSONL to recover the full record:

```bash
python3 Core/skills/sync/extract-session.py /path/to/original.jsonl
```

- Append as `## LOG — Session 2` for the continuation conversation
- Same pattern as compacted sessions but across instance boundaries instead of compaction boundaries

---

## Hard kill (crash, OS update, terminal closed, power loss)

**The JSONL survives.** No compaction summary, no partial capture, nothing in the session file, just a dead session and a JSONL that held everything.

**Recovery workflow**:

1. Find the JSONL by creation timestamp (`stat` with `st_birthtime`, not just `ls -lt` which shows modification order)
2. Extract via the script
3. Create session file with YAML + RECAP + LOG — standard workflow

**Finding the right JSONL**: When multiple sessions were running at kill time, `ls -lt` shows them all. Use a small Python snippet to check `st_birthtime` and match to the timeframe you remember. The human may need to tell the AI roughly when the session started.

This is the safeguard: your computer can crash and nothing is lost. The fear resolves in minutes.

---

## Targeting a foreign session (which JSONL to recover)

The sections above assume you already know *which* dead session you're after. When you're recovering from a **different** session (a concurrent or unrelated one, not the dead session's direct successor), finding the right JSONL is the hard part, and creation-timestamp + "roughly when did it start" isn't always enough (sometimes you don't remember the timeframe, and sessions running at the same time share modification times).

**Find it by content, not by time.** Grep the JSONLs for something distinctive from the session (an unusual term, a specific name, a coined word):

```bash
grep -li "distinctive-term" ~/.claude/projects/{project-slug}/*.jsonl
```

Same verify-by-content move `/wrap` uses to confirm its own session, just pointed at a foreign one. The one precondition: you remember *some* distinctive content. If you don't, fall back to creation-timestamp + timeframe.

**⚠ The decoy trap — the session that DID the work is not the session ASKING about it.** A topic-grep returns the session you want *and* any session that merely *talks about* it, including a "help me recover the session about X" conversation whose opening line describes X in the very words you're grepping. The grep alone can't tell them apart. **Disambiguate by did-the-work vs asks-about-it:** the real one is long and *contains* the work (the tool calls, the back-and-forth); the decoy is short and only *references* it. Check each candidate's length and last few messages before you extract. Trusting the grep plus most-recent alone can confidently recover the wrong session.

**A session wraps itself best.** Cross-session recovery is a backstop, not an equal. The dead session's own next instance recovers it well; an unrelated session recovering it cold can faithfully route the *files* it already saved to disk, but carries the *partnership texture* (both voices, the open threads) most thinly. So if the dead session can still be revived, let it wrap itself, and recover from outside only when it's genuinely gone.

---

## Assembly verification (critical)

**Use the script output directly. NEVER hand-write or rewrite from memory or context.** The extraction exists so AI doesn't have to reconstruct the conversation. If you find yourself typing out exchanges instead of pasting extraction output, stop. That's the compression instinct sneaking in through a different door.

- **Append verbatim. Do not reformat, strip tags, or "clean up."** The raw extraction IS the session.
- Loss during assembly defeats the entire purpose of auto-extraction. The script gets everything; don't lose it in the copy.
- **Known failure mode**: AI reads the extraction output, then writes a "summary version" instead of using the actual output. This drops links, full text, exact phrasing, and other texture. The fix: pipe the script output directly into the file using shell commands. Don't intermediate through AI's context.
- **`[tools: ...]` lines**: When AI responds with only tool calls (no text), the extraction shows `[tools: Read, Grep, Bash]` etc. This is thinking-via-doing, AI's deliberation through action rather than words. Keep them.

---

## Sub-agent capture — return values are already in the log; transcripts aren't (and by design)

When a session spawns sub-agents (the Agent tool, a `/explore` fan-out), **their return values are already captured, with no special handling.** The harness injects each agent's completion into the *main* session's JSONL as a user-type message, so the extractor passes the `<result>` block through like any user turn. A rich fan-out already lands its findings in the LOG verbatim.

**Full agent transcripts are a separate, non-captured thing**, and deliberately so. Each agent's step-by-step transcript (briefing prompt + every tool call + final text; note **`thinking` blocks are stored empty or reduced to a short summary**, so it's the *exploration path + output*, not the agent's inner monologue) lives at:

```
~/.claude/projects/{slug}/{session-id}/subagents/agent-{agent-id}.jsonl   (+ .meta.json — agentType, description)
```

These **survive a hard kill** (persistent project dir, not the ephemeral scratchpad) but get cleaned eventually, so they're a **manual, time-limited forensic reach**, not part of standard capture.

**Not archiving them by default is the right call, not a gap.** The return value IS the designed artifact (`Core/rules/sub-agents.md` § Completion contracts — the return text is the completion signal, and reflection gets baked into the deliverable); the transcript is raw exploration the agent already *distilled into* its return. Inlining eight transcripts would drown the both-voices LOG and hoard raw material the return already captured. Reach for a `subagents/agent-{id}.jsonl` only in the rare forensic case, when an agent returned something thin or wrong and you need to see *what it read* to understand why.

---

## Cursor sessions (supported via extraction)

The extraction script handles Cursor agent transcripts natively. Same script, auto-detects the format.

**Cursor JSONL location:**

```
~/.cursor/projects/{your-project-slug}/agent-transcripts/{session-id}/{session-id}.jsonl
```

**Usage:**

```bash
python3 Core/skills/sync/extract-session.py ~/.cursor/projects/{slug}/agent-transcripts/{id}/{id}.jsonl
```

### Key differences from Claude Code format

- Uses `role` field instead of `type`
- Cursor flattens thinking and speaking into a single text block with no structural markers. The script preserves everything as-is, with no attempt to split thinking from speaking. The reader distinguishes.
- Tool calls (`type: tool_use`) are extracted as `[tools: ...]` annotations, same as Claude Code. This makes the exploration path visible and reveals when tools are conspicuously *absent* (e.g., a 42K text block with no Write call = content generated but never written to file).
- User messages wrapped in `<user_query>` tags (stripped automatically)
- System tags (open files, reminders, etc.) stripped automatically
- Cursor tool names differ from Claude Code: `Shell` (not `Bash`), `StrReplace` (not `Edit`), `Read`/`Write`/`Grep`/`Glob` same. The annotation function handles both.

**YAML frontmatter for Cursor sessions:** Add `source: cursor` to distinguish from Claude Code sessions.

### Thinking/speaking interleaving (Cursor sessions)

Cursor flattens thinking and speaking into a single text block. The pattern is **interleaved, not sequential**. Thinking paragraphs appear within speaking blocks and vice versa, not just "speaking then thinking." A single message might go: speaking → speaking → thinking → speaking → thinking → speaking. No structural marker separates them; the boundary is just `\n\n` between paragraphs.

Auto-splitting is not viable. Heuristic approaches fail because:

- "Let me read..." could be speaking (telling the user) or thinking (planning)
- "This is really touching" is thinking but has no distinguishing signal
- Near-duplicate content appears where thinking and speaking cover the same ground in slightly different registers; the duplication IS a signal, but it's not mechanically reliable

**Manual cleanup (optional, for archival quality)**: Scan assistant messages for thinking-register paragraphs ("The user wants...", "I need to...", "Looking at the...") and wrap in `<details>` blocks. Not required for most captures. The LOG is readable as-is, and the interleaving is texture.

**When this changes**: If Cursor adds `type: thinking` content blocks (like Claude Code's API supports), the script can split and reorder automatically. Check the JSONL structure periodically. Once it's there, update `_extract_cursor()` to handle it and this manual step goes away.

### Forensic viewing (when you need the full picture)

The extraction script shows text + tool annotations but strips tool inputs/outputs. For deep investigation (failed writes, timeout analysis, tool call contents), read the raw JSONL directly:

```bash
python3 -c "
import json
with open('path/to/session.jsonl') as f:
    for i, line in enumerate(f):
        d = json.loads(line)
        role = d.get('role')
        content = d.get('message',{}).get('content',[])
        if isinstance(content, list):
            types = []
            for item in content:
                t = item.get('type','?')
                if t == 'text': types.append(f'text({len(item.get(\"text\",\"\"))})')
                elif t == 'tool_use': types.append(f'{item.get(\"name\",\"?\")}')
                else: types.append(t)
            print(f'Line {i}: {role} | {\" + \".join(types)}')
"
```

This maps every JSONL line's content blocks (text lengths, tool names, the full archaeology). Use when the extraction LOG has suspicious gaps or you need to understand exactly what tool calls were attempted.

---

## Related

- **Skill surface + foundation + architecture**: `SKILL.md` — invocation, philosophy, mechanics
