# PetPal 🐕

You are going to build an electronic pet, in Python, from nothing.

It will have a name and a colour and a mood. It will walk, dance, get hungry, have
birthdays, and do whatever else you teach it to do. By the end you'll have written
every line of it yourself.

This page is **class 1, first thirty minutes**: getting your own copy of the project.
After that, everything you need is in **[START_HERE.md](START_HERE.md)**.

---

## Why you're not just downloading a folder

Real programmers don't email code around. They keep it on a site called **GitHub**,
where every project has its own page — like this one you're reading right now.

You're going to take your own copy of this project. In GitHub's words:

```
   smilejennyyu/PetPal          ← this page. The teacher's copy.
            │
            │  FORK  (a button on this page)
            ▼
   YOUR-USERNAME/PetPal         ← your copy, on the internet, with your name on it
            │
            │  CLONE  (a command you type)
            ▼
   PetPal on your Desktop       ← your copy, on your laptop, where you actually work
```

**Fork** = "give me my own copy of this project on GitHub."
**Clone** = "put a copy of that on this laptop so I can open it."

You do the fork once. You do the clone once per laptop. That's it — and you'll
understand *why* all of this exists in Session 5, once you've felt the problem it
solves.

---

## Step 1 — Make a GitHub account

Go to **[github.com/signup](https://github.com/signup)**.

- Pick a username you won't be embarrassed by later. It goes on everything you make.
  Your real name is a good choice. `xXx_d4rkl0rd_xXx` is a bad one.
- Use an email you can actually open right now — you'll need to click a link in it.
- **Write your username and password down somewhere real.** You will need them again
  in Session 5, four weeks from now, and "I forgot" costs the whole class ten minutes.

> **You need to be 13 or older to have a GitHub account,** and you should ask a parent
> or guardian first. If that's not happening — genuinely no problem. Tell your teacher
> and you'll get the files another way. You will not miss anything: Session 5 has a
> version that uses a shared folder and teaches exactly the same commands.

---

## Step 2 — Fork this project

Make sure you're looking at **this page** (`smilejennyyu/PetPal`) and logged in.

Near the top right there's a row of buttons: **Watch**, **Fork**, **Star**.

1. Click **Fork**.
2. On the next screen, leave everything as it is. Click **Create fork**.

Wait a few seconds. The page will change — and the name at the top will now say:

```
YOUR-USERNAME / PetPal        forked from smilejennyyu/PetPal
```

**Check that it says your username.** If it still says `smilejennyyu`, you're back on
the teacher's copy — the fork didn't happen, or you navigated away. Try again.

This page, with your name on it, is *yours*. Keep the tab open — you need its address
in Step 4.

---

## Step 3 — Install the tools

Three programs, all free.

**Python** and **VS Code** — follow **[START_HERE.md § 1](START_HERE.md)**, then come
back here. About five minutes.

**git** — this is the program that does the cloning:

| Your computer | What to do |
|---|---|
| **macOS** | Type `git --version` in a terminal. If a box offers to install *"command line developer tools"*, click **Install** and wait. |
| **Windows** | Download from **[git-scm.com/download/win](https://git-scm.com/download/win)** and click through with the default options. |
| **Linux** | `sudo apt install git` |

Then tell git who you are — once per computer, and it stamps your name on everything
you write:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase false
```

Full instructions with more detail are in **[SETUP.md § 5.4](SETUP.md)** if you get
stuck.

---

## Step 4 — Clone your fork

Open a terminal. In VS Code that's **View → Terminal**, or `` Ctrl+` `` (the key above
Tab).

Type these two lines — and **put your own username in**, not `YOUR-USERNAME`:

```bash
cd ~/Desktop
git clone https://github.com/YOUR-USERNAME/PetPal.git
```

On **Windows PowerShell**, the first line is:

```powershell
cd $env:USERPROFILE\Desktop
```

You should see something like:

```
Cloning into 'PetPal'...
remote: Enumerating objects: 47, done.
Receiving objects: 100% (47/47), done.
```

There is now a **PetPal** folder on your Desktop. That folder is the project. 🎉

> **The single most common mistake in this class** is cloning `smilejennyyu/PetPal`
> instead of your own fork. Look at the address you typed. Is your username in it?
> If not, delete the folder and do it again — otherwise you won't be able to save
> your work to GitHub in Session 5.

---

## Step 5 — Open it and meet your pet

In VS Code: **File → Open Folder…** and choose the whole **PetPal** folder — the
folder, not one file.

Then open **[START_HERE.md](START_HERE.md)** and keep going from there. It has the
full command reference, everything your pet can do, and what to do when something
breaks.

Run `demo_show_off.py` first. A window should open with a puppy in it.

---

## When it doesn't work

Everyone hits at least one of these. None of them mean you've broken anything.

| What you see | What it means |
|---|---|
| `git: command not found` | git isn't installed yet, or the terminal was open before you installed it. Close the terminal, open a new one, try again. |
| `repository not found` | A typo in the address, or your fork doesn't exist. Go to your fork's page on GitHub and copy the address from the browser bar. |
| `destination path 'PetPal' already exists` | You already cloned it. It's on your Desktop. You're done — go to Step 5. |
| It asks for a username and password | Only happens if you're pushing, which isn't until Session 5. For now press `Ctrl+C` and check you typed `https://`, not `git@`. |
| The clone worked but there's no puppy | That's Python, not git. **[START_HERE.md § 6](START_HERE.md)** and `python check_setup.py`. |

Still stuck? Ask. Getting the tools installed is genuinely the least interesting part
of programming, and nobody gets points for suffering through it alone.
