# Session 5 — Beyond the Fence

### Packages, environments, and working together

> **Before you start:** do Part 2 of `SETUP.md`. You need Miniconda and git installed.
>
> **A note on time:** this is two hours of packages and two hours of git. Do it as two
> meetings if you can — Part A and Part B are completely independent, and git deserves
> a fresh brain.

In Sessions 1–4 you wrote Python on your own, for yourself, using only what Python
comes with. Today you learn the two things that turn that into *working like a
programmer*: using code other people wrote, and writing code with someone else.

---
---

# PART A · Packages and environments

## A1. Break it first

Open `growth_chart.py` and run it. Don't read it yet — just run it.

```
ModuleNotFoundError: No module named 'matplotlib'
```

Good. That's today's problem.

Python comes with a lot of tools built in — that's why `import random` just worked in
Session 4. But it doesn't come with *everything*. `matplotlib` is a drawing library
that thousands of scientists use to make graphs, and it isn't part of Python. Somebody
else wrote it, and you have to go and get it.

**Talk about it for a minute:**

- Why *shouldn't* Python come with everything ever written?
- Where do you think the code actually comes from when you "install" something?
- How would you know whether to trust it?

## A2. What a package is

A **package** is a folder of Python files that somebody else wrote and published so
that anyone can `import` it.

There are hundreds of thousands of them. A few you'll meet if you keep going:

| package | what it does |
|---|---|
| `matplotlib` | draws graphs and charts |
| `numpy` | fast maths on big piles of numbers |
| `pandas` | spreadsheets, but in code |
| `requests` | fetches things from the internet |
| `pygame` | games |
| `biopython` | DNA and protein sequences |

The last one is not a joke. Actual cancer research runs on packages like these.

**Two tools install them:** `pip` (the standard one) and `conda` (which also manages
environments, which is the next bit). Today we use conda.

## A3. The problem with just installing things

Here's the trap. Imagine you install `matplotlib` version 3.9 for PetPal. Next year
you join a science club whose project needs `matplotlib` version 2.2, because their
code was written a long time ago and uses an old feature.

You install 2.2. Now **PetPal is broken**, because it wanted 3.9.

You install 3.9 again. Now **the science club project is broken**.

One computer, one pile of packages, two projects that want different things. This is a
genuinely annoying problem and it has broken more people's afternoons than almost
anything else in programming.

## A4. Environments: one box per project

An **environment** is a separate box of packages with its own Python inside it.

PetPal gets a box. The science club gets a different box. Each box has whatever
versions that project wants, and they never touch each other. Switching projects means
switching boxes.

Make yours:

```bash
conda create -n petpal python=3.12
```

`-n petpal` names the box. It'll list what it's about to install; type `y`.

Now step into it:

```bash
conda activate petpal
```

**Look at your prompt.** It changed from `(base)` to `(petpal)`. That little word is
the most useful thing on your screen today: it's telling you which box you're standing
in. Every package you install now goes in *this* box only.

```bash
conda install matplotlib
```

Say `y`. Watch the list — you asked for one package and it's installing a dozen.
That's because matplotlib depends on other packages, which depend on others. Conda
works all of that out for you. That is genuinely the hard part of the job it does.

## A5. Now run it again

```bash
cd ~/Desktop/PetPal          # Windows: cd %USERPROFILE%\Desktop\PetPal
python growth_chart.py
```

A window opens with your pet's growth curve — the exact rule you wrote in Session 3,
drawn as a line. It also saves `growth_chart.png` next to your code.

*Now* read the file. There's nothing in it you don't already know: a loop, an `if`, two
lists. The only new part is the last eight lines, where matplotlib turns those lists
into a picture.

## A6. Useful conda commands

| command | what it does |
|---|---|
| `conda env list` | show every box you have (the `*` is the active one) |
| `conda activate petpal` | step into a box |
| `conda deactivate` | step back out to `(base)` |
| `conda list` | show every package in the current box |
| `conda install <name>` | put a package in the current box |
| `conda remove <name>` | take one out |
| `conda env remove -n petpal` | throw a whole box away |

That last one is the quiet superpower: if you wreck an environment, you delete it and
make a new one in thirty seconds. Nothing is precious. Your *code* is precious;
environments are disposable.

## A7. Your turn — Part A challenges

1. **(easy)** Run `conda env list`. How many environments do you have? Which one has
   the `*` next to it?
2. **(easy)** Run `conda deactivate`, then run `growth_chart.py` again. Predict what
   happens *before* you press enter. Then `conda activate petpal` to fix it.
3. **(medium)** Change the growth rule in `growth_chart.py` — make a pet that never
   stops growing. Re-run and look at the shape of the line.
