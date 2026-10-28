# The explore loop

*Curiosity → `/explore` → reserve grows → resurface → reserve compounds → apply. The loop that makes you find more than you put in, every time you reach for a topic.*

This is one of the **two loops** the system runs on (the other is the [session-loop](session-loop.md)). Together they cover session-bridging AND topic-deepening, which is what creates compounding.

---

## The shape

```
You ask a question (or run discovery mode with no topic)
   ↓
/explore searches the system (in parallel, for a broad topic)
   ↓
Returns raw material — verbatim quotes, sources, texture
   ↓
Lands in Core/reserves/{topic}.md
   ↓
Reserve grows over time, each run adding what's NEW since last
   ↓
You use the reserve as raw ingredients for whatever you're cooking
```

Reserves are markdown files by topic (one file per topic, ever-growing). They're not summaries; they're rich extracts with pointers back to sources, so the trail is always there.

---

## How `/explore` works

For a broad topic, `/explore` runs sub-agents across your system in parallel, one per territory (sessions, library, rules, projects). Each searches its territory, returns verbatim quotes with file paths, and you assemble the results into a reserve file. A narrow topic you can hold in one head gets searched inline instead. What makes it an explore and not just a search is the same either way: it gathers verbatim texture and lands in a reserve.

**The orient-first step.** Before searching, the AI reads the most likely canonical doc for the topic. That gives the agents the vocabulary to look for. Searching blind returns junk; searching with vocabulary returns signal.

**Sub-agents are for surprise, not precision.** If you only send them to find what your brain can already articulate, you're wasting them. The whole point: they search territory you don't know to look in, and come back with passages you forgot you wrote and connections you didn't see.

**No synthesis at this stage.** `/explore` is the gathering pass. Don't ask it to summarize, conclude, or compress. The reserve is a *raw tank*. Synthesis happens when you USE the reserve later, a different thinking move in a different mode.

Two modes: **topic** (you give it a topic to chase) and **discovery** (no topic; agents fan out to surface what's connecting across the system unprompted). Discovery mode is where the real magic lives; it finds threads you couldn't have asked it to look for.

---

## What's inside a reserve

Each reserve is one markdown file per topic at `Core/reserves/{topic}.md`:

- **Sources** — every file the agents found relevant material in
- **Verbatim passages** — full quotes with file paths and line numbers, never summaries
- **Decisions made** — what was decided about this topic, where, when
- **Open questions** — things raised that didn't get resolved
- **Connective tissue** — patterns across passages, things that rhyme, contradictions

Reserves are append-friendly. Each subsequent `/explore` on the same topic adds to the file rather than replacing it.

---

## The tail-eating guard

The trap: on a second `/explore` for a topic, sub-agents find the existing reserve file and treat IT as a source, searching a derivative instead of the originals, searching what they already searched. The reserve cannibalizes itself.

The fix is built into `/explore`: subsequent runs read the reserve FIRST to get the existing Sources list, then exclude that reserve from the search territory. Agents go find new material, not redundant material.

If a reserve ever feels stale or echoey, that's the signal. The guard might have slipped. Read the reserve, find anything circular, prune, then run `/explore` again on a fresh tank.

---

## The compounding

Each subsequent run asks: *what's NEW since last time?* (new sessions captured, new library content, new thinking from intervening work, things your brain didn't connect to this topic before). The reserve gets richer; the skill gets sharper (every `/explore` updates itself via skill-check). Both compound.

**Treating `/explore` as one-shot is the failure mode**: running it once, taking the output, never returning. The reserve is a *living document*; the loop only compounds if you come back. (And don't confuse it with search: `/explore` is for surprise, the agent finding what you can't think of; explicit search is for known targets.)

---

## What you cook from reserves

Reserves aren't the destination; they're ingredients. This is the **apply** layer, where the loop pays off:

- **Writing** something? The reserve gives you the texture and the receipts.
- **Teaching** something? The reserve has the verbatim moments worth pointing at.
- **Deciding** something? The reserve shows the through-line of your prior thinking.
- **Sharing** something? The reserve is where the original draft pulls from.

Turn a reserve into a thesis doc, a chapter outline, an FAQ, an instructional guide. The reserve is the raw tank; what you make from it is the meal.

---

## When to run this loop

- **Before writing or sharing on a topic** — pull what you already have so the new thing builds on the old instead of duplicating it
- **Before a sprint** — gather what's known so you start warm
- **When you sense a topic has scattered** — `/explore` consolidates; the reserve becomes the canonical home
- **When curiosity has no specific target** — discovery mode, no topic, see what surfaces

---

## What this isn't

- **Not a search index** — sub-agents read text and judge relevance; curated extraction, not raw search
- **Not a knowledge base** — knowledge bases optimize for completeness; reserves optimize for *texture* (your words, your reframes, the back-and-forth)
- **Not a summary** — reserves preserve, they don't compress

---

## You are what makes it run

`/explore` returns surprises only if you bring genuine curiosity, and the reserve compounds only if you keep coming back. See [human-as-compound-element](../lenses/human-as-compound-element.md) (the lens). The system carries the weight, you are the lever.

---

## Related

- `Core/skills/explore/SKILL.md` — the skill mechanics
- `Core/reserves/` — where reserves live
- [session-loop.md](session-loop.md) — the other loop (session-bridging)
- [human-as-compound-element.md](../lenses/human-as-compound-element.md) — why the loop needs you to run it
