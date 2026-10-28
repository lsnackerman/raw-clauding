# Working in Claude Code

*Day-to-day Claude Code: starting, ending, permissions, diffs, the things you'll wish someone had told you. The USER-GUIDE covers the universal stuff; the setup guides get you wired up once. This system runs in the **Claude desktop app's Code tab**, so that's the spine of this doc. Running Claude Code in a terminal instead? Same engine, different controls: § In a terminal instead, at the end.*

---

## In the Code tab

### Starting, ending, coming back

**Start.** Open the Claude app, click the **Code** tab, and your folder is already there from setup (if not: the folder control next to the environment selector). **+ New session** in the sidebar (or `Cmd+N`, `Ctrl+N` on Windows) opens a fresh session in the same folder. Type what you're thinking about and press Enter. The AI reads your `AGENTS.md`, your rules and `MEMORY.md` and shows up oriented; `/pickup` is what brings in the handoff (ALIVE, PULLING, THREADS).

**End.** One move: **`/wrap`**. It captures the session to `Core/sessions/`, updates ALIVE and THREADS, and hands off to next-you. After that, leave the session where it is, archive it, close the app. **Nothing is lost.** The conversation lives in your files, not in the window.

**Come back.** New session, same folder, `/pickup`. The AI reads the handoff and picks up where you left off.

What stays, because the files ARE the persistence: your system folder (Core/, Library/, Projects/, Tasks/, the root `.md` files), the session files in `Core/sessions/`, everything markdown. What doesn't matter: the window, the sidebar entry, any summarized view of the conversation.

### Auto, Manual, and where the partnership lives

Your system starts on **Auto**: the AI works without stopping to ask about each step, with safety checks running in the background, and you read what changed afterwards. That's the default Anthropic ships with now, and staying on it keeps raw-clauding as easy as possible for everyone. Prefer to stay closer to the edits and approve each one before it happens? Switch to **Manual** (the permission mode, next to the send button; the other modes there are for other kinds of work). In Manual, each edit or command waits for you in the conversation before it runs: approve it, or type what you'd rather it did.

Either way, **the partnership isn't the approve button.** A prompt you click through without reading is the executor relationship with extra steps. What matters is where your attention goes:

- **Read the diffs.** Click the `+12 -1` counter in the Changes card after it edits. **Green = added, red = removed. Read the red**: that's what you gave up.
- **Steer as it goes.** Type a correction any time. Or hover a line in the diff, click the `+`, leave a comment; after commenting on several lines, `Cmd+Enter` (`Ctrl+Enter` on Windows) sends them all at once.
- **Ask why.** *"Why did you do that?"* gets a real answer, and that's the two of you calibrating.
- **Draw one hard line early: anything you can't undo.** Sending, deleting, publishing, spending. Tell the AI: *"check with me before anything you can't undo."* That's an agreement between you, not a lock, so say it anyway.

### Stopping and steering

