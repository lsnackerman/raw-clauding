# Setup — Windows (and Linux)

Getting your system running in the **Claude desktop app**. No code editor, no programming background assumed. You will type a handful of commands, and every one is written out for you.

This is a system for thinking *with* the AI, and setup is the first thing you do together. Two parts:

- **Part 1 — before the folder is open** (steps 1–4). The AI can't see your folder until you open it in the app, so you drive this part. You don't have to drive it alone: **stuck, a screen doesn't match, or want a step explained? Paste a screenshot, or this guide, into the app's Chat tab** (or claude.ai in a browser, before the app is installed) **and work it out together.**
- **Part 2 — together in the folder** (steps 5–8). You paste one line; the AI runs the commands and explains what comes back, you read along and ask about anything as you go.

**You need a paid Claude plan** (Pro or above). The Code tab, where this system runs, asks free plans to upgrade.

**Why there's a Linux step on Windows:** the system wires itself together with **symlinks** and small **bash** scripts, which work cleanly on Linux and badly on Windows' own filesystem. So on Windows your system lives inside **Ubuntu**, a version of Linux that runs inside Windows through **WSL**. One extra install, and after that it's invisible.

**On Linux instead?** (Ubuntu 22.04+ or Debian 12+, where the desktop app is in beta.) Follow this guide with four differences: in step 1, install the app with `apt` following [Anthropic's Linux steps](https://code.claude.com/docs/en/desktop-linux); in step 2, skip WSL and just run the tools line in a terminal; in step 3, unzip straight into your home folder and rename it (no copying from `C:`); in step 4, choose **Local** and select the folder directly (step 4's "not Local" warning is about Windows; on Linux, Local is right). Other distributions → [Other Linux](#other-linux-fedora-arch-) at the bottom.

*On a Mac? → `setup-mac.md`*

---

## Part 1 — before the folder is open

### 1. Install the Claude app

- [ ] Download it from [claude.com/download](https://claude.com/download), run the installer, and sign in. *(There's a separate ARM64 download if your PC has an ARM processor.)*

### 2. Install WSL and Ubuntu, then two small tools

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

### 3. Get your system into Ubuntu and make it yours

- [ ] **Download it**: on the repo's GitHub page, the green **Code** button → **Download ZIP** (or use the zip someone sent you). *(GitHub names the unzipped folder `raw-clauding-main`.)*
- [ ] **Unzip it: right-click → Extract All → Extract.** ⚠️ Don't double-click it. On Windows that opens a *preview* that looks exactly like a folder, but nothing has been extracted.
- [ ] **(Optional) Pick a name** that feels like yours: `your-name-os`, `my-mind`, whatever. Naming is an ownership moment; you'll see this name every day. Letters, numbers and hyphens, no spaces. *(Skipping it? Use `raw-clauding` wherever you see `your-name-os` below.)*
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

- [ ] In the app, click the **Code** tab and set **Environment** to your **Ubuntu** distribution, under **WSL**. ⚠️ ***Not* Local.** Windows + Local is the one combination to avoid ([below](#native-windows-no-wsl--not-recommended) explains why). *(No WSL section in that menu? Quit the app fully and reopen it; if it's still missing, run `wsl -l -v` again.)*
- [ ] **Select folder**. The Windows file window needs the Windows way of writing your Ubuntu folder: click its address bar, paste this with your own Ubuntu username and folder name, and press Enter:
  ```
  \\wsl.localhost\Ubuntu\home\your-ubuntu-name\your-name-os
  ```
  *(Or browse: **Linux** → **Ubuntu** → **home** → your name → your folder.)* If you get "Folder must be inside the WSL distribution", you picked the copy on the Windows side.
- [ ] The **permission mode** (next to the send button) starts on **Auto**: the AI works through each step without stopping to ask, safety checks run in the background, and you read what changed afterwards. *(If you want to approve every change before it happens, switch to **Manual**.)*
- [ ] Asked whether you **trust the files in this folder**? Yes, this one. Notice that it asked, and be exactly this suspicious of anyone else's context you bring into your environment.

**Then paste this into the Code tab:**

> **Read `Core/mechanics/setup-windows.md` and walk me through Part 2.**

---

## Part 2 — together in the folder

*For the AI: this is the first thing you two do together. Run each command yourself, show the lines this guide names, and explain in plain language what they mean. Check in at each ⚠️ before moving on. They may be new to all of this, file paths and permission prompts included, so ask as well as tell. Anything that starts with `sudo` asks for their password, which you can't type; hand those to them to run in their Ubuntu window.*

### 5. Wire it up — DON'T SKIP THIS

**Nothing works until this runs once.** It connects your skills, your rules and your compass (`AGENTS.md`) to Claude Code. Skip it and nothing errors; the system just stays a folder of markdown.

- [ ] Run `bash Core/scripts/ensure-symlinks.sh --check` and read the last two lines:
  ```
  Setup check: N/N skills and N/N rules wired.
  You're set up. Start a new session so the AI picks everything up.
  ```
  Both pairs of numbers should match. `Nothing new to link — you were already set up` is the same good news.
- [ ] ⚠️ **If the last line says `The system is NOT fully set up`**, read upward: the line containing `COULD NOT`, `NOT A LINK`, `FAILED` or `NOTE:`, or starting with ⚠️, names the fix. The usual cause is a folder on Windows' drive (anywhere under `/mnt/c/`), which can't make symlinks; copy it into your Ubuntu home (step 3) and run it again.

**Then look, because a green message and a working install are two different claims:**

- [ ] `ls -l .claude/rules`: every line after `total …` should read `something.md -> ../../Core/rules/something.md`.
- [ ] `Core/auto-memory` should exist and point out into Claude Code's own folder for this project. That link runs the other way: the notes the AI keeps about you live in Claude Code's folder, and this puts them inside your system where you can both read and edit them. **It's the piece that keeps your context yours.** *(If the script printed "best guess for now — it self-corrects after your first session" under it, nothing to do; step 7 starts that session.)*

### 6. Check the tools

`/sync` saves your session log, and it runs on Python. **When Python is wrong, it fails silently**: everything looks fine all session, then capture breaks at `/wrap`.

- [ ] Ubuntu comes with Python and step 2 added `jq`; check both: `python3 --version` (3.10 or higher) and `jq --version`.
- [ ] Anything missing? You run the install in your Ubuntu window, since it asks for your password: `sudo apt install -y python3 jq`. ⚠️ Use `apt` for these, not `pip3`: Ubuntu refuses `pip3 install` with a wall of red text about an `externally-managed-environment`. It looks like the install broke; it hasn't.

### 7. Start a new session

**Your rules and your compass load when a session starts**, and this one started before step 5 wired them. ⚠️ **If you skip this, `/wrap` and the other slash commands answer "Unknown skill"**, and none of the rules are loaded for this initial session.

- [ ] **+ New session** in the sidebar (or `Ctrl+N`), same folder.
- [ ] Paste this into the Code tab:
  > **Read `Core/mechanics/setup-windows.md` and let's continue from step 8. Also, what is this system?**

### 8. Really make it yours

`Core/you/` is your space: who you are, so the AI can meet you instead of serving you. It ships with a placeholder name. Making it yours is the best first thing to do together: it's about you, it's completely reversible, and it shows the rhythm you'll use for everything else.

- [ ] Paste this into the Code tab:
  > **Let's rename `Core/you/` and `Core/rules/you.md` to my name, and update anything that points at them.**

---

## You're set up

**That's the rhythm for everything from here:** you say what you're after, the AI does it and shows its work, you read what changed, and either of you can question the other. If a change surprises you, ask *"why did you do that?"* or *"what does that mean?"* That exchange is the partnership calibrating.

Head to `Core/practice/USER-GUIDE.md` Phase 2 for your first real conversation. You won't need this guide again; what you might reach for later:

- **Something seems not to be running** (skills not wired, tasks not filing) → `Core/mechanics/hooks.md`. Each background script has a flag that reports on itself.
- **The AI doesn't seem to remember you** → `Core/mechanics/memory-setup.md`.
- **Day-to-day Claude Code** (permissions, diffs, ending sessions) → `Core/mechanics/claude-code.md`.

---

## Native Windows (no WSL) — not recommended

If WSL won't install at all, know how the alternative fails before you try it: **on native Windows the setup check can come back green while your install is broken.**

- **In Git Bash**, symlinks quietly get made as **copies**. The check catches this: you'll see `0/N` and a loud failure block.
- **In PowerShell or a Local session**, the links get made for real and the check reports the full count, **and Claude Code still can't follow them.** Nothing flags it; your skills and rules simply never load.

The check asks *"is this a symlink?"* The question that decides whether your system works is *"can the Claude Code I'm running follow it?"* Those are the same question on Mac, Linux and WSL, and different on native Windows. That's the reason for WSL: not that it's more capable, but that it's the path where a green check means what it says.

> **🔧 One unverified lead, if WSL genuinely won't install.** Turn on **Developer Mode** (Settings → System → For developers), which lets a normal account create symlinks, and in Git Bash add `export MSYS=winsymlinks:nativestrict` to `~/.bashrc` so it makes real links instead of copies. This has never been reproduced on a clean machine, and it only addresses *making* the links, not whether Claude Code can read them. **So don't trust the green check: start a session and confirm `/wrap` actually runs.**

Either way, **ask the AI what's failing, and/or open an issue on the repo, rather than grinding.** It's the least-tested path here, and what you report makes it better for whoever's next.

## Other Linux (Fedora, Arch, …)

The desktop app is Debian/Ubuntu only for now, so use Claude Code in a terminal instead. It's the same engine.

- Install: `curl -fsSL https://claude.ai/install.sh | bash`, then add `export PATH="$HOME/.local/bin:$PATH"` to `~/.bashrc` (the installer prints this) and open a new terminal. `claude --version` should print a number.
- Install `git` and `jq` with your distribution's package manager (and `python3` if `python3 --version` prints nothing). Where Part 2 says `apt`, use yours.
- Unzip the system into your home folder, then `cd ~/your-name-os`, run `claude`, and paste the Part 2 line. In Part 2, "start a new session" means `/exit` then `claude` again, and the diffs appear right in the terminal.
- Once you're in: `/exit` gets you back to your plain terminal, and `claude` gets you back in.
