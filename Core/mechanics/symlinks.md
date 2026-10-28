# Symlinks

Knowledge lives in `Core/`. Tools point to it.

---

## The pattern

Every AI tool invents its own convention for finding instructions (`.claude/`, `.cursor/`, `.whatever/`). They all solve the same problem: "where does the AI get its context?"

So put the knowledge in one universal place and let each tool *symlink* to it. A symlink is just a pointer, a file (or folder) that says "look over there." The real content lives in `Core/`; the tool's directory holds pointers to it. The tool serves the knowledge, not the other way around.

This is what keeps your system tool-agnostic: switch tools tomorrow and your thinking doesn't move, only the pointers do.

---

## How symlinks stay in sync

**Automated, via a hook.** The `ensure-symlinks.sh` script runs on SessionStart and after every Write/Edit. When you add a new skill or rule under `Core/`, it gets a symlink into `.claude/` automatically, with no manual step. (It also creates the System Compass and Auto-Memory links on first run.) See `Core/mechanics/hooks.md` for how it's wired.

**Manual** (for one-off symlinks, or if you're on a system without the hook):

1. Create the source file in its canonical home (`Core/rules/`, `Core/skills/`, etc.)
2. Make a symlink from the tool's convention directory:
   ```bash
   cd .claude/rules/   # (or .claude/skills/, .cursor/rules/, etc.)
   ln -s ../../Core/rules/filename.md filename.md
   ```
3. Verify it resolves: `ls -la .claude/rules/filename.md` (an arrow `->` means it's pointing correctly)

---

## What points to what

### System compass
`.claude/CLAUDE.md` -> `../AGENTS.md`

Claude Code auto-loads `.claude/CLAUDE.md` at startup. It's a pointer to the tool-agnostic `AGENTS.md` at your repo root, so the compass any tool reads and the compass Claude Code reads are the same file.

### Skills
`.claude/skills/{name}` -> `../../Core/skills/{name}` (one directory symlink per skill)

Each skill is a folder under `Core/skills/` (`add/`, `explore/`, `wrap/`, and so on). Claude Code discovers skills by looking in `.claude/skills/`, so each skill folder gets a symlink there. Add a new skill folder under `Core/skills/`, and the hook symlinks it on the write, so it shows up as a slash command in the session you made it. *(New **rules** differ: the symlink is immediate too, but rules auto-load at session start, so a new rule takes effect next session.)*

**The generalizable principle**: a system's source-of-truth shape doesn't have to match the shape a tool wants to load. The source layer (where you and the AI reach for things) is organized for *you*; the registry layer (what the tool consumes) is organized for the *tool's* discovery rules. Don't conflate them. Let symlinks bridge the two.

**A skill is symlinked as a whole FOLDER, not file-by-file.** `.claude/skills/{name}` is a directory symlink to `Core/skills/{name}`, so *every file inside* (`SKILL.md`, helper scripts, templates, briefs) is shared automatically. There's only ever **one real file** per asset. Two things follow from that:

- **Don't try to edit "both copies" of a helper script.** A file like `.claude/skills/add/helper.py` and `Core/skills/add/helper.py` are the *same file on disk* (same inode) reached by two paths, so one edit changes both. Trying to edit the "second copy" fails (it was already changed). The canonical home is `Core/`; reach for it there.
- **A new file dropped into `Core/skills/{name}/` shows up in `.claude/` for free**, no separate symlink, no extra step. Add it under `Core/`, it's live in `.claude/` immediately. (This is the flip side of the same fact: the whole skill folder is one symlink, so anything inside rides along.)

### Rules
`.claude/rules/*` -> `../../Core/rules/*`

Every rule file is symlinked 1:1. Claude Code auto-loads everything in `.claude/rules/` at session start, so your rules are ambient context from the first message.

### Auto-memory
`Core/auto-memory/` -> `~/.claude/.../memory/` (directory symlink)

This one reaches *outside* the repo, into Claude Code's global config location for memory. A directory-level symlink surfaces the whole auto-memory folder (the `MEMORY.md` index plus individual entries) so you can browse it from inside your system instead of hunting in `~/.claude/`. See `Core/mechanics/memory-setup.md` for the full setup.

---

## Cloud-synced folders — where a symlink can point

If your system folder lives inside iCloud Drive (for example `~/Documents` with Desktop & Documents sync turned on), know that **iCloud Drive doesn't sync data *through* a symlink**. The link works on the Mac that made it and fails on every other device, because the cloud layer ignores the pointer rather than following it. (That's widely reported by users rather than documented by Apple, and other sync services behave differently, so check yours before relying on a link to travel.)

So the direction of the link matters:

| shape | example | status |
|---|---|---|
| inside your system → inside your system | the links in `.claude/` | fine, but not because the link syncs: the hook recreates these on every machine at session start |
| inside the synced folder → outside it | `Core/auto-memory` → `~/.claude/…/memory` | works on this machine, doesn't travel |
| inside the synced folder → elsewhere in the synced folder | your system → a sibling `ARCHIVE-OS/` | don't: this is the case that fails (nothing recreates it on the other device) |

Concretely: `Core/mechanics/archiving.md` puts `ARCHIVE-OS` beside your system as a peer folder, and linking it into your system is tempting. If both live in iCloud, don't; refer to the archive by its own path instead.

---

## Bulk-substitution gotcha (sed/find across symlinked directories)

**Sweep hygiene first: filter, never blanket-sed the whole tree.** *(Commands below are macOS/BSD `sed`; GNU `sed` takes `-i` with no argument.)* **(1) `sed -i ''` rewrites every matched file even when it changes nothing**, which touches every file's modification time; if a sync client watches the tree (iCloud, Dropbox) that means a full re-sync and sometimes `filename 2.md` **conflict copies**. **Fix: match first** (`grep -rl 'PATTERN' … | tr '\n' '\0' | xargs -0 sed -i '' 's/…/…/g'`), so only files that contain the pattern get rewritten. **(2) A batched `-exec sed {} +` fails on the first symlink** in the batch (your `.claude/*` links): `sed` refuses with *"in-place editing only works for regular files"* and none of that batch changes. Easy to miss in a long run → add `-type f -not -path '*/.claude/*'`.

When you run a bulk find-and-replace (`find … | xargs sed`, or similar) across a directory that's actually a *symlink target*, **verify the real file directly afterward**, because the recursion may not pass cleanly through the symlink.

The trap: a sweep can report "matched and replaced everything" while the canonical file behind the symlink still holds stale matches. The replace *looks* done; it isn't. One mechanism behind this is `find`'s documented default, measured against the real binary:

```bash
/usr/bin/find Core/auto-memory  -name MEMORY.md   # 0  ← symlink named as start point, no slash
/usr/bin/find Core/auto-memory/ -name MEMORY.md   # 1  ← trailing slash DOES descend
/usr/bin/find -H Core/auto-memory -name MEMORY.md # 1  ← -H does too
/usr/bin/find . -name MEMORY.md                   # 0  ← tree-wide: never reaches it
```

**`find` never follows a symlink it meets *during* traversal, and follows one named as a *starting point* only if the path carries a trailing slash or you pass `-H`/`-L`.** The fix is that small: add the trailing slash, or pass `-H` (or `-L` to follow every link in the tree).

**Which links this bites: only ones pointing *out* of your system with an absolute path.** The `.claude/` links are relative and point *into* `Core/`, so a sweep of `Core/` already covers what they reach. In the starter the one outward link is `Core/auto-memory` (→ Claude Code's memory folder), and it's the costliest to leave stale, because `MEMORY.md` loads every session. List yours any time with: `find . -type l | while read l; do case "$(readlink "$l")" in /*) echo "$l";; esac; done`

**Discipline**: after bulk-substituting across a symlinked directory, post-verify by grepping the **canonical (non-symlinked) path** for the pattern you tried to remove. If matches remain, run the substitution against the canonical path directly. The same caution applies to any tool that walks directory trees: `rg`, custom scripts, anything recursive.

**And if you're checking how a tool treats symlinks, check the real one.** Inside Claude Code, `grep` and `find` may be wrappers that behave differently here (one of them follows a symlinked directory where the real `grep` doesn't). See `Core/mechanics/claude-code.md` § Pro tips.

**Doesn't apply to**: single-file edits through a symlink (those pass through fine), reads through a symlink, or normal Edit/Write tool operations.

---

*Zero content in tool directories. All the knowledge lives in your system.*
*For the full philosophy: `Core/foundations/tool-agnostic.md`*
