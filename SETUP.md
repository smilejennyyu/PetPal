# PetPal — Setup

Everything you need to get your computer ready.

**Read Part 1 before Session 1.** It takes about fifteen minutes and you only do it once.

**Ignore Part 2 until Session 5.** Seriously — it's there for later.

---

## Do I need Anaconda? Do I need a virtual environment?

**No.** Not for Sessions 1–4.

PetPal is written with nothing but Python itself. No `pip install`, no `conda`, no
virtual environment, no internet connection once you've got Python. If you have
Python, you can run your pet.

That's not a shortcut — it's on purpose. Environments and package managers exist to
solve a problem you haven't had yet. In Session 5 you'll *cause* that problem
deliberately, and then the tool will make sense. Installing it now would just be
five confusing commands you'd have to take on faith.

---
---

# PART 1 · Sessions 1–4

You need two things: **Python** (the language) and **VS Code** (the editor you type
it in). They're separate programs, and you install Python first.

> **Why VS Code?** It's what actual programmers use — at companies, in labs, in this
> building. It has a built-in terminal and a built-in git panel, which is exactly what
> you'll need in Session 5, so you never have to change tools halfway through. It
> takes ten more minutes to set up than a beginner editor. It's worth it.

## Step 1 — Install Python

### macOS

Your Mac already has a `python3`, but it's old and Apple keeps it for its own use.
Get your own:

1. Go to **python.org/downloads** — it will offer you the macOS version.
2. Open the `.pkg` and click through the installer.
3. When it finishes, a Finder window may open. You can close it.

<details>
<summary>Prefer Homebrew?</summary>

`brew install python python-tk` — **you need the `python-tk` part**, or PetPal
can't draw its window.
</details>

### Windows

1. Go to **python.org/downloads** and download Python for Windows.
2. Run the installer — and **before you click Install, tick the box at the bottom
   that says "Add python.exe to PATH".**

   This is the single most common setup mistake in all of Python. If you miss it,
   the `python` command won't work and the easiest fix is to run the installer
   again. Tick the box.
3. Leave everything else at its default. Click **Install Now**.

### Linux

```bash
sudo apt install python3 python3-tk python3-pip
```

The `python3-tk` part matters — that's the bit that draws windows.

### Check it worked

Open a terminal — **Terminal** on macOS/Linux, **Command Prompt** on Windows — and type:

```bash
python3 --version      # macOS / Linux
python --version       # Windows
```

You want `Python 3.10` or higher. Anything from 3.8 up will run PetPal.

## Step 2 — Install VS Code

1. Go to **code.visualstudio.com** and download it for your system.
2. Install and open it.
   - **macOS:** drag it into your Applications folder.
   - **Windows:** run the installer; tick *"Add to PATH"* if it offers.
3. Click the **Extensions** icon in the left sidebar — the four little squares — or
   press `Cmd+Shift+X` / `Ctrl+Shift+X`.
4. Search for **Python** and install the one published by **Microsoft**. (It will
   quietly install a second one called Pylance. That's expected and good.)

## Step 3 — Turn on Auto Save (do this now, thank me later)

**File → Auto Save** — click it so it's ticked.

Without this, VS Code doesn't save your file until you press `Cmd+S` / `Ctrl+S`, and
you *will* spend ten minutes wondering why your change didn't do anything. This one
menu item prevents that for the whole course.

## Step 4 — Put the PetPal folder somewhere sensible

Unzip `PetPal.zip` and move the `PetPal` folder to somewhere you'll find it again:

- **macOS/Linux:** `~/Desktop/PetPal`
- **Windows:** `C:\Users\YourName\Desktop\PetPal`

**Two rules about this folder:**

1. **Keep every file together.** `petpal.py` must sit next to the file you're running.
   If you move `session1_meet_your_pet.py` somewhere else on its own, it will stop
   working with the message `No module named 'petpal'`.
2. **Don't put it inside iCloud Drive, OneDrive or Google Drive** if you can avoid it.
   They sometimes move files out from under you while a program is running.

## Step 5 — Open the folder (the *folder*, not a file)

In VS Code: **File → Open Folder…** and choose the whole `PetPal` folder.

This matters. If you open a single file on its own, VS Code doesn't know where it
lives, and half its cleverness switches off. Open the folder once and everything in
the course is in the sidebar on the left.

If it asks "Do you trust the authors of the files in this folder?" — yes, you do.

## Step 6 — Tell VS Code which Python to use

Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux). This opens the
**Command Palette**, which is how you do everything in VS Code without hunting
through menus. Type:

```
Python: Select Interpreter
```

