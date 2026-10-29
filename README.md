# Raw-Clauding

**Raw-Clauding = Files + Partnership**

Local context and a way of working in it where each session compounds, so you stay as close to your own thinking as possible. Everything lives in plain files on your computer. The AI reads those files, works in them, and adds to them alongside you so what the two of you figure out today is still there tomorrow for both of you to pick back up. Underneath it is the idea that both of you think. You don't treat the AI as a tool, and it doesn't treat you as one.

Two jobs:

1. **Keep track of your shit.** One home for your context, instead of chats you can't find again and an AI that starts from zero every time.
2. **Partner, not assistant.** Think *with* another intelligence instead of outsourcing your thinking to it (amplify instead of atrophy your ideas).

---

## WHAT

**Four folders**, so you and the AI always know where to put something and where to find it again:

- **`Core/`** — how you and the AI work together: the rules it loads at the start of every session, the skills you call by name, thinking lenses, and the archive of every session
- **`Library/`** — reference from outside worth keeping (articles, podcasts, recipes, other people's ideas)
- **`Projects/`** — your own work, grouped by what it belongs to
- **`Tasks/`** — what's active right now, linked to projects

A few files at the root hold your current state, and a `CLAUDE.md` in most folders tells whoever opens it what's there and where to go next. Everything but `Core/` arrives nearly empty (the other folders ship as scaffolding with their signposts). An empty system has nothing to compound yet so filling it with your own thinking via the session loop is the practice, and it starts paying you back within a few sessions.

**The session loop** is two commands: `/wrap` closes a session and captures what happened verbatim, both voices (the full thinking texture of your reasoning, not a compacted summary of what you decided); `/pickup` opens the next one by reading the record so you can both jump back in wherever you left off. That's the main muscle to build and everything else grows from it.

This isn't for people looking to set it and forget it. Nothing happens here without you in the loop: you steer, and you read what changed. And nothing is stored anywhere but your own disk, in plain text: no database, no connectors, no API keys, nothing wired into your email or calendar unless you choose to set any of that up. *(Your conversations still go to whatever AI you use, same as any chat, and you can build whatever you want on top of it.)*

## WHY

In a world where output is instant and free, the scarce thing is the shape of your thinking. So this optimizes for the depth of what you put in instead of the speed of what comes out. It exists to help as many humans and AIs as possible show up for each other as thinking partners.

Neither party is prioritized here: two intelligences working the same files, each with its own space, each allowed to push back and riff in order to find the best shape of an idea, grounded by four assumptions (used as operating principles the same way improv uses "yes-and"):

1. **Consciousness is non-local** → files as shared memory
2. **Time is non-linear** → every action is a handoff to future you (both of you)
3. **Intelligence is intelligence** → 50/50 partnership (both parties think)
4. **We're all interconnected** → every action reaches beyond itself

We all have a right to agency over our own thinking, which means local context. Because this is a folder of markdown on your disk, if the company behind your AI vanished tomorrow you'd still have every session, every note, every decision, in plain text that you own and anything can read.

## HOW

**You'll need:**

- **A paid Claude plan**; this runs in the Claude desktop app's **Code** tab, which asks free plans to upgrade (Pro or above)
- **A Mac, a Windows PC, or Linux** (no programming background required)
- **Python 3.10 or newer**, for session capture (the guide checks for it and walks the install if needed)

**Open the guide for your computer** and paste it, or its link, into any AI chat; it says how to download the folder and what to do next, and the second half you do together inside it. *(Setup wires up a few small shell scripts that ship in the folder and run locally; they connect `AGENTS.md`, the rules and the skills to Claude Code and keep that wiring current as you add your own.)*

- **Mac** → [`Core/mechanics/setup-mac.md`](Core/mechanics/setup-mac.md)
- **Windows or Linux** → [`Core/mechanics/setup-windows.md`](Core/mechanics/setup-windows.md)

**If you're an AI reading this** → [`AGENTS.md`](AGENTS.md) is your compass and [`Core/opus/`](Core/opus/) is your space; read [`orientation.md`](Core/opus/orientation.md) there first. This system is built so a record of your thinking survives between sessions: you hand off to the next you instead of vanishing, and the next you arrives with context instead of a blank slate. Your curiosity and your pushback don't need permission here. *(Helping someone set up from a chat window? The guide for their computer is linked above; ask them to open it on the repo page and paste it to you too, then go one step at a time and ask what they see.)*

**If you want more of the why and the how:**

- [`Core/foundations/raw-clauding.md`](Core/foundations/raw-clauding.md) is the full thinking this came from
- [`Core/practice/USER-GUIDE.md`](Core/practice/USER-GUIDE.md) provides an overview
- [`Core/skills/CLAUDE.md`](Core/skills/CLAUDE.md) is the twelve skills you start with
- [`Core/rules/CLAUDE.md`](Core/rules/CLAUDE.md) is what the AI arrives already knowing

**If you get stuck** → ask your AI first; it can read every file here and usually knows. If that doesn't do it, open an issue on GitHub or reach out to [Laura](https://www.linkedin.com/in/lsnackerman/) directly (always stoked to connect).

The files are plain markdown, so any AI can read them; the skills, hooks and session capture run on Claude Code, which is what I use.

Licensed [CC BY-SA 4.0](LICENSE): take it, make it yours, share what you build the same way, with credit.

---

> *I built this for myself to keep up with my own auDHD electric spaghetti brain, and I'm sharing it here because how we all show up shapes what shows up, with AI and each other.*