- Going the wrong direction mid-response? The **stop button**, or **Esc**. Then say "wait," ask a question, redirect. Claude Code is a conversation, not a pipeline; if something feels off, stop and say so (that's partnership mode).
- Stuck retrying during an API overload? Stop it, wait a few minutes, try again. Letting it retry ten times just burns through the queue.
- You're never trapped. Stop is always available.

### Showing it things

Drag a screenshot, a photo, a diagram, or a PDF into the prompt box (or use the **+** button next to it). *"Here's what my screen looks like"* or *"here's the error"* is faster than describing it.

### Switching models

The model picker sits in the same row as the permission mode, and you can change it mid-session. Which model when → `Core/practice/which-model-when.md`.

---

## Slash commands

Skills are invoked with a slash. Type `/` in the prompt box and the list appears: built-in commands, plus every skill in `Core/skills/`.

- `/add` — add something to your library (a URL, a PDF, a podcast, an article, a film)
- `/sync` — refresh the captured conversation log (idempotent)
- `/wrap` — end a session intentionally
- `/task` — create a task doc from a sentence
- `/pickup` — resume a thread with full context
- `/gut` — pressure-test an idea
- `/fresh-eyes` — get a cold read from a fresh instance, outside the loop
- `/floor` — open the floor for the AI's curiosity
- `/explore` — search across your system
- `/pulse` — step back and scan the whole system for what's alive
- `/tune` — hold external input or friction against the system
- `/universal` — test if something is ready to share

Type the command and the AI does the rest. The skill file has the instructions; you stay in the thinking.

**In other tools** (Claude's Chat tab, another editor's built-in agent, etc.), you share skill files directly in conversation. Paste or reference the skill markdown and the AI follows it.

---

## Commands you'll see

Claude Code runs terminal commands as part of its work, whichever way you run it. You don't need to memorize these. Just know enough to read what the AI is doing when it shows you a command or asks for permission.

| Command | What it does | Example |
|---------|-------------|---------|
| `ls` | Lists files in a folder | `ls Projects/` |
| `cd` | Goes to a folder | `cd ~/my-system` |
| `mkdir` | Makes a new folder | `mkdir Core/sessions/` |
| `cat` | Shows a file's contents | `cat AGENTS.md` |
| `pwd` | Shows where you are | `pwd` → `/Users/you/my-system` |

---

## Context window

Your conversation has a context window, and it fills up. When it does, Claude Code summarizes the conversation so far and keeps going (that's **compaction**), and you may not get a notice. This is normal. It's why we capture sessions: nothing is lost when the live window is squeezed or when you start a new one.

Compaction manages the live window; capture preserves the record. They're different systems. The session file on disk is untouched by compaction, and the extraction script reads from disk, not from memory. If the window feels thin after a compaction, `/sync` refreshes the file and `/pickup` re-orients you from it.

---

## Setup notes

The setup guide had the AI run this once, from your system folder:

```bash
bash Core/scripts/ensure-symlinks.sh --check
```

It creates the symlinks that connect your skills, rules and `AGENTS.md` to Claude Code's `.claude/` folder, copies the hook config into `.claude/settings.local.json` (from the template in `Core/scripts/`), and from then on the hooks keep things in sync: add a new skill or rule and the symlink appears on its own. `--check` makes it print the summary and exit non-zero on failure even when the AI runs it for you; without the flag a run from inside Claude Code can succeed or fail silently, and you can't tell which. Re-run it any time you wonder whether setup is wired.

**Auto-memory** is part of the same run. The script creates `MEMORY.md` in Claude Code's native auto-memory location, seeds it, and symlinks the whole directory into your system at `Core/auto-memory/`, so the index and the individual memory entries are browsable beside your other `Core/` clusters. `Core/mechanics/memory-setup.md` has the plumbing if you ever need to redo it.

---

## Pro tips

Things you'll wish someone told you on day one. These hold in the Code tab and in a terminal.

### Nothing is lost to compaction

When your context window fills up and the conversation gets summarized, it feels alarming the first time. Your session file on disk is untouched. The full conversation is always there.

### An API error after a diff usually isn't lost work

If you saw an edit's diff and then an API error, check the file before redoing anything. In our experience the edit has usually already landed; redoing it makes a second copy of the change.

### A long file can look "done" before it's done

When the AI reads a file too big for one pass, it reads in chunks, and a clean section break (a `---`, a blank stretch) can look like the end. If it declares a long file "complete" and the summary feels thin for the size, have it check: did the last read actually reach the end? (`wc -l`, or "what's the total line count vs. where you stopped?"). Separators are formatting, not file boundaries. The extra check costs seconds; missing two-thirds of a file costs rework.

### The AI's `grep` and `find` may not be the real ones

Inside Claude Code's shell, `grep` and `find` can be shell *functions* that Claude Code injects, handing off to bundled search tools (ugrep and bfs) instead of your system's binaries. For ordinary searching that's fine, and faster. It bites in two places. First, a recursive search can come back **quietly narrower** than you asked, because the wrapper skips ignored and binary files. Second, **any check of how a tool behaves measures the wrapper**, not the tool it's named after. This depends on your Claude Code version, so check rather than assume: have the AI run `type grep` and `type find` (`which` from a separate terminal reports the real binary, because the functions only exist inside Claude Code's shell). If they come back as functions, re-run anything load-bearing (a completeness check, a "does this exist anywhere," a claim about what `find` does) against the real binary: `/usr/bin/grep`, `/usr/bin/find`.

### Changed a rule? Start a new session to test it

Claude Code loads rules when a session starts. If you edit one and test it in the session you're already in, you're testing the OLD version, and you'll chase ghosts wondering why your change "didn't work." Start a new session (**+ New session** in the sidebar; `/exit` then `claude` again in a terminal), then test. No app restart needed. This catches a lot of people debugging phantom issues that were never issues. (Hook and settings edits are picked up live by Claude Code's file watcher, and a new skill is callable the moment the symlink hook links it; rules are the ones that need the new session.)

---

## In a terminal instead

Everything above holds. These are the controls that differ.

**Start:** open a terminal, `cd ~/your-system-folder`, type `claude`, Enter. **End:** `/wrap`, then `/exit` (or `Ctrl+D` twice). Close the terminal whenever after that; the files hold everything. **Come back:** `claude` in the same folder, `/pickup`.

**Install:** the Claude Code docs at code.claude.com cover the terminal install for each OS (the setup guides don't, since they're written for the app).

**Permission prompts** (Manual mode, or anything Auto still asks about) are text. **Yes** is the first option. **Tab is your superpower**: with Yes or No focused, it opens a comment field; type "but rename that variable" or "do the same to the other file too," and Enter sends your answer with the note attached. That's the difference between rubber-stamping and collaborating. **Esc** declines, and Tab on No lets you say why.

**Diffs** show inline in the conversation as each edit lands. There's no counter to click and no line comments, so you steer by typing, or by Tab on the prompt in Manual.

**Esc stops everything** mid-response, same as the stop button. `Ctrl+C` interrupts a running operation (pressed twice with nothing running, it exits).

**Showing it things:** drag an image file into the terminal window, paste one with `Ctrl+V`, or give it the file path.

**Switching models:** `/model`.

---

*This doc grows as you learn. Add your own tips, gotchas, and patterns here.*