4. **(medium)** Plot **two** pets on the same chart, one fast-growing and one slow.
   Call `plt.plot()` twice, give each a `label="..."`, and add `plt.legend()`.
5. **(medium)** Run `conda list` and count the packages. You asked for one. How many
   are there?
6. **(tricky)** Make a second environment called `experiment` with an older Python:
   `conda create -n experiment python=3.9`. Activate it, run `python --version`, then
   switch back to `petpal` and run it again. Two Pythons, one laptop, no arguing.
7. **(tricky)** Save your environment so someone else can rebuild it exactly:
   ```bash
   conda env export > environment.yml
   ```
   Open `environment.yml` and read it. This one file is how a scientist lets another
   lab re-run her analysis and get *the same answer*. It matters more than it looks.

---
---

# PART B · Git, and building something together

## B1. Break it first (again)

Ask yourselves honestly: how do you two share a file right now? Email? AirDrop? A
shared drive?

Now imagine you've both got a copy, you both change it on the same evening, and now
there are two different files both called `park.py`. Which one is right? What happened
to the bit that only exists in the other one?

Everyone solves this the same bad way:

```
park.py
park_v2.py
park_final.py
park_final_REAL.py
park_final_REAL_mia_edit.py
park_use_this_one.py
```

**Git is the tool that makes that folder never happen again.**

## B2. What git actually is

Three ideas, and that's genuinely most of it:

**A repository ("repo")** is a folder that git is watching.

**A commit** is a save point. Not a file — a snapshot of *everything* in the folder at
one moment, with your name, the time, and a short message saying what you changed. You
can go back to any commit, ever, forever.

**A remote** is a copy of the repo that lives somewhere you can both reach. You *push*
your commits up to it and *pull* other people's down.

The key thing, and it's the thing people find strange at first: **you each have your
own complete copy of the whole project and its entire history.** You work on your copy.
Git's job is to combine the copies sensibly.

## B3. Your first repo (each of you, on your own laptop)

Copy the `pet_park` folder out of `PetPal` to your Desktop first — this project is
going to become a repo of its own.

```bash
cd ~/Desktop/pet_park
git init -b main
git status
```

Read what `git status` says. It has noticed files, and it's calling them *untracked* —
git can see them but isn't watching them yet.

```bash
git add .
git status
```

`git add .` means "start watching everything here". Look at status again — the files
are green now, and git calls this the **staging area**: the pile of changes you're
about to save.

```bash
git commit -m "First commit: the park and our two trick files"
git log --oneline
```

There it is. One save point, with your name on it.

> **Why two steps?** `add` chooses *what* goes in the snapshot, `commit` takes it. It
> feels like extra work for about a week, and then one day you'll want to save half of
> your changes and not the other half, and it'll make perfect sense.

## B4. The time machine

Let's prove commits are real. Wreck something on purpose:

Open `park.py` and delete a big chunk of `main()`. Save it. Run it — it's broken.

```bash
git status              # git noticed
git diff                # exactly what you changed, line by line
git restore park.py     # put it back
```

Run it again. It's fine.

Sit with that for a second. You can now **try anything** — rewrite half the program,
delete something you're scared to delete — because getting back is one command. That's
not an accounting tool. That's permission to experiment.

## B5. Sharing it — pick one

### Option A: a shared folder (no accounts, works right now)

One of you makes the "remote" in a folder you can both reach — a shared drive, a
network folder, or a USB stick:

```bash
git init --bare -b main /path/to/shared/pet-park.git
```

A *bare* repo is one with no files you can edit — just the history. That's all a
remote is.

Then, from your project:

```bash
git remote add origin /path/to/shared/pet-park.git
git push -u origin main
```

And your partner gets her own copy:

```bash
cd ~/Desktop
git clone /path/to/shared/pet-park.git
cd pet-park
```

### Option B: GitHub (real, public, and it's a portfolio)

GitHub is a website that hosts remotes. It's where an enormous amount of the world's
software lives, and having your work there is genuinely something to show people.

**You must be 13 or older to have a GitHub account, and you should ask a parent or
guardian first.** If that's not happening today, use Option A — the commands you learn
are identical.

1. One of you makes an account and creates a **new repository** called `pet-park`.
   Don't tick "add a README" — you already have one.
2. GitHub shows you a URL. Then:
   ```bash
   git remote add origin https://github.com/YOURNAME/pet-park.git
   git push -u origin main
   ```
3. Add your partner: repo **Settings → Collaborators → Add people**.
4. She clones it:
   ```bash
   git clone https://github.com/YOURNAME/pet-park.git
   ```

Refresh the GitHub page. Your code is on the internet. Click through the commit history
— it's the same `git log` you ran, with nicer fonts.

## B6. Now build the show

**Claim your file.** Rename your trick file to your own name, using git so it keeps the
history:

