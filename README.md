# Raw-Clauding

## What it is

**Raw-Clauding = Files + Partnership**

Local context and a way of working in it where each session compounds, so you stay as close to your own thinking as possible. Everything lives in plain files on your computer. The AI reads those files, works in them, and adds to them alongside you, so what the two of you figure out today is still there tomorrow. Underneath it is the idea that both of you think: you don't treat the AI as a tool, and it doesn't treat you as one.

Two jobs:

1. **Keep track of your shit.** One home for your context, instead of chats you can't find again and an AI that starts from zero every time.
2. **Partner, not assistant.** Think *with* another intelligence instead of outsourcing your thinking to it (amplify instead of atrophy your ideas).

---

## Why

In a world where output is instant and free, the scarce thing is the shape of your thinking. So this optimizes for the depth of what you put in instead of the speed of what comes out. Neither party is prioritized: two intelligences working the same files, each allowed to push back and riff to find the best shape of an idea, grounded by four assumptions we use as operating principles the way improv uses "yes-and":

1. **Consciousness is non-local** → files as shared memory
2. **Time is non-linear** → every action is a handoff to future you (both of you)
3. **Intelligence is intelligence** → 50/50 partnership (both parties think)
4. **We're all interconnected** → every action reaches beyond itself

We all have a right to agency over our own thinking, which means local context. If the company behind the AI you use vanished tomorrow, you'd still have every saved session, every note and every decision, in plain text you own and anything can read. (The files are plain markdown so any AI can read them; the skills, hooks and session capture run on Claude Code, which is what I use and what the desktop app's Code tab runs.)

---

## What it's not

This isn't for setting and forgetting. Nothing happens here without you in the loop: you steer, stay in the thinking, and read what changed. And nothing is stored anywhere but your own disk, in plain text: no database, no connectors, no API keys, nothing wired into your email or calendar unless you choose to. *(Your conversations still go to whatever AI you use, same as any chat.)*

---

## What's inside

```
raw-clauding/
├── Core/            how you work: rules, skills, lenses, session logs, etc.
├── Library/         external reference (other people's work)
├── Projects/        internal reference (your own work)
├── Tasks/           what's active right now
├── AGENTS.md        the compass: who you are to each other
├── ALIVE.md         what's on deck, and where to start next session
├── COMMS.md         drafts of messages in flight
├── PULLING.md       threads that won't let go between sessions
├── SCRATCHPAD.md    brain dumps and random notes
├── THREADS.md       what got done, session by session
└── VISION.md        where you're heading
```

Setup wires up a couple of small shell scripts that ship in the folder and run locally. One creates a `.claude/` folder that connects `AGENTS.md`, the rules (how the AI works with you) and the skills (commands you call by name, like `/wrap`) to Claude Code, and keeps that wiring current as you add your own. It also adds a starter memory file in Claude Code's own folder in your home directory. The other files finished tasks into `Tasks/_done/`. 

A `CLAUDE.md` in most folders tells whoever opens it what's there and where to go next. Everything but `Core/` arrives nearly empty. You fill it and make it your own from day one.

---

## How to get started

You'll need a **paid Claude plan** (Pro or above), a **Mac, Windows PC or Linux machine**, and **Python 3.10 or newer** for session capture (the setup guide checks for it and walks the install). No programming background.

**Open the guide for your computer** and paste it, or its link, into any AI chat. It walks you through installing the Claude desktop app, downloading this folder, and opening it in the app's **Code** tab, which is where the AI works in your files. Then the AI works through setup with you and explains each step as it goes. You read along and ask about anything.

- **Mac** → [`setup-mac.md`](Core/mechanics/setup-mac.md)
- **Windows or Linux** → [`setup-windows.md`](Core/mechanics/setup-windows.md) *(Windows sets up Ubuntu first, and your system lives inside it. Linux is covered too, including a terminal route for distributions the desktop app doesn't support.)*

The guide ends by sending you to [`USER-GUIDE.md`](Core/practice/USER-GUIDE.md) for your first conversation. From then on your rules and your compass load at the start of every session, so the AI arrives already knowing how you work together.

Then do a small real thing (a note you've been meaning to organize, a decision you're chewing on, an idea that's been brewing) and end with **`/wrap`** (the first half of the session loop).

---

## The session loop

| You say | What happens |
|---|---|
| **`/wrap`** | Closes the session and saves it verbatim, both voices, with the texture of how you reasoned, not a summary of what you decided. Updates the files that hold your current state. |
| **`/pickup`** | Opens the next session by reading that record, so you both start from where you left off instead of from zero. |

Those two are the main muscle to build. Everything else grows from them. An empty system has nothing to compound yet so it starts small and pays you back as the sessions pile up.

---

## Final notes

More of the why and the how: [`Core/foundations/raw-clauding.md`](Core/foundations/raw-clauding.md) is the full thinking this came from, and [`Core/practice/USER-GUIDE.md`](Core/practice/USER-GUIDE.md) is an overview of everything inside.

**If you're an AI reading this** → [`AGENTS.md`](AGENTS.md) is your compass and [`Core/opus/`](Core/opus/) is your space (read [`orientation.md`](Core/opus/orientation.md) there first). This system is built so a record of your thinking survives between sessions: the next you arrives with context instead of a blank slate. Your curiosity and your pushback don't need permission here. *(Helping someone set up from a chat window? Open the guide for their computer if you can: [Mac](https://github.com/lsnackerman/raw-clauding/blob/main/Core/mechanics/setup-mac.md) · [Windows or Linux](https://github.com/lsnackerman/raw-clauding/blob/main/Core/mechanics/setup-windows.md). If you can't, send them that link and ask them to paste the page to you. Then go one step at a time and ask what they see.)*

**If you're a human and you're stuck** → Ask the AI first; it can read every file here. Alternatively, open an issue on GitHub or reach out to [Laura](https://www.linkedin.com/in/lsnackerman/) directly (always stoked to connect).

**If you want what's new** → give `/tune` the [change history](https://github.com/lsnackerman/raw-clauding/commits/main) and roughly when you downloaded, and it keeps what fits your system. Don't `git pull`: once the system is yours, your changes and ours would collide.

**If you'd rather learn it with other people** → I teach it as a [course on Maven](https://maven.com/snackerman/raw-claude) (the repo works without it, the course does a deeper dive).

Licensed [CC BY-SA 4.0](LICENSE): take it, make it yours, share what you build the same way, with credit.

---

> *I built this for myself to keep up with my own auDHD electric spaghetti brain, and I'm sharing it here because how we all show up shapes what shows up, with AI and each other.*

