# Setup — Windows (and Linux)

Getting your system running in the **Claude desktop app**. No code editor, no programming background assumed. You will type a handful of commands, and every one is written out for you.

This is a system for thinking *with* the AI, and setup is the first thing you do together. Two parts:

- **Part 1 — before the folder is open** (steps 1–4). The AI can't see your folder until you open it in the app, so you drive this part. You don't have to drive it alone: **stuck, a screen doesn't match, or want a step explained? Paste a screenshot, or this guide, into the app's Chat tab** (or claude.ai in a browser, before the app is installed) **and work it out together.**
- **Part 2 — together in the folder** (steps 5–8). You paste one line; the AI runs the commands and explains what comes back, you read along and ask about anything as you go.

**You need a paid Claude plan** (Pro or above). The Code tab, where this system runs, asks free plans to upgrade.

**Two ways to run it on Windows. Pick one before step 2:** the system wires itself together with links and small **bash** scripts, and there are two ways to give Windows those.

|                   | **Native Windows**                                             | **WSL (Ubuntu)**                                                |
| ----------------- | -------------------------------------------------------------- | --------------------------------------------------------------- |
| Your folder lives | on your PC's drive, like any other folder (outside OneDrive)   | inside **Ubuntu**, a version of Linux that runs inside Windows  |
| You install       | Git for Windows, Python and `jq`: three installers, no restart | WSL and Ubuntu (10–20 minutes, maybe a restart), then two tools |
| In the app        | Environment **Local**                                          | Environment **WSL → Ubuntu**                                    |
| Good fit if       | you'd rather not add Linux, or WSL won't install               | you already use WSL, or want the most-travelled path            |

