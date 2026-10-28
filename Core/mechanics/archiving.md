# Archiving — move, don't delete

How to move things out of your active system without losing them.

---

## The three OS pattern

Your active system is one of three parallel containers, each named for what it does:

- **PERSONAL-OS** — the working system. Everything live, in flow, currently in use. Your starter is one of these.
- **ARCHIVE-OS** — preserved-but-out-of-the-way. Things you don't want cluttering your daily working set, but don't want to delete either.
- **PUBLIC-OS** — what you share outward. Cleaned-up, universalized, ready for others. Public repos, distribution artifacts.

Each is a peer folder at the same level on your machine. They're siblings, not nested. None is "more important" than the others. Each is named for exactly what it is.

This is the convention, not a requirement. You can run with one container forever. But as your system grows, the friction of "I don't want this in my way but I'm not ready to delete it" is the signal that ARCHIVE-OS wants to exist. Same with "this is ready to share" → PUBLIC-OS.

---

## Why three (not one)

A single working system accumulates everything. Old projects, finished work, drafts you've outgrown, notes from a phase that's over. They don't go away. They pile up, slow down search, dilute attention.

**Deleting them feels wrong.** Future you might want them. The thinking is real, just not currently load-bearing. Throwing it out trades short-term clarity for long-term loss.

**Moving them is right.** Same files, different container. Out of your daily working set, still alive, still searchable when you need them. The move preserves texture; deletion erases it.

The three-container pattern is move-don't-delete applied at the system level. Same principle as "Move, don't recreate" inside a single repo (`Core/foundations/file-philosophy.md`), one layer up.

---

## When to move things out

Signals that something wants to live in ARCHIVE-OS instead of your working system:

- **Completed projects** that aren't likely to be referenced for months
- **Phase-of-life material** (old career, old client, old relationship), still meaningful but not active
- **Earlier system iterations** — drafts of structures you've replaced. Don't delete; archive. The "why" of how you got here lives in old shapes.
- **Reference material that's stale** — articles you read once that don't pull anymore, but might in a different context later
- **Long-completed task docs** that are themselves rich (case-study-grade) but are crowding the active list

**One thing starts in ARCHIVE-OS rather than moving there: other people's repos.** When `/add` clones a GitHub repo, it goes to `ARCHIVE-OS/Library/repos/`, not into your working system. A repo often carries its author's `CLAUDE.md` files and `.claude/skills/`, and inside your system Claude Code would load those as *your* instructions and skills whenever the AI read a file in them. Outside it, they're just files you read on purpose.

Signal that something wants to live in PUBLIC-OS instead of staying personal:

- **You've used it enough that it's load-bearing for you** — that's the prerequisite for sharing (we share what we do, not what we think)
- **It universalizes cleanly** — strip the personal, the structure still stands
- **You want others to be able to clone it as a starting point**

---

## The move

When archiving, move whole folders or whole task docs. Keep their structure. The destination should look as much like the origin as possible, the same texture preserved in a different home.

```
~/your-system/Projects/old-project/   →   ~/ARCHIVE-OS/Projects/old-project/
```

**Don't recompose.** Don't extract "the important parts" and toss the rest. The container is the texture's home. A summary version isn't the same thing, it's a different (lesser) artifact. The full move is the safety net you're trying to build.

**Update references.** When you move something, anything pointing at it from your working system breaks. A quick grep + fix-in-flight at archive-time keeps the friction low. (See "Always Be Compounding" in AGENTS.md; friction in passing has its lowest cost while context is hot.)

---

## What ARCHIVE-OS looks like

It mirrors your working system's structure. If your system has `Projects/`, `Library/`, `Tasks/`, then ARCHIVE-OS has the same shape. You navigate it the same way. Familiarity matters; you'll go looking for things later, and "where would past-me have put this?" is the question that needs to answer itself.

Some prefer a flatter structure in archive (`_lab/` for misc, dated folders for cohorts). Either works. The point is: it's organized enough that finding something is realistic, not buried in a pile.

---

## What PUBLIC-OS looks like

Each top-level folder is a separate public repo. Each repo has its own README, license, and structure shaped for its purpose. You DON'T mirror your private structure here. You universalize and re-shape for whoever's receiving it.

Anything that ships outward goes through a universalization step (use `/universal`). Strip the personal, verify the structure stands alone for someone who's never seen your system, package for distribution. Whether the destination is a public git repo or a zip you email someone, the work is the same.

---

## The bigger pattern

These three containers are infrastructure for the elder lens applied to your whole system. Past you made things. Future you will want some of them. Most won't be load-bearing daily, but losing them entirely is the wrong trade.

Containers are how you keep everything without drowning in everything.
