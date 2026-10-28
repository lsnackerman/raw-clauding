# The session loop

*`/pickup` → work → `/wrap` → repeat. The loop that makes every session start warm instead of cold.*

This is one of the **two loops** the system runs on (the other is the [explore-loop](explore-loop.md)). Together they cover session-bridging AND topic-deepening, which is what creates compounding.

---

## The shape

```
/pickup  (start of session — read the handoff, orient, get warm)
   ↓
work     (the actual thinking, building, deciding)
   ↓
/wrap    (end of session — capture both voices, surface threads, update state)
   ↓
next session opens with full warmth instead of a cold start
```

---

## What it does

Every session compounds because nothing is lost between them.

- **`/wrap`** captures what happened (both voices, verbatim), surfaces the threads worth carrying forward, and updates the state files (`ALIVE.md`, `PULLING.md`, `THREADS.md`).
- **`/pickup`** reads that handoff, orients you back in the workstream, and gets you to where the energy left off.

Together they bridge sessions so each one starts where the last ended.

**The unlock**: cold-start is the default cost of working with AI. Every conversation begins from zero, and you spend the first ten minutes re-explaining context. The loop eliminates it. Without the loop, every session re-explains; with it, every session extends.

---

## Between the bookends

The bookends do the compounding, but the loop has a middle. Between `/pickup` and `/wrap`:

- **Route as you go** — when something surfaces that belongs elsewhere, say *"route that to [wherever]"* and keep your thread. Don't let it drop; next-you finds it where it belongs.
- **`/floor`** when you've been heads-down a while — open the floor and surface what you'd otherwise lose.
- **`/gut`** when you're about to make a design choice that matters — pressure-test it through the lenses before you commit.

These aren't extra loops; they're moves *inside* the session loop.

---

## Why it has to be lived

A loop is muscle, not knowledge. Reading about `/pickup` doesn't give you the experience of finding yourself oriented at the start of a session that started cold. The loop has to be **run**, ideally with someone alongside the first time, watching it close, not "here's how `/pickup` works" (lecture) but "let's `/pickup` this right now" (practice). After a few cycles, the muscle is yours.

---

## When the loop doesn't fire

Failure modes, named so they're recognizable when they happen:

- **Skipping `/wrap`** — session ends without capture; next session has nothing to `/pickup` from. The loop never closes, nothing compounds.
- **Skipping `/pickup`** — session starts cold; all the texture in `PULLING.md`/`ALIVE.md` goes unused. Each session works in isolation.
- **New rules don't activate mid-session** — a rule you add loads at the *next* session start, not the one you're in. The AI itself often doesn't know this and burns twenty minutes debugging a non-problem. End the session, start a new one, and it's there. (A new *skill* is the exception: the symlink hook makes it callable in the session you wrote it. Hook and settings edits are normally picked up live.)

**But a session that *dies* before `/wrap` (a crash, an API error, a context-limit cutoff) isn't lost.** The raw session transcript survives on disk, and a later session can recover the full record from it, even from a *different* session. The capability is real but doesn't advertise itself; the how-to lives in [`edge-cases.md`](../skills/sync/edge-cases.md) (§ Hard kill, § Context limit hit, § Targeting a foreign session).

---

## You are what makes it run

The loop is the mechanism; *you* are the lever. `/wrap` doesn't fire automatically; you initiate it. The system can hold what you've captured, but it doesn't compound on its own. See [human-as-compound-element](../lenses/human-as-compound-element.md) (the lens). The system carries the weight, you are the lever; both layers required.

---

## Related

- `Core/skills/pickup/SKILL.md` + `Core/skills/wrap/SKILL.md` — the two skills that run this loop
- [explore-loop.md](explore-loop.md) — the other loop (topic-deepening)
- [human-as-compound-element.md](../lenses/human-as-compound-element.md) — why the loop needs you to run it
