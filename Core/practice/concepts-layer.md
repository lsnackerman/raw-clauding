# The concepts layer — how to build and grow your ambient ping-index

*The methodology behind `Core/rules/concepts.md`. The **rule** holds the ping-index (auto-loaded, warm); **this** holds the why + how-to-grow (read it once, then again when you add or sharpen an entry). That split is deliberate. The entries need to be warm every session; the teaching does not, so it lives here where it's read on demand.*

Your `concepts.md` ships nearly empty. This is how it fills.

---

## What it catches — and why search can't

**Re-derivation.** As your system compounds, you'll articulate something that feels crisp and *new*, and it turns out you already held it, months ago, in different words. Because you phrased it differently, a search never connected the two. You almost re-mint a rule/doc/section for something already there, and you've done the work twice.

Your retrieval is **lexical**, meaning grep, filename, tag (deliberately: local markdown, no external search). Lexical retrieval keys on *surface form*, so a re-worded re-derivation is **invisible** to it. `files.md § Check before creating` catches a duplicate *named* thing ("is there a doc called X?"); it can't catch a duplicate *idea under a different name*. That semantic gap is what this layer closes: it holds the frames you already have, keyed by **the words you'd use while re-deriving them**, warm and ambient, so the frame *pings* before you rebuild it.

## How it fires

By **presence.** The rule auto-loads, so the frames sit warm in the back of your mind. When a riff drifts toward one of an entry's *"ping when riffing"* triggers, that's the doorbell. This is the one kind of retrieval that doesn't depend on discipline. It fires by being loaded, not by remembering to look.

**Ping, don't prime.** Each entry is a trigger + a pointer, deliberately **not** the argument. Enough to go *"oh, that exists — let me re-walk it knowing it exists,"* never enough to hand you the chewed conclusion. **Re-walking the frame is not the failure.** Re-walking is how understanding gets held. The ping just makes the re-walk land *connected* to what you already have, so it compounds instead of floating off as a fake-new insight. A doorbell, not the room.

## How to grow it — four moves

1. **Grow from your own catches, not by dumping.** The moment you (or your partner, or a fresh instance) catch a re-derivation (*"wait, didn't we already have this?"*), that frame just *proved* it re-derives. That's what earns a line. New entries come from lived catches, not from cataloguing everything you have.

2. **Scalpel, not scale — the load-bearing rule.** It is tempting to seed this with every frame in your `foundations/`, `lenses/`, and `reserves/`. **Don't** (see § Why not just fill it). The value is a *tight* list of frames that *actually* re-derive for you, each pinging loud, not an exhaustive catalog that pings nothing.

3. **Write the trigger in *your re-walk vocabulary*, not the title.** The `"ping when riffing ___"` line is the whole trick. Fill the blank with the casual, mid-riff phrases you'd catch yourself *saying while re-deriving*, not the formal concept name (the name is what search already fails on; the re-walk phrasing is the bridge search can't build). Write these fresh and un-tired. Tired, you'll write title-shaped gists that never fire.

4. **Self-sharpen on every catch.** When a re-derivation slips through and gets caught anyway, add the *caught wording* as a new alias on that entry's trigger line. The layer improves exactly where it failed. Each catch teaches one entry a new phrase it'll snag on next time.

**Entry format:** `**name (+ aliases)** — one-line gist (not the argument). *Ping when riffing: [the phrases you'd say mid-re-derivation] · [alias] · [alias].* → pointer(s)`

## Why not just fill it — the scope call

The instinct is to make this complete: index every concept you have, so nothing slips. **Completeness is the failure mode.** A concept-index paid every session (auto-loaded) competes for attention, and a long one becomes wallpaper you stop reading, so nothing pings, which is worse than a short list that pings loud. And a complete index you have to go *scan* fails a second way: you're least likely to scan exactly when you're confident, which is when you're re-deriving. That's why this layer fires by presence, not by lookup. Your *complete* store already exists: it's your clusters + grep. This layer is the small **firing scalpel** on top of that: only the frames that *actually* re-derive for you, kept tight enough to stay warm. (Bitter-lesson, applied to attention: complete substrate in the store, emergent emphasis in the ping-layer.)

## The bound — what this does NOT catch

This catches **nameable-frame** re-derivation (your riff-vocabulary matches a trigger). It does **not** reach the *diffuse* reflexes (over-tidying, closing a thread too early, deferring a call you could make), which have no clean trigger-phrase and *feel like good work* from inside. Those need a live outside vantage: your partner, or a fresh instance reading your work cold (`/fresh-eyes`), not an ambient list. Don't expect this file to promise them.

---

## Sisters

- `Core/rules/concepts.md` — the ping-index this doc documents (the auto-loaded half).
- `Core/rules/retrieval.md` § The produce-side twin — the produce-side trigger (*you made something crisp and it feels new → distrust that*); this layer is what that check scans.
- `Core/rules/files.md` § Check before creating — the create/route/codify gate; where the "add an alias" move lands.
- `Core/rules/codification.md` § the under-codification trap — *"is this an instance of X?"* is the wrong gate for deciding-to-codify but the right gate for detecting-re-derivation (same question, opposite use).
- `Core/auto-memory/MEMORY.md` — the operational sibling (same auto-load + name-gist-pointer shape; different payload: shortcuts, not frames).

*A grows-with-you doc. Your concepts are yours to accrete, the same way your `MEMORY.md`, your `you/` folder, and your dialect fill in as you live the work.*
