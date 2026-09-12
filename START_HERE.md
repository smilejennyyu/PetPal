# PetPal — start here

Welcome! In this folder is everything you need to bring an electronic pet to life
with Python.

---

> **Full setup instructions, for macOS, Linux and Windows, are in `SETUP.md`.**
> This page is the short version plus the command reference.
>
> **Haven't got the PetPal folder yet?** Start with `README.md` — it walks you
> through forking and cloning the project, which is class 1.
>
> **Do you need Anaconda or a virtual environment? No.** PetPal uses nothing but
> Python itself. You used two git commands to get this folder; you'll learn what
> git actually *is*, and meet conda, in Session 5 — once you've hit the problems
> they solve.

## 1. Install Python (once, about 5 minutes)

You need two things, and they're separate programs:

1. **Python** from **python.org/downloads**.
   On **Windows**, tick *"Add python.exe to PATH"* in the installer — this is the
   mistake everyone makes. On **Linux**, also run `sudo apt install python3-tk`.
2. **VS Code** from **code.visualstudio.com**, then install the **Python**
   extension by Microsoft from the Extensions sidebar.

Then turn on **File → Auto Save**. It saves you a confusing half-hour later.

VS Code is what real programmers use, and it has a terminal and a git panel built
in — which is exactly what Session 5 needs, so you never change tools.

---

## 2. Open the folder

**File → Open Folder…** and choose the whole `PetPal` folder — the folder, not one
file. Then `Cmd/Ctrl+Shift+P` → **Python: Select Interpreter** and pick the Python
you just installed.

Click `demo_show_off.py` in the sidebar, then the **▷ play button in the top right**.

A window should open with a puppy in it. If it does — you are ready. 🎉

If a program won't stop (hello, infinite loop), click the terminal at the bottom and
press `Ctrl+C`.

---

## 3. The files

| File | What it is |
|---|---|
| `README.md` | How to fork and clone the project. You did this in class 1. |
| `demo_show_off.py` | A finished demo. Run this first to see where you are going. |
| `session1_meet_your_pet.py` | Session 1 — variables and types |
| `session2_pet_decisions.py` | Session 2 — if / elif / else |
| `session3_loops.py` | Session 3 — for and while loops |
| `session4_functions_and_lists.py` | Session 4 — functions, lists, your own project |
| `my_pet.py` | Your own playground. Nothing here is homework. |
| `petpal.py` | The engine. **Don't edit this one** — it's the magic behind the curtain. |
| `check_setup.py` | Run this if you're not sure your computer is ready. |
| `SETUP.md` | Full install instructions for Mac, Linux and Windows. |
| `SESSION5.md` | Session 5: packages, environments and git. Later. |
| `growth_chart.py` | Session 5 — it crashes on purpose until you install matplotlib. |
| `pet_park/` | Session 5 — the two-person project you'll share with git. |

---

## 4. How the window works

```
┌───────────────┬─────────────────────┬──────────────┐
│  Your code    │     Your pet        │  Variables   │
│  (the yellow  │   (walking around   │  (name, type │
│   line is the │    doing what you   │   and value) │
│   line Python │    told it to)      ├──────────────┤
│   is running  │                     │  Console     │
│   right now)  │                     │  (print())   │
└───────────────┴─────────────────────┴──────────────┘
```

- **Replay** runs your program again from the beginning
- **Slower / Faster** change how fast the pet moves — use *Slower* when you
  want to watch exactly what each line does

---

## 5. Everything your pet can do

**Things your pet can BE** (these are variables):

```python
pet.name = "Mochi"        # str    text, always in quotes
pet.age = 2               # int    whole number
pet.size = 1.4            # float  number with a decimal point
pet.is_hungry = True      # bool   True or False
pet.color = "lavender"    # str
pet.mood = "sleepy"       # str    happy excited sleepy sad surprised
```

**Things your pet can DO** (these are actions):

```python
pet.say("hello")     pet.think("hmm...")   pet.wait(1)
pet.step()           pet.walk(3)           pet.back(2)
pet.turn()           pet.jump()            pet.spin()
pet.dance()          pet.wag()             pet.cheer()      pet.sit()
pet.eat()            pet.sleep(2)          pet.wake()
pet.birthday()       pet.grow(0.2)         pet.shrink(0.1)
```

**Helpers:**

```python
show("treats", 5)              # put any variable on the Variables panel
name = ask("What's my name?")  # ask the human a question (gives back a str)
print("hello")                 # write in the Console
help_me()                      # print the full list of commands
```

**Colours:** golden, cream, peach, pink, rose, lavender, purple, sky, blue,
mint, green, grey, silver, chocolate, brown, ginger, white, black, orange,
yellow, red — or any hex code like `"#FF99CC"`.

---

## 6. When something goes wrong

It will. That's normal — professional programmers break things all day.

Look at the **Console** panel on the right. PetPal tries to explain the problem
in plain English and tell you which line to look at.

Three things to check first:

1. **Quotes** — text needs `"quotes"`, numbers don't.
2. **Colons and indents** — after `if`, `for`, `while` and `def` you need a `:`
   and the lines underneath must be pushed in (4 spaces).
3. **Spelling** — `pet.Say` is not `pet.say`. Python is fussy about capitals.
