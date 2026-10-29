# Setup — Mac

Getting your system running in the **Claude desktop app**. No terminal, no code editor, no programming background assumed.

This is a system for thinking *with* the AI, and setup is the first thing you do together. Two parts:

- **Part 1 — before the folder is open** (steps 1–3). The AI can't see your folder until you open it in the app, so you drive this part. You don't have to drive it alone: **stuck, a screen doesn't match, or want a step explained? Paste a screenshot, or this guide, into the app's Chat tab** (or claude.ai in a browser, before the app is installed) **and work it out together.**
- **Part 2 — together in the folder** (steps 4–7). You paste one line; the AI runs the commands and explains what comes back, you read along and ask about anything as you go.

**You need a paid Claude plan** (Pro or above). The Code tab, where this system runs, asks free plans to upgrade.

*On Windows or Linux? → `setup-windows.md`*

---

## Part 1 — before the folder is open

### 1. Install the Claude app

- [ ] Download it from [claude.com/download](https://claude.com/download), open the `.dmg`, and **drag Claude into Applications.** Then open it *from Applications* and sign in.

### 2. Get your system (and make it yours)

- [ ] **Download it**: on the repo's GitHub page, the green **Code** button → **Download ZIP**. Unzip it. *(GitHub names the unzipped folder `raw-clauding-main`; the `-main` is fine to keep or drop.)* *(Know Git? `git clone` works too; just don't `git pull` once the system is yours, because our changes and yours collide. "You're set up," below, says how to bring in what's new.)*
- [ ] **(Optional) Rename the folder** to something that feels like yours: `your-name-os`, `my-mind`, whatever. Naming is an ownership moment; you'll see this name every day. Letters, numbers and hyphens, no spaces. Also cool to leave as `raw-clauding` if you like.
- [ ] **Move it into Documents** (or Desktop or anywhere in your home folder). Not Downloads.

### 3. Open your system in the Code tab

- [ ] In the app, click the **Code** tab, set **Environment** to **Local**, then **Select folder** → your folder.
- [ ] The **permission mode** (next to the send button) starts on **Auto**: the AI works through each step without stopping to ask, safety checks run in the background, and you read what changed afterwards. *(If you want to approve every change before it happens, switch to **Manual**.)*
- [ ] Asked whether you **trust the files in this folder**? Yes, this one. Notice that it asked, and be exactly this suspicious of anyone else's context you bring into your environment.
- [ ] Asked whether Claude can access your **Documents** (or **Desktop**) folder? **Allow.** Your system lives there.

⚠️ **It may offer to install Git, or Apple's "command line developer tools."** Same install, about 2.5 GB, and it may offer again later. **Skip it**: setup doesn't need it, and step 5 sets up Python separately. *(If you ever `/add` a repo to your library, say yes then.)* *(Already clicked Install? That's fine too. It takes 10–15 minutes and can look stuck near the end without being stuck.)*

**Then paste this into the Code tab:**

> **Read `Core/mechanics/setup-mac.md` and walk me through Part 2.**

---

## Part 2 — together in the folder

*For the AI: this is the first thing you two do together. Run each command yourself, show the lines this guide names, and explain in plain language what they mean. Check in at each ⚠️ before moving on. They may be new to all of this, file paths and permission prompts included, so ask as well as tell. Anything outside this folder (step 5's `~/.zshrc` line): show the exact line and wait for a yes before writing it.*

### 4. Wire it up — DON'T SKIP THIS

**Nothing works until this runs once.** It connects your skills, your rules and your compass (`AGENTS.md`) to Claude Code. Skip it and nothing errors; the system just stays a folder of markdown.

- [ ] Run `bash Core/scripts/ensure-symlinks.sh --check` and read the last two lines:
  ```
  Setup check: N/N skills and N/N rules wired.
  You're set up. Start a new session so the AI picks everything up.
  ```
  Both pairs of numbers should match. `Nothing new to link — you were already set up` is the same good news.
- [ ] ⚠️ **If the last line says `The system is NOT fully set up`**, read upward: the line containing `COULD NOT`, `NOT A LINK`, `FAILED` or `NOTE:`, or starting with ⚠️, names the fix.
- [ ] A **"command line developer tools"** dialog? Same offer as step 3: **Cancel.** Step 5 sets up Python.

**Then look, because a green message and a working install are two different claims:**

- [ ] `ls -l .claude/rules`: every line after `total …` should read `something.md -> ../../Core/rules/something.md`.
- [ ] `Core/auto-memory` should exist and point out into Claude Code's own folder for this project. That link runs the other way: the notes the AI keeps about you live in Claude Code's folder, and this puts them inside your system where you can both read and edit them. **It's the piece that keeps your context yours.** *(If the script printed "best guess for now — it self-corrects after your first session" under it, nothing to do; step 6 starts that session.)*

### 5. Check Python, install if needed

`/sync` saves your session log, and it runs on Python. **When Python is wrong, it fails silently**: everything looks fine all session, then capture breaks at `/wrap`.

- [ ] Run `python3 --version`. **3.10 or higher?** Skip ahead to step 6. *(If it pops the "command line developer tools" dialog instead, there's no usable Python yet: Cancel it and install.)*
- [ ] **Older than 3.10, or no Python?** Install the one this system runs on. It sits alongside anything already there.
  - Download it from [python.org/downloads](https://www.python.org/downloads/) and run the installer.
  - ⚠️ At the end it opens a folder with an **Install Certificates** file: **double-click it.** Without it, this Python can't make secure web connections, and that only shows up later as a confusing error.
  - Run `python3 --version` again. **Still the old one?** The app hasn't picked up the new Python yet. Quit it completely (**Claude** menu → **Quit Claude**, or `Cmd+Q`; the red dot leaves it running), reopen it, pick this session back up in the sidebar, and say *"continue from step 5."*
  - **Still the old one after a real quit?** The AI can add one line to `~/.zshrc`, the file your Mac's shell reads on startup, so it finds the new Python. It shows you the line and asks first; then quit and reopen once more. The line: `export PATH="/Library/Frameworks/Python.framework/Versions/Current/bin:$PATH"`

### 6. Start a new session

**Your rules and your compass load when a session starts**, and this one started before step 4 wired them. ⚠️ **If you skip this, `/wrap` and the other slash commands answer "Unknown skill"**, and none of the rules are loaded for this initial session.

- [ ] **+ New session** in the sidebar (or `Cmd+N`), same folder.
- [ ] Paste this into the Code tab:
  > **Read `Core/mechanics/setup-mac.md` and let's continue from step 7. Also, what is this system?**

### 7. Really make it yours

`Core/you/` is your space: who you are, so the AI can meet you instead of serving you. It ships with a placeholder name. Making it yours is the best first thing to do together: it's about you, it's completely reversible, and it shows the rhythm you'll use for everything else.

- [ ] Paste this into the Code tab:
  > **Let's rename `Core/you/` and `Core/rules/you.md` to my name, and update anything that points at them.**
- [ ] **(Optional) Clear the top of your folder.** `README.md` is the GitHub front page and `LICENSE` is the terms you got the system under; your system doesn't need either up front. If you'd rather not see them, paste:
  > **Move `README.md` into `Core/foundations/` as `readme-from-github.md`, move `LICENSE` beside it, fix the links inside, and add both to `Core/foundations/CLAUDE.md`.**

  If you ever share your version, the LICENSE goes with it. Leave `.gitignore` where it is (you may not even see it): it has to stay at the top to work, and it keeps your machine's wiring out of anything you ever put on GitHub.

---

## You're set up

**That's the rhythm for everything from here:** you say what you're after, the AI does it and shows its work, you read what changed, and either of you can question the other. If a change surprises you, ask *"why did you do that?"* or *"what does that mean?"* That exchange is the partnership calibrating.

Head to `Core/practice/USER-GUIDE.md` Phase 2 for your first real conversation. You won't need this guide again; what you might reach for later:

- **Something seems not to be running** (skills not wired, tasks not filing) → `Core/mechanics/hooks.md`. Each background script has a flag that reports on itself.
- **The AI doesn't seem to remember you** → `Core/mechanics/memory-setup.md`.
- **Day-to-day Claude Code** (permissions, diffs, ending sessions) → `Core/mechanics/claude-code.md`.
- **Something new in the repo you want** → give `/tune` the repo's change history (`github.com/lsnackerman/raw-clauding/commits/main`) and roughly when you downloaded. By then your system has its own shape, so you keep what fits instead of copying ours over yours.