Press Enter, and pick the Python you installed in Step 1 (it'll say something like
*Python 3.13.1 64-bit*). Avoid any that say "deprecated".

Look at the **bottom-right corner** of the window — it now shows which Python you're
using. Glance at it whenever something strange happens.

## Step 7 — Run your first program

1. In the sidebar, click **`demo_show_off.py`**.
2. Click the **▷ play button in the top-right corner** of the editor.
3. A terminal panel opens at the bottom, and a window appears with a puppy in it.

That's it. You're set up.

<details>
<summary>Other ways to run a file</summary>

- **Keyboard:** `Ctrl+F5` (Run Without Debugging) on all systems.
- **From the terminal**, which you'll use a lot in Session 5. Open VS Code's built-in
  terminal with **View → Terminal** or `` Ctrl+` `` (the key above Tab), then:

  ```bash
  python3 demo_show_off.py     # macOS / Linux
  python demo_show_off.py      # Windows
  ```

  Note the difference: `python3` on Mac and Linux, `python` on Windows. That trips up
  everybody at least once.
</details>

## Step 8 — Check everything is right

Click `check_setup.py` in the sidebar and press ▷. You want `[ OK ]` on the first
three lines:

```
  [ OK ]  Python is new enough.
  [ OK ]  tkinter found (version 8.6) - PetPal can draw its window.
  [ OK ]  petpal.py is in this folder.
```

The `[ -- ]` lines further down are the Session 5 things. They're supposed to be
missing right now.

---

## Three VS Code things worth knowing on day one

**Stopping a program that won't stop.** You'll write an accidental infinite loop at
some point — everyone does. Click inside the terminal panel at the bottom and press
`Ctrl+C`. (Yes, `Ctrl`, even on a Mac.) Or click the **trash-can icon** on the
terminal to kill it outright.

**The Command Palette** — `Cmd/Ctrl+Shift+P` — is how you find anything. Forgot where
a setting lives? Type what you want.

**Red squiggles** under your code are VS Code noticing a problem before you even run
it. Hover over one to read what it thinks is wrong. It's usually right — but not
always, so don't panic if it's grumpy about something that works.

---

## If something goes wrong

| What you see | What's actually happening | Fix |
|---|---|---|
| `No module named 'petpal'` | You're running a file that isn't in the PetPal folder | Move the file back next to `petpal.py`; open the **folder** in VS Code, not a lone file |
| `No module named 'tkinter'` | Python was installed without the window part | **Linux:** `sudo apt install python3-tk`. **macOS Homebrew:** `brew install python-tk`. Otherwise reinstall from python.org |
| `'python' is not recognized...` (Windows) | The "Add python.exe to PATH" box wasn't ticked | Run the Python installer again and tick it |
| `command not found: python` (macOS) | On a Mac the command is `python3` | Type `python3` |
| The ▷ play button isn't there | The Python extension isn't installed, or the file isn't `.py` | Extensions sidebar → install **Python** by Microsoft |
| VS Code runs the wrong Python | Interpreter not selected | `Cmd/Ctrl+Shift+P` → *Python: Select Interpreter* |
| Nothing changes when you run | The file wasn't saved | Turn on **File → Auto Save**, or press `Cmd/Ctrl+S` |
| The window flashes and vanishes | `run(main)` is missing from the bottom of your file, or there's a typo above it | Check the last line is `run(main)`, then read the error in the terminal |
| The window is bigger than your screen | It's resizable | Drag a corner. It needs about 1150 × 620 |
| The program won't stop | Infinite loop | Click the terminal, press `Ctrl+C` |

---
---

# PART 2 · Session 5 only

**Do not do this before Session 5.** We'll do it together, and it'll make far more
sense after you've hit the problem it solves.

In Session 5 you need two new tools:

- **conda** — installs Python packages, and keeps each project's packages separate
- **git** — remembers every version of your code, and lets two people work on the
  same project without emailing files back and forth

## 5.1 — Install Miniconda

Miniconda is the small version of Anaconda. Same `conda` command, same everything you
need, but a few hundred megabytes instead of several gigabytes. If your computer
already has full Anaconda, skip this — every command below works exactly the same.

Download from **anaconda.com/download** (choose Miniconda), or, to skip the sign-up
form, straight from **repo.anaconda.com/miniconda**.

### macOS

1. Download the **macOS graphical installer** for Miniconda. Choose **Apple silicon**
   if your Mac is M1/M2/M3/M4, **Intel** if it's older. (Apple menu → About This Mac
   tells you which.)
2. Open the `.pkg` and click through: Continue → Agree → Install.
3. **Quit Terminal and VS Code completely, then reopen them.**
4. In a terminal you should now see `(base)` at the start of your prompt.

### Windows

1. Download the **Windows 64-bit graphical installer** for Miniconda.
2. Run it. Choose **Just Me** when it asks.
3. Leave **"Add Miniconda to my PATH"** *unticked*.
4. Open the Start menu, search for **Anaconda Prompt**, open it, and run this once:

   ```bat
   conda init powershell
   ```

   That's what lets VS Code's built-in terminal understand `conda`. Close VS Code
   and open it again afterwards.

### Linux

```bash
cd ~/Downloads
bash Miniconda3-latest-Linux-x86_64.sh
# read the licence, type yes, accept the default location, and say yes to conda init
```

Then close and reopen your terminal.

### Check it worked

In VS Code's terminal (`` Ctrl+` ``):

