# PetPal — start here

Welcome! In this folder is everything you need to bring an electronic pet to life
with Python.

---

## 1. Install Python (once, about 5 minutes)

**The easiest way, and the one we recommend: Thonny.**

1. Go to **thonny.org**
2. Download the version for your computer (Mac or Windows)
3. Install it and open it

Thonny *is* a Python editor and it brings Python with it, so there is nothing
else to install. It was made for beginners: big buttons, no confusing settings.

<details>
<summary>Already have VS Code or another editor? That works too.</summary>

You need Python 3.8 or newer from **python.org**. On Windows, tick
*"Add Python to PATH"* during install. On Linux you may also need
`sudo apt install python3-tk`.
</details>

---

## 2. Open the folder

In Thonny: **File → Open…** and pick a file from this folder.

Start with `demo_show_off.py`. Press the big green **Run** button (or `F5`).

A window should open with a puppy in it. If it does — you are ready. 🎉

---

## 3. The files

| File | What it is |
|---|---|
| `demo_show_off.py` | A finished demo. Run this first to see where you are going. |
| `session1_meet_your_pet.py` | Session 1 — variables and types |
| `session2_pet_decisions.py` | Session 2 — if / elif / else |
| `session3_loops.py` | Session 3 — for and while loops |
| `session4_functions_and_lists.py` | Session 4 — functions, lists, your own project |
| `my_pet.py` | Your own playground. Nothing here is homework. |
| `petpal.py` | The engine. **Don't edit this one** — it's the magic behind the curtain. |
| `solutions_session*.py` | For the teacher (and for after you've had a real go). |

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