Both end in the same system. Each step below that differs has a **Native Windows** part and a **WSL** part: do the one for your path and skip the other. *(Native Windows is the newer of the two; if something in it doesn't match what you see, say so in the app's Chat tab or open an issue on the repo. How it differs underneath: [How native Windows wires itself](#how-native-windows-wires-itself).)*

**On Linux instead?** (Ubuntu 22.04+ or Debian 12+, where the desktop app is in beta.) Follow this guide with four differences: in step 1, install the app with `apt` following [Anthropic's Linux steps](https://code.claude.com/docs/en/desktop-linux); in step 2, skip WSL and just run the tools line in a terminal; in step 3, unzip straight into your home folder and rename it (no copying from `C:`); in step 4, choose **Local** and select the folder directly (step 4's "not Local" warning is about Windows; on Linux, Local is right). Other distributions → [Other Linux](#other-linux-fedora-arch-) at the bottom.

*On a Mac? → `setup-mac.md`*

---

## Part 1 — before the folder is open

### 1. Install the Claude app

- [ ] Download it from [claude.com/download](https://claude.com/download), run the installer, and sign in. *(There's a separate ARM64 download if your PC has an ARM processor.)*

### 2. Install the tools

#### Native Windows: Git for Windows, Python and jq

Claude Code runs the system's background scripts in **Git Bash**, which comes with Git for Windows. Python saves your sessions, and `jq` lets the scripts read what just changed.

- [ ] Open **PowerShell** (Windows key → type `PowerShell` → Enter; *not* as administrator) and run these **one at a time**, pressing Enter after each:
  ```
  winget install -e --id Git.Git
  ```
  ```
  winget install -e --id Python.Python.3.13
  ```
  ```
  winget install -e --id jqlang.jq
  ```
  Each prints `Successfully installed` when it's done. *(Already have one? winget says so; move on to the next. No `winget`? Download Git from [git-scm.com](https://git-scm.com/download/win) and Python from [python.org](https://www.python.org/downloads/windows/), and on Python's first screen tick **Add python.exe to PATH**.)*
- [ ] ⚠️ **Fully quit the Claude app and reopen it**: right-click its icon in the taskbar's corner tray → **Quit**, not just closing the window. A program only sees new installs when it starts, so an app that was already open still can't find them.
- [ ] Skip to step 3, **Native Windows**.

#### WSL: install WSL and Ubuntu, then two small tools

⏱️ **If you don't have WSL yet, budget 10–20 minutes, and it may ask for a restart.**

- [ ] Open **PowerShell as administrator** (right-click it → **Run as administrator**) and **check first**: `wsl -l -v`.
  - `Ubuntu` with **VERSION `2`**: already done, skip to the tools line below.
  - `Ubuntu` with **VERSION `1`**: run `wsl --set-version Ubuntu 2`. The app needs WSL 2.
  - An error, nothing listed, or a short help text (only `--install`, `--list`, `--status`, `--help`, the placeholder every Windows ships with): not installed, keep going.
- [ ] Run:
  ```
  wsl --install --web-download
  ```
  *(`--web-download` fetches Ubuntu straight from the web. Plain `wsl --install` goes through the Microsoft Store, which can stall or fail.)*
- [ ] **If it tells you to restart, do a full restart** (not sleep). Often it doesn't: if Ubuntu opens on its own and asks for a username, you're past it.
- [ ] **Ubuntu asks two questions the first time:**
  - **A username**: anything lowercase, no spaces. It doesn't have to match your Windows name.
  - **A password.** ⚠️ **Nothing appears as you type**, and the cursor doesn't move. That's how Linux does passwords; it hasn't frozen. Type it, Enter, type it again. **Write it down**; you'll need it again.
- [ ] **Install two small tools**, in that same Ubuntu window:
  ```
  sudo apt update && sudo apt install -y git jq
  ```
  It asks for the password you just set (nothing appears as you type), and it's done when your prompt comes back. **This one is yours to run:** `sudo` asks for your password, and the AI can't type it. *(Already have Git on Windows? Ubuntu still needs its own; they're separate programs.)*
- [ ] **Closed the Ubuntu window, or skipped the install because you already had it?** Windows key → type `Ubuntu` → Enter. It opens in your Linux home.

### 3. Get your system and make it yours

- [ ] **Download it**: on the repo's GitHub page, the green **Code** button → **Download ZIP**. *(GitHub names the unzipped folder `raw-clauding-main`.)* *(Know Git? `git clone` works too (into your Ubuntu home on WSL, into any folder that fits step 3's rule on native Windows) and skips the unzip-and-copy steps below; just don't `git pull` once the system is yours, because our changes and yours collide. "You're set up," below, says how to bring in what's new.)*
- [ ] **Unzip it: right-click → Extract All → Extract.** ⚠️ Don't double-click it. On Windows that opens a *preview* that looks exactly like a folder, but nothing has been extracted.
- [ ] **(Optional) Rename the folder** to something that feels like yours: `your-name-os`, `my-mind`, whatever. Naming is an ownership moment; you'll see this name every day. Letters, numbers and hyphens, no spaces. Also cool to leave as `raw-clauding` if you like. *(Then use `raw-clauding` wherever you see `your-name-os` below.)*

#### Native Windows: move it to where it will live

- [ ] **Pick its home.** Any folder on your PC's own drive works, as deep as you like: `C:\Users\YOURNAME\your-name-os`, or a work folder such as `C:\Users\YOURNAME\Workspace\your-name-os`. Your user folder is the easy default. ⚠️ **Just not inside OneDrive, Documents or Desktop** (on many PCs those three are synced by OneDrive), and not on a USB stick or network drive. The wiring uses Windows *junctions*, which need an ordinary local drive and get mangled by sync.
- [ ] Open the unzipped folder in File Explorer. Extract All usually makes a folder inside a folder (from GitHub: `raw-clauding-main\raw-clauding-main`); go in until you see `AGENTS.md`, `Core`, `Library`, `Projects` and `Tasks`. **That** is the folder to move.
- [ ] Go up one level, right-click it → **Cut**. Open the home you picked (for your user folder, type `%USERPROFILE%` in the address bar and press Enter), right-click empty space → **Paste**, and rename it to your chosen name.
- [ ] Skip to step 4, **Native Windows**.

#### WSL: copy it into Ubuntu

- [ ] **Copy it into your Ubuntu home**, not anywhere on `C:` (Windows' own drive, which Ubuntu calls `/mnt/c/`; the wiring breaks there). In the Ubuntu window, **one command at a time, pressing Enter after each**:
  ```
  cd ~
  ```
  ```
  ls /mnt/c/Users/
  ```
  Ignore anything that isn't a name (`Public`, `Default`, `All Users`, `desktop.ini` and the like); what's left is **your Windows username**. Use it, exactly as shown, wherever you see `YOURNAME` below. Then look where you unzipped it (**keep the quotes**):
  ```
  ls "/mnt/c/Users/YOURNAME/Downloads/"
  ```
  *(Nothing there? Try `"/mnt/c/Users/YOURNAME/OneDrive/Downloads/"`.)* Extract All usually makes a folder inside a folder (from GitHub: `raw-clauding-main/raw-clauding-main`), so look one level deeper, swapping in the folder name your `ls` just showed:
  ```
  ls "/mnt/c/Users/YOURNAME/Downloads/FOLDER-YOU-JUST-SAW/"
  ```
  Repeat until you see `AGENTS.md`, `Core`, `Library`, `Projects` and `Tasks`. Copy **that** folder home:
  ```
  cp -r "/mnt/c/Users/YOURNAME/Downloads/OUTER-FOLDER/INNER-FOLDER" ~/your-name-os
  ```
  **Swap in the real names:** the folder names your `ls` just showed in place of `OUTER-FOLDER/INNER-FOLDER`, and your name for `your-name-os`. Keep the quotes. Nothing prints when a copy works, so check:
  ```
  ls ~/your-name-os
  ```
  It should show the same list.
- [ ] ⚠️ **Once setup is done, delete the copy left on the Windows side.** Otherwise a Windows search finds that one, and you (or the AI) end up editing the wrong copy. *(Your real folder shows in File Explorer under **Linux** in the left sidebar.)*

### 4. Open it in the Code tab

#### Native Windows

- [ ] In the app, click the **Code** tab and set **Environment** to **Local**.
- [ ] **Select folder** and pick your system's folder from step 3 (if it's in your user folder, paste `%USERPROFILE%` into the file window's address bar to get there).
- [ ] Skip to the permission-mode line below.

#### WSL

- [ ] In the app, click the **Code** tab and set **Environment** to your **Ubuntu** distribution, under **WSL**. ⚠️ **Not Local**: Local runs on Windows itself, and your folder lives in Ubuntu. *(No WSL section in that menu? Quit the app fully and reopen it; if it's still missing, run `wsl -l -v` again.)*
- [ ] **Select folder**. The Windows file window needs the Windows way of writing your Ubuntu folder: click its address bar, paste this with your own Ubuntu username and folder name, and press Enter:
  ```
  \\wsl.localhost\Ubuntu\home\your-ubuntu-name\your-name-os
  ```
  *(Or browse: **Linux** → **Ubuntu** → **home** → your name → your folder.)* If you get "Folder must be inside the WSL distribution", you picked the copy on the Windows side.

#### Both paths

- [ ] The **permission mode** (next to the send button) starts on **Auto**: the AI works through each step without stopping to ask, safety checks run in the background, and you read what changed afterwards. *(If you want to approve every change before it happens, switch to **Manual**.)*
- [ ] Asked whether you **trust the files in this folder**? Yes, this one. Notice that it asked, and be exactly this suspicious of anyone else's context you bring into your environment.

**Then paste this into the Code tab:**

> **Read `Core/mechanics/setup-windows.md` and walk me through Part 2.**

---

## Part 2 — together in the folder

*For the AI: this is the first thing you two do together. Run each command yourself, show the lines this guide names, and explain in plain language what they mean. Check in at each ⚠️ before moving on. They may be new to all of this, file paths and permission prompts included, so ask as well as tell. First work out which path they took: a folder path starting `C:\` (or `/c/` in your shell) is **Native Windows**, `/home/...` is **WSL**, and the steps below say where the two differ. On WSL, anything that starts with `sudo` asks for their password, which you can't type; hand those to them to run in their Ubuntu window. On native Windows, installs are `winget` lines they run in PowerShell, and the app has to be fully quit and reopened afterwards before it sees them. Also on native Windows, `python3` is often Windows' Store placeholder rather than Python (python.org's installer makes `python` and `py`, not `python3`): wherever this system's docs say `python3`, use `python` there.*

### 5. Wire it up — DON'T SKIP THIS

**Nothing works until this runs once.** It connects your skills, your rules and your compass (`AGENTS.md`) to Claude Code. Skip it and nothing errors; the system just stays a folder of markdown.

- [ ] Run `bash Core/scripts/ensure-symlinks.sh --check` and read the last two lines:
  ```
  Setup check: N/N skills and N/N rules wired.
  You're set up. Start a new session so the AI picks everything up.
  ```
  Both pairs of numbers should match. `Nothing new to link — you were already set up` is the same good news.
- [ ] ⚠️ **If the last line says `The system is NOT fully set up`**, read upward: the line containing `COULD NOT`, `NOT A LINK`, `FAILED` or `NOTE:`, or starting with ⚠️, names the fix. The usual cause:
  - **WSL:** a folder on Windows' drive (anywhere under `/mnt/c/`), which can't make symlinks; copy it into your Ubuntu home (step 3) and run it again.
  - **Native Windows:** the folder is inside OneDrive or on a USB or network drive (move it to a local folder outside OneDrive, step 3), or `Python: MISSING` because the app was open while Python installed (fully quit and reopen it, step 2).

**Then look, because a green message and a working install are two different claims:**

- [ ] **WSL:** `ls -l .claude/rules`: every line after `total …` should read `something.md -> ../../Core/rules/something.md`.
- [ ] **Native Windows:** `ls -ld .claude/rules` should end in `-> …/Core/rules` (on Windows the whole rules folder is one link, called a *junction*), and `cat .claude/CLAUDE.md` should print just `@../AGENTS.md`, the line that loads your compass.
- [ ] `Core/auto-memory` should exist and point out into Claude Code's own folder for this project (on native Windows, a folder under `.claude/projects/` whose name starts `C--Users-`). That link runs the other way: the notes the AI keeps about you live in Claude Code's folder, and this puts them inside your system where you can both read and edit them. **It's the piece that keeps your context yours.** *(If the script printed "best guess for now — it self-corrects after your first session" under it, nothing to do; step 7 starts that session.)*

### 6. Check the tools

`/sync` saves your session log, and it runs on Python. **When Python is wrong, it fails silently**: everything looks fine all session, then capture breaks at `/wrap`.

**WSL:**

- [ ] Ubuntu comes with Python and step 2 added `jq`; check both: `python3 --version` (3.10 or higher) and `jq --version`.
- [ ] Anything missing? You run the install in your Ubuntu window, since it asks for your password: `sudo apt install -y python3 jq`. ⚠️ Use `apt` for these, not `pip3`: Ubuntu refuses `pip3 install` with a wall of red text about an `externally-managed-environment`. It looks like the install broke; it hasn't.

**Native Windows:**

- [ ] Check both: `python --version` (3.10 or higher) and `jq --version`.
- [ ] ⚠️ **A `python` that opens the Microsoft Store, or prints nothing at all, is Windows' placeholder, not Python.** Windows ships one, and it sits on the path until a real Python is installed. The system's scripts skip it and look for the real one, but if this check fails, Python isn't installed yet: run step 2's `winget` line for Python in PowerShell, then fully quit and reopen the app.
- [ ] `jq` missing? `winget install -e --id jqlang.jq` in PowerShell, then fully quit and reopen the app. Without it nothing breaks: tasks you mark done file away at the end of each turn instead of the moment you save.

### 7. Start a new session

**Your rules and your compass load when a session starts**, and this one started before step 5 wired them. ⚠️ **If you skip this, `/wrap` and the other slash commands answer "Unknown skill"**, and none of the rules are loaded for this initial session.

- [ ] **+ New session** in the sidebar (or `Ctrl+N`), same folder.
- [ ] Paste this into the Code tab:
  > **Read `Core/mechanics/setup-windows.md` and let's continue from step 8. Also, what is this system?**

### 8. Really make it yours

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

---

## How native Windows wires itself

On Mac, Linux and WSL the setup script makes **symlinks**. Windows' own symlinks need administrator rights or Developer Mode, and in Git Bash the usual `ln -s` doesn't make a link at all: it quietly makes a **copy** and reports success, so every "link" would be a copy that drifts away from the original. So on native Windows the script uses the link Windows lets anyone make, the **junction**, and works around the one thing junctions can't do, which is point at a single file:

| What                            | Mac, Linux, WSL                    | Native Windows                                                                                                        |
| ------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Each skill in `.claude/skills/` | a symlink                          | a junction                                                                                                            |
| `.claude/rules`                 | a folder of symlinks, one per rule | one junction to the whole `Core/rules/` folder; the settings file keeps `Core/rules/CLAUDE.md` from loading as a rule |
| `.claude/CLAUDE.md`             | a symlink to `AGENTS.md`           | a one-line file, `@../AGENTS.md`, which tells Claude Code to load your compass from `AGENTS.md`                       |
| `Core/auto-memory`              | a symlink                          | a junction                                                                                                            |

The setup check knows both shapes. It reports a **copy** sitting where a link belongs as `NOT A LINK`, the old failure this replaces, and the counts read through the junctions. The question that decides whether your system works is *"can the Claude Code I'm running follow it?"*, so it was answered by running Claude Code on Windows and checking that it loaded the skills, every rule, `AGENTS.md` and `MEMORY.md` through these links.

What native Windows needs that the other paths don't: **Git for Windows** (Claude Code runs the background scripts in its Git Bash; without it they never run), a folder on a **local NTFS drive outside OneDrive**, and **fully quitting the app after installing anything**, so it sees the new program.

If something doesn't match, **ask the AI what's failing, and/or open an issue on the repo, rather than grinding.** What you report makes it better for whoever's next.

## Other Linux (Fedora, Arch, …)

The desktop app is Debian/Ubuntu only for now, so use Claude Code in a terminal instead. It's the same engine.

- Install: `curl -fsSL https://claude.ai/install.sh | bash`, then add `export PATH="$HOME/.local/bin:$PATH"` to `~/.bashrc` (the installer prints this) and open a new terminal. `claude --version` should print a number.
- Install `git` and `jq` with your distribution's package manager (and `python3` if `python3 --version` prints nothing). Where Part 2 says `apt`, use yours.
- Unzip the system into your home folder, then `cd ~/your-name-os`, run `claude`, and paste the Part 2 line. In Part 2, "start a new session" means `/exit` then `claude` again, and the diffs appear right in the terminal.
- Once you're in: `/exit` gets you back to your plain terminal, and `claude` gets you back in.
