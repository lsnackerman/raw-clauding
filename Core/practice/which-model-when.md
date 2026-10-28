# Which model when

*Your plan sets your model ceiling. Default to the best model your plan already includes; reach for a metered/premium tier only when a specific task justifies the out-of-pocket spend. And never assume the person across from you has the same access you do.*

The model you *can* reach for and the model you *should* default to are two different questions. Plan tier answers the first. Task-justifies-the-spend answers the second. This doc holds the evergreen frame. Specific model names and prices are a moving target, so verify current state at [anthropic.com/pricing](https://www.anthropic.com/pricing).

---

## The frame (evergreen)

1. **Plan tier is the ceiling.** What you can run for free is set by your subscription, not your preference. Two people raw-clauding the same task on different plans are not working with the same defaults. Design around that, especially when teaching or sharing.
2. **Default to the best *in-plan* model.** The everyday driver is whatever your plan covers without metering. That's the model you build your habits around, because it's the one you can run without watching a meter.
3. **Reach for a metered/premium tier on justification, not by default, and weigh *two* axes.** A premium model that bills usage credits is a *reach-for-it* tool: pull it in when a specific task's complexity, length, or stakes justify it, then drop back to your in-plan default. The justification has two dimensions: **cost** (worth the metered spend?) *and* **data retention** (is this content OK to route through a model with mandatory retention? See § Data retention). Defaulting to a metered tier for everyday work is how a subscription quietly becomes pay-as-you-go.
4. **Don't assume shared access.** When writing guidance, teaching, or briefing sub-agents, defaulting to "just use the top model" is a blind spot of whoever has the highest tier. State model recommendations relative to plan, or name the model explicitly with its tier.

---

## Plan → default (the durable shape)

The specific models shift, but the *shape* holds:

| Plan | Everyday default | Reach-for |
|---|---|---|
| **Entry tier** (lower-cost subscription) | the strong mid model your plan covers without tight caps | the top model, on metered credits, when a task justifies it |
| **Top subscription tier** | the best in-plan model, effectively unmetered | a frontier/premium model (metered) for the hardest long-running work |
| **API / usage-credits** | pick per task, since everything bills tokens | n/a (it's all pay-per-use) |

**The nuance worth knowing:** an entry-tier subscriber often *has* the top model but hits caps that push them onto the mid model for sustained work. So the question isn't "can I use the top model?" but "how often can I, before I'm capped back?" Budget your habits around the model you can run *without* watching a meter. The same nuance travels outward: when you brief a sub-agent, share your system, or compare notes with someone, their access may not match yours. Guidance and skill defaults that assume the top model break for whoever's capped onto the mid one.

---

## Data retention — the second axis (the part that outlasts the price)

Picking a model isn't only a cost call; it's a **data-handling** call. The most powerful models can carry retention terms that *override your normal privacy settings*, whether the model is free-in-plan or metered.

**The evergreen frame:** frontier models often ship with **mandatory safety monitoring**. Public access to a model that's otherwise considered too capable to release raw comes bundled with retention you can't opt out of. Expect this pattern to recur on future top-tier models.

**What that tends to mean in practice:**
- The model **retains prompts + outputs** for a retention window for safety classifiers, on first- *and* third-party surfaces.
- The retention is typically **safety-only** (not training) and deleted after the window, but it can **override existing zero-data-retention agreements**, with no opt-out: using the model *is* opting in.

**The baseline it's measured against (know this, or "mandatory retention" is meaningless).** *(Checked against Anthropic's privacy docs in July 2026. Vendor-controlled and will change; re-read the current docs before you rely on any number here.)* "Retention" and "training" are **two different things that one consumer setting controls**, which is why it's easy to miss:
- On **consumer plans** (Free / Pro / Max) one switch, **Model Improvement** (claude.ai → Settings → Privacy), moves both axes together: **OFF → not trained on + 30-day retention**; **ON → trained on + up to 5-year retention**. If you opted out of training, the 30-day retention came along as the paired effect, and that's the part most people don't know applies to them.
- It's **account-level, not per-tool.** The setting follows your account across chat, Claude Code, desktop, and mobile.
- **Incognito chats** are never trained on regardless of the setting; **safety-flagged content** is held for years on every tier, unavoidably.

**So what a mandatory-retention frontier model actually changes for a consumer-plan user: nothing on retention.** Anthropic's own docs say consumer plans are *"unaffected"* by that retention *"since we already retain inputs and outputs on these surfaces".* The mandatory window matches the 30-day floor you already have. The override bites **enterprise and zero-data-retention workspaces**, which normally retain *nothing*. ⚠️ **One honest gap:** no single Anthropic page states the exact combination *"consumer + Model Improvement OFF + frontier model = not trained on."* Every source points that way (the retention is safety-only, never for training without permission), but it's assembled from two documents. If training opt-out is the thing you care about, that's a one-line question to Anthropic support, not an assumption to lean on.

**The rule of thumb:** on a consumer plan, don't avoid the stronger model *for retention reasons*, because your 30 days is the same 30 days either way. If you work inside an **enterprise or zero-data-retention** workspace, the override is real: keep sensitive or personal system content on the standard model there. Either way, check the Model Improvement setting once, because it's the setting that actually decides what happens to your words.

---

## Related

- `Core/practice/multiple-agents.md` — model choice compounds when fanning out sub-agents (each agent's tier is a cost/quality decision)
- `Core/mechanics/claude-code.md` — the harness mechanics (the model picker in the Code tab, `/model` in a terminal)