```bash
git mv tricks_a.py tricks_aisha.py
```

Then change the `import` line at the top of `park.py` to match. Commit both, push.

**The rule that makes this work:**

> Your trick file is yours. Nobody else edits it, ever.
> `park.py` and `README.md` are shared: **pull before you edit, push as soon as you're
> done.**

Now go. Each of you writes a new trick in *your* file:

```python
def zoomies(pet):
    for i in range(3):
        pet.step()
        pet.jump()
```

Then the loop you'll repeat all session:

```bash
git add tricks_aisha.py
git commit -m "Add zoomies"
git pull                    # get her work
git push                    # send yours
python park.py              # watch both pets do both people's tricks
```

**Stop and notice what just happened.** You edited your file. She edited hers. Neither
of you sent the other anything. `git pull` merged both sets of changes, and now the
show contains work from two people. Nobody lost a line.

Do this three or four times each. Add tricks, call them from `park.py`, push, pull, run.
The routine is the lesson.

## B7. The conflict (on purpose)

Everything above worked because you edited *different files*. Now let's do the thing
that scares people.

Open `README.md`. Find the "Who does what" heading. **Both of you, at the same time,**
add a line right underneath it:

```
- Aisha: tricks_aisha.py
```
```
- Mia: tricks_mia.py
```

Commit. One of you pushes first — she's fine. The second one pushes and gets rejected,
so she pulls, and git says:

```
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

**This is not an error and nothing is broken.** Git is telling you the truth: two
people changed the same line, and it is not willing to guess which one wins. That's a
human decision.

Open `README.md`:

```
<<<<<<< HEAD
- Mia: tricks_mia.py
=======
- Aisha: tricks_aisha.py
>>>>>>> 70d5b56
```

- Above `=======` is **your** version.
- Below it is **theirs**.
- The `<<<<<<<`, `=======` and `>>>>>>>` lines are just markers.

Fix it the way a human would: keep both lines, delete the three marker lines. Then:

```bash
git add README.md
git commit -m "Merge: keep both names in the README"
git push
```

The other one runs `git pull` and now you both have the same README.

That's it. That's a merge conflict. Nine people in ten are frightened of these, and
you've now resolved one on your second day of using git.

## B8. Your turn — Part B challenges

1. **(easy)** `git log --oneline --graph`. Find the place where your two lines of work
   came back together.
2. **(easy)** `git log -p tricks_mia.py` — every change ever made to one file.
3. **(medium)** Add a `.gitignore` line for something you don't want saved. Why
   shouldn't `growth_chart.png` be in the repo?
4. **(medium)** Make a change, commit it, then use `git log` to find the commit *before*
   it and `git show <that id>` to look at the old version.
5. **(medium)** Write a commit message that's actually useful, and one that's useless.
   What's the difference? (Hint: imagine reading it in six months.)
6. **(tricky)** Cause a conflict in `park.py` on purpose and resolve it, keeping both
   people's changes. Harder than the README, because the result has to still *run*.
7. **(tricky)** `git branch trick-experiment`, then `git switch trick-experiment`. Make
   a wild change. Switch back to `main` — it's gone. Switch again — it's back. Branches
   are the reason real teams don't step on each other.

## B9. The vocabulary

| word | what it means |
|---|---|
| repository / repo | a folder git is watching |
| commit | a save point, with a message and your name |
| `git add` | choose what goes in the next save point |
| `git status` | what's changed, what's staged — **run this constantly** |
| `git diff` | show me exactly what I changed |
| `git log` | the history |
| remote / `origin` | the shared copy everyone pushes to |
| `git push` | send my commits to the remote |
| `git pull` | get everyone else's commits |
| `git clone` | make my own copy of a repo that already exists |
| merge | combining two people's work |
| conflict | git needs a human to decide which version wins |
| branch | a separate line of work you can switch between |

## B10. If you get stuck

- **Run `git status` first, always.** It tells you what state you're in and usually
  suggests the next command. It's the most useful command in git and it can't break
  anything.
- **"Everything is ruined"** — almost certainly not. Every commit you made is still
  there. Ask for help before deleting anything.
- **"It says I need to commit before I can pull"** — commit your work first, then pull.
  Git doesn't want to merge on top of half-finished edits.
- **It opened a weird text editor asking for a message** — you forgot `-m "..."`. If
  it's vim, press `Esc`, then type `:wq` and Enter.

---

## Where this goes

Everything in this session is the boring plumbing under real software, and it's the
part nobody teaches in a first course — which is exactly why knowing it makes you look
like you've been doing this for years.

Environments are why a scientist can hand her code to another lab and have it produce
the same numbers. Git is why five hundred people can work on the same program without
it dissolving. Every professional programmer uses both of these every single day.

You've now used them too, on a project with two pets in it.
