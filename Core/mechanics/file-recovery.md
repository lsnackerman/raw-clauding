# File recovery — Claude Code's file-history backup

If a file unexpectedly reverts or work feels lost (a stale-buffer overwrite from another editor, an accidental save-over, etc.), Claude Code's file-history snapshots are your safety net. Every Edit/Write operation creates a versioned backup automatically, so even when something gets clobbered, an earlier good version is almost always sitting on disk.

---

## First: confirm snapshots exist on your setup

The snapshot location is **version- and config-dependent, so don't assume it's there.** Check before you rely on it:

```bash
ls ~/.claude/file-history/ 2>/dev/null && echo "✓ snapshots on" || echo "✗ no file-history — see fallbacks"
```

- **Folder exists, with session-named subfolders** → you're covered; continue below.
- **Folder missing** → some Claude Code versions/configs don't keep file snapshots here (you may see only `~/.claude/backups/`, which holds *config*, not file versions). This recovery path won't run as written. Fall back to your **editor's local history** (Cursor / VS Code "Timeline" view), **git** if the project is versioned, or **iCloud / Time Machine**. Worth confirming *before* you need it, not during a panic.

---

## Where snapshots live

`~/.claude/file-history/{session-id}/`

- One folder per Claude Code session (UUID-named, matches the session ID in `~/.claude/projects/`)
- Inside: files named `{content-hash}@v{N}` — each version of each file Claude touched in that session
- Different files = different content hashes; multiple versions of the same file = an incrementing `v{N}` per edit

## Finding the right backup

**1. Identify the session.** The current session's UUID is logged in the JSONL trail at `~/.claude/projects/{project-key}/{session-id}.jsonl`. To find the most recent activity:

```bash
ls -lat ~/.claude/file-history/ | head -5
```

**2. Find the file's hash by CONTENT, not by size or date.** Matching on size and modification time fails twice over: the newest snapshot is your *current* file (so it's never the one you want), and a batch of edits can land several files on one timestamp.

```bash
H=~/.claude/file-history/{session-id}
grep -rl "a distinctive line from the file" $H          # find the hash
ls -v $H/{hash}@v*                                      # the chain, oldest → newest
```

**The chain is a complete version history: for N edits you get N+1 states, and the newest is byte-identical to what's on disk.** So pick by diffing against what you have. The version you want is the newest one that *differs*:

```bash
for v in $(ls -v $H/{hash}@v*); do
  cmp -s "$v" /path/to/file && echo "$v  == current" || echo "$v  DIFFERS"
done
```

**The last `DIFFERS` is your undo-the-last-edit candidate.** Everything below it walks further back.

**3. Verify before restoring.** Spot-check that the candidate version has the content you expect:

```bash
grep -n "expected-marker-text" ~/.claude/file-history/{session-id}/{hash}@v{N}
```

## Recovery

```bash
cp ~/.claude/file-history/{session-id}/{hash}@v{N} /path/to/original/file
```

That's it. The snapshot becomes the file. This kind of recovery turns what could be hours of reconstruction into a single `cp`.

---

## Reading the chain as a time series — and its deadline

This doc is named for recovery, so the store only gets reached for when something broke. But the chain holds every state of every file the AI edited, which answers a different class of question: **how did this file change over time?** What did this rule say a month ago? When did this doc double in size? Nothing about the word "recovery" will make you reach for it for that, so it's named here.

Two facts make it work:

- **The hash is per-path, not per-content.** One file's whole history shares one hash across every session, so a grep for its H1 finds the entire chain in one shot: `grep -rl "^# Some H1$" ~/.claude/file-history`. A file that **moved or was renamed gets a new hash**, so its chain breaks at the move; stitch the two by hand.
- **Session folders date themselves against your own session files.** The first segment of a folder's UUID is the short hash in `Core/sessions/{date}-{short-hash}.md`. Where no session file exists, the folder's modification time is the fallback.

**To reconstruct a file as of date D:** take the last snapshot dated on or before D; failing that, take the **earliest `v1` after D**, the pre-image of that session's first edit, which is still the file's state at D *provided nothing edited it in between*. Say which rule you used; they aren't equally strong.

Three traps:

1. **Absence means no snapshotted edit, not no change.** A file with no snapshot in the window had no `Edit`/`Write` from the AI directly, but sub-agent edits leave no snapshot and shell mutations don't reliably trigger one (see § Prevention), so check whether any ran before reading absence as "unchanged." If none did, the file's state at D is the earliest later `v1`, or the current file if there's none. Read as missing data, it silently drops a row.
2. **A pre-image can post-date the file's creation.** If the file didn't exist at D, its earliest `v1` is a post-creation state, and the honest value at D is "didn't exist yet." Check the file's own origin date.
3. **Parallel same-day sessions interleave**, so two folders can hold overlapping versions of one file. Across days the order is clean; within a day it needs care.

**⚠️ It is pruned.** Old session folders disappear from this store. How long it keeps them, and what does the pruning (age, count, size, a setting), isn't documented, so don't assume a window. Check yours: `ls -ltr ~/.claude/file-history | head -3` shows the oldest folders you still have. The consequence: **any historical question this store can answer, it can only answer for a while.** When you find one worth answering, extract the data into a file in your system now; don't leave a note telling future-you to go look. A pointer at a store that's being pruned isn't a capture (`Core/rules/persist-before-pause.md`).

---

## What causes reverts (so you can prevent the next one)

- **Stale editor buffer**: if another editor (Cursor, VS Code, etc.) had the file open *before* Claude edited it on disk, that editor's buffer is now stale. A later save, manual or auto, writes the stale buffer over Claude's edits. This is the most common cause.
- **"Close without saving" can still revert**: closing in another editor without saving doesn't *itself* touch disk, but that editor's auto-save (if enabled), or any later save from a stale buffer, will overwrite Claude's work.
- **Concurrent edits in two tools**: editing the same file in another editor while Claude Code also edits it sets up race conditions, even within the same session.

## Prevention

- **Trust the conflict prompt.** When your editor warns about external changes ("file changed on disk"), accept Claude's version unless you've made manual edits worth keeping.
  - **The words you'll actually see on screen: "revert block" / "accept block".** Cursor shows the difference as hunks with a button on each. **"Revert" throws away the change in that block and restores what your editor's buffer had**, which in the stale-buffer case means *discarding the AI's edit*. So when a file "is different," revert is usually the wrong button, and the section above is why.
- **Save manually before stepping away.** A manual save syncs your editor's buffer to the current disk state, eliminating stale-buffer risk for the next operation.
- **Use one editor at a time on the same file.** If Claude is actively editing a file, close it in your other editor (or vice versa) until the edit completes.
- **Trust the file-history backup, within its bounds.** Even when prevention fails, a snapshot exists for every `Edit` and `Write` the AI makes directly in the session. Two things it does *not* cover: edits made by a sub-agent the AI dispatched (those leave no snapshot at all), and changes made through shell commands (`sed`, a redirect, a script). That's one more reason to have agents return their work for the AI to apply (the return-text contract, `Core/rules/sub-agents.md` § Completion contracts: when the AI applies the returned work itself, that edit creates the recovery point the agent's own edit never would), and to prefer `Edit`/`Write` over shell mutation.

---

## Sister references

- `Core/mechanics/hooks.md` — hooks fire on Edit/Write, which is also when file-history snapshots get created (same trigger)
- `~/.claude/projects/{project-key}/{session-id}.jsonl` — the parent session trail, including which files were edited when. Sub-agent transcripts aren't in it (their returns are); each agent's own transcript lives in the sibling `{session-id}/subagents/` folder.