```bash
conda --version
```

You should get something like `conda 24.x.x`. Any version is fine. If the terminal
says it's never heard of conda, use **Anaconda Prompt** (Windows) or a fresh Terminal
window (macOS/Linux) instead, and we'll sort VS Code out in class.

## 5.2 — Make your PetPal environment

This is the actual lesson of Session 5, so we'll go through *why* in class. The
commands are the same on all three systems:

```bash
conda create -n petpal python=3.12
conda activate petpal
```

Your prompt changes from `(base)` to `(petpal)`. That prompt is the whole point —
it tells you which box of packages you're standing in.

Then install the thing we actually came for:

```bash
conda install matplotlib
```

## 5.3 — Point VS Code at your new environment

Two steps, and skipping either one is the cause of about 90% of "but I installed it!"
confusion:

1. `Cmd/Ctrl+Shift+P` → **Python: Select Interpreter** → choose the one labelled
   **`petpal`** (it'll say *conda*).
2. **Close the terminal panel and open a new one**, so it starts inside the
   environment. Check the prompt says `(petpal)`.

Now the ▷ play button and the terminal both use the environment you just built.

## 5.4 — Install git

### macOS

Type `git --version` in a terminal. If it prints a version, you already have it. If a
box pops up offering to install "command line developer tools", click **Install** and
wait.

### Windows

Download from **git-scm.com/download/win** and run the installer. Click through with
the default options — they're fine. (If you can't install software on this laptop,
`conda install git` inside your `petpal` environment works too.)

### Linux

```bash
sudo apt install git
```

### Tell git who you are (once, on each computer)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase false
```

The last two lines just pick sensible defaults so git doesn't ask you awkward
questions later. Your name and email get stamped on every change you make — that's
how a project knows who wrote what.

> **About GitHub:** you need to be **13 or older** to have a GitHub account, and you
> should ask a parent or guardian first. If that's not happening, no problem at all —
> Session 5 has a version that uses a shared folder instead, and you learn exactly
> the same git commands.

> **VS Code has a git panel** — the branching icon in the left sidebar, or
> `Cmd/Ctrl+Shift+G`. It's genuinely useful for *seeing* what changed. In Session 5
> we type the commands anyway, because the commands are the thing you're learning and
> they work on every computer you'll ever sit at. Keep the panel open and watch it
> react.

## 5.5 — Check everything again

```bash
conda activate petpal
cd ~/Desktop/PetPal          # Windows: cd $env:USERPROFILE\Desktop\PetPal
python check_setup.py
```

Now you want to see:

```
  [ OK ]  conda environment active: petpal
  [ OK ]  matplotlib 3.x.x is installed.
  [ OK ]  git version 2.x.x
```

---

## Appendix — surviving the terminal

VS Code has a terminal built in: **View → Terminal**, or `` Ctrl+` `` (the key above
Tab). It opens already pointing at your project folder, which saves a lot of `cd`.

Five commands get you everywhere:

| What you want | macOS / Linux | Windows (PowerShell) |
|---|---|---|
| Where am I? | `pwd` | `pwd` |
| What's in here? | `ls` | `ls` |
| Go into a folder | `cd PetPal` | `cd PetPal` |
| Go back up one | `cd ..` | `cd ..` |
| Go home | `cd ~` | `cd ~` |
| Run a Python file | `python3 park.py` | `python park.py` |

Three things that save time:

- **Press Tab** to finish a folder name instead of typing it out. Type `cd Pet` then
  Tab and the computer fills in `PetPal`.
- **Press the up arrow** to bring back the last command you typed.
- **Drag a folder onto the terminal window** to paste its full path.

If a path has a space in it, wrap it in quotes: `cd "My Stuff/PetPal"`.
