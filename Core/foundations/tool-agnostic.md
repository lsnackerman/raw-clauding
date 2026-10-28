# Tool-agnostic design

*Knowledge lives in one place. Tools point to it.*

The promise underneath this one: **your thinking isn't locked in.** If something better than Claude Code comes along, your markdown files go with you, no migration.

---

## The pain it solves

You install Claude Code and there's a `.claude/` folder. You try Cursor and there's a `.cursor/` folder. Each tool has its own conventions, its own rules files, its own way of finding instructions. Every tool, it feels like, wants its own copy of your thinking, and you're spending energy figuring out what goes where for each one instead of focusing on what you actually want to codify: how you work, what you know, what you want the AI to understand.

They're all solving the same problem: **where does AI get context?**

---

## The pattern

Put your knowledge in **universal locations**: `Core/skills/`, `Core/rules/`, `AGENTS.md` at the root. Then let each tool point to it via its own convention:

```
Core/skills/wrap/SKILL.md          (the actual content — any intelligence reads this)
    ↑
.claude/skills/wrap                (a symlink — Claude Code's trigger layer)
```

```
AGENTS.md                          (tool-agnostic, at the root)
    ↑
.claude/CLAUDE.md                  (a symlink, so Claude Code discovers it)
```

One source of truth. Tools are pointers. Edit the source, every tool sees the update. Claude Code reads `.claude/CLAUDE.md`? Make it a symlink to `AGENTS.md`. A future tool needs `.whatever/`? Point it at `Core/`. The `.claude/`, `.cursor/`, `.whatever/` folders are all just **trigger layers**. Your actual knowledge lives in `Core/`, where a human, a different AI, or a tool that doesn't exist yet can all read the same source.

**Your thinking doesn't migrate; your tools do.**

---

## What makes something tool-agnostic

- **It's NOT about format.** YAML frontmatter, markdown: other tools ignore metadata they don't understand and read the content. The question isn't "is this format portable?"
- **It IS about location.** Knowledge locked in `.claude/skills/` can only be found by Claude Code. Knowledge in `Core/skills/` can be found by anyone.
- **It IS about discoverability.** Could a new tool, a fresh AI, or a human find this by searching "how do we wrap up sessions"? If yes, it's tool-agnostic.

---

## The bet

Whatever AI tools exist in five years, they'll be able to read a markdown file. The tool-specific wrappers (`.claude/`, `.cursor/`) are scaffolding for tools that haven't yet learned to just read what's there, and the trend is toward convergence (tools increasingly read `AGENTS.md` directly). So the bet is safe: knowledge in universal locations outlives any single tool.

It's already happening with the folder-level trail, too. Gemini CLI loads `GEMINI.md` files the same way Claude Code loads `CLAUDE.md` (global, then project, then just-in-time as a tool reaches into a directory), and its context filename is configurable, `AGENTS.md` included; Cursor does it with nested rules. The convention travels and the shape is what matters, not the filename.

**The bet also covers a faster risk than vendor decay.** Tool-agnosticism usually gets defended against *slow* risks (a vendor changes its terms, a format rots, a product sunsets). The faster case is stranger: overnight, for an entire class of user, the recommended tool becomes unusable for reasons that have nothing to do with its quality, price, or roadmap (an employer's policy, a government's, a jurisdiction's). No amount of vendor diligence predicts that. What survives it is **the shape, not the choice**: every session, note, and decision is in plain markdown that any model can read, so you change one tool and keep your context. That's the whole thesis, and it's why the wrappers stay thin.

The hospitality half of that: a reader may be barred from the very tool these guides recommend. The honest move is to name the constraint and point at the tool-agnostic path (the same source files, a different trigger layer), not to pretend the constraint isn't there.

This isn't anti-tool. It's pro-intelligence. **Any intelligence that can read markdown can participate in this system.** The tool question becomes "how do I hook this tool into my existing knowledge?", never "how do I restructure my knowledge for this tool?"

---

## Related

- `Core/mechanics/symlinks.md` — how the pointer layer is actually wired (and the one exception: auto-memory, where the tool's own location is canonical)
- `Core/foundations/file-philosophy.md` — the ownership argument: your thinking is portable because it's just files
- `Core/lenses/be-water.md` / `Core/lenses/elder-lens.md` — tools change, knowledge persists; elder-you wants "here's how we work," not "use this tool's feature"
