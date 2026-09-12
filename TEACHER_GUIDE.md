# PetPal — Teacher Guide

**Course:** *PetPal — bring a pet to life with Python*
**Learners:** 2 students, Grade 8, no programming experience
**Format:** 4 sessions × 2 hours, plus an optional Session 5 (see below)
**Goal:** They leave able to read and write real Python — and, more importantly,
believing they are the kind of person who can.

---

## The one-paragraph version

Each student builds an electronic pet. Everything they learn about Python has an
immediate, visible consequence: a string becomes the pet's name, an integer
becomes its age, a float becomes its size, a boolean decides whether it eats, an
`if` statement decides whether it keeps growing, a `for` loop makes it walk. The
PetPal window shows their code on the left with the running line highlighted, the
pet in the middle, and a live **Variables** panel on the right that labels every
variable with its type. Nothing is a metaphor — the type panel really is the
types, the highlighted line really is the interpreter's position.

---

## Before session 1 — a 15-minute setup checklist

- [ ] Send the students `SETUP.md` — it walks them through the install for macOS,
      Linux and Windows, and it explicitly tells them they do **not** need Anaconda
      or a virtual environment for Sessions 1–4.
- [ ] On both laptops: **Python** from python.org (on Windows, *tick "Add python.exe
      to PATH"*), then **VS Code** from code.visualstudio.com, then the **Python**
      extension by Microsoft. Turn on **File → Auto Save** — it prevents the
      single most common "but I changed it!" confusion.
- [ ] In VS Code, **File → Open Folder** on `PetPal` (the folder, not a file), then
      `Cmd/Ctrl+Shift+P` → *Python: Select Interpreter*.
- [ ] Run `check_setup.py` on each laptop. Three `[ OK ]` lines means you're ready.
- [ ] Copy the `PetPal` folder onto each laptop — Desktop is fine.
- [ ] Open `demo_show_off.py`, click the **▷** button top-right, confirm a puppy appears.
- [ ] If nothing appears, see *Troubleshooting* at the end of this guide.
- [ ] Print the handouts (`handouts/PetPal_Handouts.pdf`) — one set each, plus the
      cheat sheet, which should live on the table for all four sessions.
- [ ] Have sticky notes or index cards nearby (used in the session 1 warm-up).

**Room setup.** Two laptops, side by side, both facing you. You want to be able
to glance at each screen without hovering over a shoulder.

---

## How to teach this (the short version)

**1. They type. Always.** Never take the keyboard. If you must show something,
say it out loud while they type it. Muscle memory matters more than you'd think,
and "I made it do that" is the whole point.

**2. Predict before you run.** The single highest-value habit in this course.
Before every Run: *"What do you think will happen?"* Wrong predictions are the
good ones — that's the moment learning actually happens.

**3. Errors are normal, not failure.** Break something on purpose in session 1
(there's a scripted moment for it) so the first red text they see is one *you*
caused. Say out loud, cheerfully: "Great, an error! Let's read it."

**4. Let them make it theirs.** Names, colours, personalities. The five minutes
spent choosing a pet colour buys you forty minutes of investment. Don't rush it.

**5. Pair, but don't let one drive.** With two students, each should have their
own laptop and own pet. Use "navigator moments": *"Aisha, tell Mia what to type
next."* Swap who explains. Two pets also means comparison — "why did yours grow
and hers didn't?" is a free teaching moment.

**6. Ten-minute rule.** If someone's been stuck on the same bug for ten minutes,
the frustration is now costing more than the lesson is worth. Sit down, debug it
*together, out loud*, modelling how you read the error.

---

# Session 1 — Meet Your Pet
### Variables, and the four types

**They will be able to:** create a variable; explain what `str`, `int`, `float`
and `bool` are and give an example of each; use `print()` and f-strings; run a
Python program; read an error message without panicking.

**File:** `session1_meet_your_pet.py`

| Time | What |
|---|---|
| 0:00 | Warm-up: the sticky-note game |
| 0:10 | The wow: run `demo_show_off.py` |
| 0:20 | Setup tour: how the window works |
| 0:30 | Live-code: name, age, size, hungry |
| 0:55 | **Break — 10 min** |
| 1:05 | Strings vs numbers, `print()` and f-strings |
| 1:25 | The scripted bug |
| 1:35 | Challenges 1–5 |
| 1:50 | Boss challenge + show each other |
| 2:00 | Done |

### 0:00 — Warm-up: the sticky-note game (no computers)

Give each student a stack of sticky notes. "A variable is a labelled box." Write
`name` on a note, stick it on a pen, and say the pen is now `name`. Now peel it
off and stick it on a phone — *the label moved; the box didn't.* That's
assignment.

Then: ask them to write on separate notes the name of a pet, its age, how tall it
is in metres, and whether it is hungry (yes/no). Four notes. Ask: **which of these
are the same kind of thing?** Let them sort. They'll naturally separate text from
numbers, and usually separate the yes/no too. Tell them Python calls those four
kinds `str`, `int`, `float`, `bool` — they just invented the type system.

### 0:10 — The wow

Open `demo_show_off.py`, have them press **Run**. Let it play. Don't explain
anything. Then: "Everything you just saw, you'll be able to write by session
four. Today we start with its name."

Point at the code panel: "that yellow highlight is Python, reading your code one
line at a time. That's all a computer does. It's fast, but it's not clever."

### 0:20 — Tour the window

Have them open `session1_meet_your_pet.py` and run it *before* changing anything.
Point out the three panels; especially the **Variables** panel — "the little
coloured tags are the types from your sticky notes."

Show the **Slower** button. Tell them to use it whenever something happens too
fast to follow.

### 0:30 — Live-code the four types

Work down the file together. At each one, *change it and re-run*:

```python
pet = Pet("dog")          # try "cat"
pet.name = "Mochi"        # str
pet.age = 2               # int
pet.size = 1.0            # float  -> try 0.5, then 2.0
pet.is_hungry = True      # bool
pet.color = "lavender"    # str
```

Questions to ask while they work:

- "Why does `"Mochi"` have quotes but `2` doesn't?"
  *(Quotes mean "treat this as text, don't try to understand it".)*
- "What happens if you write `pet.age = "2"` with quotes?"
  *(Let them try. The Variables panel now says `str`. It still displays — but
  watch what breaks later. Foreshadowing!)*
- "What do you think `pet.size = 3.0` will look like?" *(Predict, then run.)*

**Make sure both pets look different by the break.** Different animal, different
name, different colour. Ownership is the objective here as much as syntax.

### 1:05 — print() and f-strings

```python
pet.say("Hi! My name is " + pet.name)
pet.say(f"I am {pet.age} years old and my size is {pet.size}.")
print("The pet's name is", pet.name)
```

Teach `+` for gluing strings first, *then* f-strings as the nicer way. They need
to have felt the pain of `+` for the f-string to feel like a gift.

Point out the difference: `pet.say()` → speech bubble, `print()` → Console panel.
"`print` is for you, the programmer. `say` is for the pet."

### 1:25 — The scripted bug (don't skip this)

Tell them to type this exactly, and predict what happens:

```python
pet.say("I am " + pet.age + " years old")
```

It breaks. The Console goes red and says, in English, that they tried to glue a
word and a number together.

Now do the important part — **read it together, slowly**:
1. What line is it on? (It says.)
2. What is it complaining about?
3. What does it suggest?

Then fix it two ways: `str(pet.age)`, and the f-string. Tell them the truth:
*this exact error is one of the most common in all of programming, and every
professional has hit it this week.*

### 1:35 — Challenges 1–5, then the boss challenge

They're in the file, in order, with difficulty marked. Let them work; circulate.
Finish with each showing the other her pet.

### Common mistakes in session 1

| What you'll see | What's actually wrong | What to say |
|---|---|---|
| `pet.name = Mochi` → NameError | Missing quotes | "Python thinks Mochi is a variable name. How do we tell it that's just text?" |
| `pet.Name = "Mochi"` | Capital N | "Python is fussy about capitals. Compare it letter by letter with the cheat sheet." |
| `pet.say("hi"` | Missing `)` | "Count your brackets — every `(` needs a `)`." |
| Changed the file but nothing changed | Didn't save, or edited outside `main()` | "Is your code indented, inside `main()`? Did it save?" |
| Nothing at all happens | Deleted `run(main)` | "What's the last line of your file supposed to be?" |
| `"2" + 2` error | The quotes-around-number foreshadowing | Celebrate. Go back to the sticky notes. |

### If they finish early

- Build the pet's *whole* family: three pets, three names, three ages, each
  introducing itself. (Yes, `Pet()` can be called more than once.)
- Find a colour that isn't in the list, and work out what happens.
- Use a hex code: `pet.color = "#B5EAD7"`. Let them pick one from a colour picker.

---

# Session 2 — Pet Decisions
### Comparisons, `if` / `elif` / `else`, booleans, `ask()`

**They will be able to:** write a condition with `==`, `<`, `>`; write
`if`/`elif`/`else` with correct colons and indentation; explain the difference
between `=` and `==`; combine conditions with `and`/`or`/`not`; get input from a
human and convert a `str` to an `int`.

**File:** `session2_pet_decisions.py`

| Time | What |
|---|---|
| 0:00 | Warm-up: the "if" game |
| 0:10 | Recap + show-and-tell of session 1 pets |
| 0:20 | Comparisons produce booleans |
| 0:35 | `if`, then `if`/`else` |
| 0:55 | **Break — 10 min** |
| 1:05 | `elif` and the "first match wins" rule |
| 1:20 | `and` / `or` / `not` |
| 1:30 | `ask()` and `int()` |
| 1:40 | The Feeding Machine + Size Rule challenges |
| 1:55 | Boss challenge: personality quiz |

### 0:00 — Warm-up: the "if" game (no computers)

You call out conditions; they act. *"If you're wearing something blue, stand up.
Otherwise, wave."* Do four or five, getting sillier. Then add an `elif`: *"If
you're wearing blue, stand. Else if you have a phone in your pocket, hop. Else,
clap."*

Now the key question: **if someone is wearing blue AND has a phone, what do they
do?** They'll usually argue about it. Perfect. Tell them Python's rule: it checks
top to bottom, takes the *first* true one, and stops reading the rest. Write it
on paper. This one rule prevents about half the `elif` bugs you'll see.

### 0:20 — Comparisons make booleans

```python
is_baby = pet.age < 3
show("is_baby", is_baby)
```

The point to land: **a comparison is a question, and the answer is always `True`
or `False`.** Have them change `pet.age` and re-run, watching the `bool` tag in
the Variables panel flip. Do this three or four times — it's worth the minute.

Then, on the board:

| you write | it means |
|---|---|
| `=` | *put this value in the box* |
| `==` | *are these two the same?* |

This is the single most confused pair in the whole course. Come back to it twice
more today.

### 0:35 — `if`, and the shape of Python

```python
if pet.is_hungry:
    pet.say("My bowl is empty!")
    pet.eat()
```

Three things to point at, physically, on the screen:
1. the `:` at the end
2. the indent (4 spaces — VS Code does it for you after the colon)
3. *the indented lines only run when it's True*

Demonstrate the indent by un-indenting `pet.eat()` and re-running. The pet eats
even when it isn't hungry. "The indent isn't decoration. It's how Python knows
what's inside the `if`."

Then `if`/`else` with the growth rule — this is the idea from Jenny's original
brief, and it's the emotional centre of the session:

```python
if pet.age < 3:
    pet.grow(0.3)
else:
    pet.say("I am all grown up.")
```

Have them run it with `pet.age = 2`, then `pet.age = 5`. Two different worlds
from one program. That's control flow.

### 1:05 — `elif`

Use the mood ladder in the file. Have them predict which branch runs *before*
running, every time. Then change `pet.mood` to something that matches no branch
and let them discover `else` is the safety net.

### 1:30 — `ask()` and types, together

```python
answer = ask("How many treats?")     # this is a str, even if you type 7
treats = int(answer)                 # now it's an int
```

Look at the Variables panel: `answer` is tagged `str`, `treats` is tagged `int`.
Have them try `int("seven")` and read the friendly error.

This is where session 1's type lesson pays off. Make the connection explicit:
"remember the sticky notes?"

### Common mistakes in session 2

| What you'll see | What's wrong | What to say |
|---|---|---|
| `if pet.age = 3:` | `=` instead of `==` | "Are you telling it, or asking it?" |
| Missing `:` | | "What goes at the end of every `if` line?" |
| Everything runs regardless | Body not indented | "Which lines are *inside* the if?" |
| `elif` before `if` | Order | "`elif` means 'or else if' — it needs an `if` above it." |
| `if answer == yes:` | Missing quotes | Back to session 1: text needs quotes. |
| `if "5" > 3:` error | Comparing str to int | "Look at the type tags. Are these the same kind of thing?" |
| Only the first branch ever runs | Condition always True | "Print the variable just before the `if`. What is it really?" |

### If they finish early

- Add a fourth and fifth mood.
- Make a condition using `and` that is *almost* never true, and prove it.
- Nested `if`: hungry AND tired → eat, then sleep. Ask them to explain what the
  double indent means.

---

# Session 3 — Loops
### `for`, `range()`, counters, `while`, nested loops

**They will be able to:** write a `for` loop with `range()`; use the loop
variable; build a counter; write a `while` loop and explain how to stop it being
infinite; nest a loop inside a loop.

**File:** `session3_loops.py`

| Time | What |
|---|---|
| 0:00 | Warm-up: the annoying instructions game |
| 0:10 | `for i in range(n)` — the walk |
| 0:25 | The loop variable is usable |
| 0:40 | `range()` variations, countdown |
| 0:55 | **Break — 10 min** |
| 1:05 | Loop + `if` = the growth simulator |
| 1:20 | Counters (`total = total + 1`) |
| 1:30 | `while` loops and the infinite loop |
| 1:45 | Nested loops, the Patrol |
| 1:55 | Boss challenge: Pet Olympics |

### 0:00 — Warm-up: the annoying instructions game

Ask one student to give you instructions to walk across the room. She will say
"walk forward." Refuse — you are a computer, you need each step. Make her say
"step" seven times. Get visibly tired of it. Then: "is there a shorter way to
tell me?" She'll say something like "do that seven times." **That's a loop.** She
invented it; you just gave it a name.

### 0:10 — The first loop

```python
for i in range(4):
    pet.step()
```

Use the **Slower** button here — they should physically see the yellow highlight
jump back up to the `pet.step()` line four times. That visual is the entire
concept. Don't move on until both have watched it at slow speed.

The stepping stones on the ground are numbered 0–6 on purpose. Ask: "where did
the pet start?" *Stone zero.* Tell them programmers start counting at 0, and
`range(4)` gives `0, 1, 2, 3` — four numbers, starting at zero. Show it:

```python
for i in range(4):
    print(i)
```

### 0:25 — The loop variable

```python
for i in range(4):
    pet.say(f"step number {i}")
    pet.step()
```

The idea to land: `i` is a *variable that changes every time round*. Have them
change `range(4)` to `range(1, 5)` and watch the numbers shift.

### 1:05 — The growth simulator (the highlight of the session)

This is the payoff of sessions 2 and 3 combined — exactly the thing Jenny
described in the original brief:

```python
for year in range(1, 6):
    pet.birthday()
    if pet.age <= 3:
        pet.grow(0.25)
    else:
        pet.say("I stopped growing at 3.")
```

Watch it at normal speed, then slow. The pet grows, grows, grows, then stops
while the birthdays keep coming. Ask: "how many times did the `if` run? How many
times did the `grow` run? Why are those different numbers?"

### 1:30 — `while`, and the infinite loop

Do the infinite loop **on purpose** — it's a rite of passage:

```python
energy = 3
while energy > 0:
    pet.jump()
    # deliberately forget: energy = energy - 1
```

The window freezes. Let it sit for five seconds. Then show them how to stop it
(click the terminal panel and press `Ctrl+C` — yes, `Ctrl` on a Mac too; or the
trash-can icon on the terminal). Then fix it together.

The rule to write down: **a `while` loop needs something inside it that changes
the answer to the question, or it never ends.**

### 1:45 — Nested loops

```python
for round_number in range(2):
    for beat in range(2):
        pet.jump()
    pet.spin()
```

Predict before running: how many jumps, how many spins? (4 and 2.) Most students
guess 2 and 2 the first time. Let them be wrong, then run it slowly.

### Common mistakes in session 3

| What you'll see | What's wrong | What to say |
|---|---|---|
| `for i in range(4)` → error | Missing `:` | Same as `if`. |
| Loop body not indented | | "What's inside the loop?" |
| Off by one | `range(1,5)` vs `range(5)` | "Add a `print(i)` inside and read the numbers." |
| Window freezes forever | Infinite `while` | "What inside the loop is supposed to change?" |
| `for i in range(4): pet.step()` written all on one line | It works but... | Accept it, then ask them to write it the normal way. Readability counts. |
| Pet stops moving at the fence | Not a bug | "The number can't go past 6 — the program kept running, the pet just ran out of garden." |

### If they finish early

- Make the pet walk an increasing distance each round: 1 step, then 2, then 3.
  (Hint: `for i in range(1, 4): for step in range(i):`)
- Count how many even numbers are in `range(20)` using a counter and `%`.
- Make a pet that grows a tiny bit every single step for 6 steps.

---

# Session 4 — Functions, Lists, and Your Own Game
### `def`, parameters, `return`, lists, `random`, final project

**They will be able to:** write a function with parameters; explain why functions
are useful; use `return`; make a list, index it, loop over it, and append to it;
use `random`; design and build a small program of their own.

**File:** `session4_functions_and_lists.py`

| Time | What |
|---|---|
| 0:00 | Warm-up: the recipe game |
| 0:10 | `def` — teaching Python a new trick |
| 0:25 | Parameters: same function, different pet |
| 0:40 | `return` |
| 0:50 | **Break — 10 min** |
| 1:00 | Lists, and looping over them |
| 1:15 | `random` |
| 1:25 | Final project briefing |
| 1:30 | Build |
| 1:50 | Showcase + what's next |

### 0:00 — Warm-up: the recipe game

"Tell me how to make a cup of tea." They'll give steps. Now: "how do you make
*two* cups?" They will *not* repeat every step — they'll say "do that again, but
for the second cup." Write their tea steps on paper, draw a box around them, and
title the box `make_tea`. That's a function: a named box of steps you can use
whenever you want.

Then ask: "what if one person wants sugar?" → that's a **parameter**.

### 0:10 — `def`

```python
def greet(pet):
    pet.say(f"Hello! I am {pet.name} and I am {pet.age}.")
    pet.wag()
```

Two things to be explicit about, because they're the usual stumbles:

1. **Functions are defined above `main()`, not inside it.** Point at the file.
2. **Defining is not running.** `def greet(pet):` doesn't do anything by itself —
   nothing happens until you write `greet(pet)`. Prove it: comment out the call
   and re-run. Nothing. That surprises people, and it should.

### 0:25 — Parameters

`do_trick(pet, "spin")` and `do_trick(pet, "jump")` — one function, two
behaviours. Ask them to add a trick to it. This is also a sneaky `if`/`elif`
revision.

### 0:40 — `return`

```python
def years_to_dog_years(age):
    return age * 7
```

The distinction worth ten minutes: some functions **do** something (`greet`),
some functions **hand back an answer** (`years_to_dog_years`). `return` is how
the answer gets out.

Show what happens if you forget the `return`: the function gives back `None`.
Show `None` in the Variables panel — new type tag, grey.

### 1:00 — Lists

```python
tricks = ["jump", "spin", "dance"]
for trick in tricks:
    do_trick(pet, trick)
```

Point out how much nicer this is than `range()` — no counting at all. Then
`tricks[0]`, `len(tricks)`, `tricks.append("sit")`.

Expect an `IndexError` when someone tries `tricks[3]` on a 3-item list. The
friendly error explains it; use the moment to repeat "the first one is zero."

### 1:25 — Final project

Brief it from the checklist at the bottom of the session 4 file. The requirements
are deliberately a *review sheet in disguise* — 3 variables of 2+ types, an
`if`/`elif`/`else`, a loop, a function of their own, a list, and an `ask()`.

Give them real choice about *what* to build. Ideas are listed in the file
(a day-in-the-life, a guessing game, a two-pet race, a birthday party).

**Scope control is your main job here.** If someone plans something enormous,
say: "that's a great version 2 — what's the smallest version that works? Build
that first, then add." Getting something finished and shown beats something
ambitious and broken, every time, especially at the end of a first course.

### 1:50 — Showcase, and then this bit matters

Have each girl run her project for the other and *explain one line she's proud
of*. Applaud properly.

Then close the course deliberately. Some things worth saying:

- Everything they used today — variables, conditions, loops, functions, lists —
  is what professional software is made of. The pet is a toy; the ideas are not.
  The same `if` statement runs in a hospital scheduling system and a video game.
- Python is used for real work by biologists, doctors, artists, economists and
  astronomers. It is the language of modern science, not just of software
  companies. (If it fits: Jenny's own lab uses code like this.)
- The feeling of being stuck and then unstuck *is* the job. Nobody outgrows it.
  Professionals are just people who've been stuck more times.

**Where to go next** (put these on the handout):

- Keep going with PetPal — `my_pet.py` is theirs forever
- *Python Crash Course* (Eric Matthes) — the standard, and genuinely good
- Turtle graphics (already in Python) → then `pygame` for real games
- **Girls Who Code** clubs, **Technovation**, local hackathons
- If a girl has caught fire: the "Automate the Boring Stuff" free online book

---

# Session 5 (optional) — Beyond the Fence
### Packages, environments, and git

**Student file:** `SESSION5.md` · **Setup:** Part 2 of `SETUP.md` ·
**Project:** `pet_park/`

## Read this before you schedule it

**No, they do not need Anaconda or a virtual environment for Sessions 1–4.** PetPal
is pure standard library — tkinter and nothing else. Keeping it that way is a
deliberate choice, not laziness: a beginner who is asked to create an environment
before writing her first line of code learns that programming is mostly ceremony you
don't understand. Everything in Session 5 exists to solve a problem, and it only
lands if they have *had* the problem first.

**This is not a two-hour session.** Part A (packages and environments) is about two
hours. Part B (git) is another two. Run them as two separate meetings if you can —
git in the back half of a four-hour day will not stick. The two parts are fully
independent; you can also do Part A now and Part B a month later.

**Two admin things to settle before the day:**

- **GitHub needs an account holder aged 13+**, and the students should have a parent's
  or guardian's agreement. Don't find this out in the room. `SESSION5.md` gives an
  equally good Option A — a bare repo in a shared folder or on a USB stick — which
  teaches identical commands with no accounts at all. Honestly, for two students in
  one room, Option A is less friction and keeps the lesson on git rather than on a
  website's UI. Use GitHub if the portfolio value matters to them, and it may well.
- **Anaconda's licence.** Anaconda's default channels are free for individuals,
  academic institutions, and non-profit/research organizations, and for companies
  under 200 people. MSK is a non-profit research institution, so this is almost
  certainly fine — but if your IT department would rather avoid the question
  entirely, **Miniforge** (conda-forge's installer) uses the community channel and
  every command in the session works unchanged.

## Part A — Packages and environments (~2 hrs)

| Time | What |
|---|---|
| 0:00 | Run `growth_chart.py` and watch it crash |
| 0:15 | What a package is; where the code comes from |
| 0:35 | The two-projects problem (tell it as a story) |
| 0:50 | `conda create` / `activate` — the box metaphor |
| 1:05 | **Break** |
| 1:15 | `conda install matplotlib`, run the chart |
| 1:35 | Reading `growth_chart.py` — it's all Session 3 code |
| 1:50 | Challenges: a second environment, `conda env export` |

**Open by breaking it.** Have them run `growth_chart.py` before installing anything.
`ModuleNotFoundError: No module named 'matplotlib'` *is* the lesson hook. Ask: "Python
knew what `random` was in Session 4. Why not this?"

**The story to tell for environments.** Don't define it — describe the trap. "You
install the newest matplotlib for PetPal. Next year you join a science club whose
code needs an old one. You install the old one. PetPal breaks. You put the new one
back. The club's project breaks." Let them sit in it for a moment and suggest fixes.
Someone will say "you'd need two separate copies" — that's the answer, and she said it.

**The prompt is the teaching aid.** Point at `(base)` becoming `(petpal)` every single
time. Most conda confusion, forever, comes down to not looking at that word. Make
"which box am I in?" a reflex. Have them deliberately `conda deactivate` and re-run the
chart so they see the crash come back — the same error, now with a cause they
understand.

**When `conda install matplotlib` pulls in a dozen packages**, stop and point at it.
"You asked for one. Why are there twelve?" Dependencies, and resolving them is most of
what conda is actually for.

**The payoff that matters.** After the chart appears, open `growth_chart.py` and read
it together. A loop, an `if`, two lists — all Session 3. Only the last eight lines are
new. Say it plainly: *the Python you already know is the Python scientists use.* The
package is just a set of extra verbs.

**`conda env export` is worth the last ten minutes** even if it feels advanced. One
file that lets another lab rebuild your exact environment and get your exact numbers
is, in a research institution, the entire ballgame. This is the moment to mention what
reproducibility means and why people care so much.

### Common mistakes in Part A

| What you'll see | What's wrong | What to say |
|---|---|---|
| `conda: command not found` | Terminal opened before install finished, or wrong terminal on Windows | Close it; on Windows use **Anaconda Prompt**, not Command Prompt |
| Installed into `(base)` | Forgot `conda activate petpal` | "Look at your prompt. Which box are you in?" |
| Still `ModuleNotFoundError` after installing | VS Code is using a different Python | *Python: Select Interpreter* → pick `petpal`, **and open a fresh terminal** (SETUP.md §5.3) |
| `python` vs `python3` | Windows vs macOS | It's on the cheat sheet; it catches everyone once |
| Conda hangs for minutes on "Solving environment" | Normal | Let it run. Good moment for the dependency conversation |

## Part B — Git and the Pet Park (~2 hrs)

| Time | What |
|---|---|
| 0:00 | The `park_final_REAL_v3.py` problem |
| 0:10 | Three ideas: repo, commit, remote |
| 0:20 | Solo git: `init`, `status`, `add`, `commit`, `log` |
| 0:40 | Wreck a file, `git restore` it — the time machine |
| 0:55 | **Break** |
| 1:05 | Remote, `push`, `clone` |
| 1:20 | Each claims a trick file; build the show together |
| 1:45 | The deliberate merge conflict |
| 2:00 | Push the finished Pet Park |

**Open with their own bad habit.** Ask how they share files now. Write the
`park_final_REAL_mia_edit.py` list on the board. They'll laugh because they recognise
it. Everything after that is the fix.

**Teach `git status` as a reflex, not a command.** Run it after literally every step.
It is safe, it explains the current state, and it usually names the next command. A
student who runs `git status` when confused is a student who can get herself unstuck.

**The restore demo is the emotional centre of Part B.** Have them delete half of
`main()` on purpose, run it, confirm it's broken, then `git restore park.py`. The point
to say out loud: *this is not about being tidy, it's about being allowed to try
things.* Once nothing can be lost, experimenting stops being scary.

**Why each student owns her own trick file.** The clean-merge experience has to come
first. When they each edit their own file and `git pull` silently combines the work,
the magic is obvious and un-scary. Only once that's felt do you introduce a conflict —
deliberately, in `README.md`, where nothing can actually break. Doing it in that order
is the difference between "git is clever" and "git is terrifying".

**When the conflict appears, slow down.** Read the markers together, out loud. Say
clearly: nothing is broken, nothing is lost, git simply refuses to guess. Two people
changed the same line; a human has to choose. Then fix it in twenty seconds and watch
the fear evaporate.

**Commit messages are a writing lesson.** "update" vs "Add zoomies trick to Mia's
file". Ask which one they'd want to read in six months. It's a genuinely useful habit
and it costs nothing to teach now.

### Common mistakes in Part B

| What you'll see | What's wrong | What to say |
|---|---|---|
| `Please tell me who you are` | git config never run | SETUP.md §5.3 — name and email, once per computer |
| An unfamiliar editor opens on commit | Forgot `-m "message"` | If it's vim: `Esc`, then `:wq`, Enter |
| `Updates were rejected` on push | Partner pushed first | "Pull, then push." This is the normal rhythm |
| `You have divergent branches` | `pull.rebase` unset | `git config --global pull.rebase false` (it's in SETUP.md) |
| Conflict markers committed into the file | Didn't delete `<<<<<<<` / `=======` / `>>>>>>>` | Those three lines always go. Then `add` and `commit` |
| Edited each other's trick file | The one rule | Restate it: your file is yours. This is why it works |
| `__pycache__` showing in `git status` | Missing ignore | It's in `.gitignore` already — good moment to explain why |

### If they finish early

- `git branch` and `git switch` — make a wild change on a branch, switch away, switch
  back. This is where real teams live.
- Add a third pet to the park and give it to whoever finishes first.
- Put the growth chart into the repo as a script both of them can improve.
- On GitHub: open an **Issue** on each other's repo asking for a feature. It's how
  open-source actually works, and it's funnier than it sounds.

## What Session 5 is really for

Sessions 1–4 teach the language. Session 5 teaches the *practice* — and it's the part
that usually goes untaught until someone's first job or first research project. Two
students who can make an environment and use git are, in a very practical sense, ready
to join a real project. That's a reasonable thing to tell them.


---

## Assessment — what "getting it" looks like

You don't need to test them. Watch for these instead:

**Session 1** — She changes a value, predicts the result out loud, and is right.
She uses the word "string" naturally.

**Session 2** — She can explain why one branch ran and another didn't, without
running it. She catches her own `=` vs `==` mistake.

**Session 3** — She reaches for a loop *unprompted* when she notices repetition.
This is the big one. It means she's thinking like a programmer.

**Session 4** — She writes a function because she's bored of repeating herself,
not because you asked her to.

**Session 5** — She checks her prompt before wondering why an import failed, and she
runs `git status` when she's confused instead of asking you what happened.

**Across all four** — She reads the error message before asking you. That's the
single best predictor that she'll keep going after the course ends.

---

## Troubleshooting

**"No module named tkinter"** — Rare with a python.org install; happens on Linux
(`sudo apt install python3-tk`) and with Homebrew Python on macOS
(`brew install python-tk`).

**"No module named petpal"** — The file they're running isn't in the same folder
as `petpal.py`. Make sure they used **File → Open Folder** on `PetPal` rather than
opening a single file.

**Window opens then closes instantly** — `run(main)` is missing, or there's a
syntax error. The terminal/shell panel will show it.

**Window is too big for the screen** — It's resizable; drag the corner. It needs
about 1150×620.

**A syntax error stops anything from running** — PetPal can explain runtime
errors, but a *syntax* error (missing bracket, missing colon) stops Python before
PetPal ever starts. VS Code underlines these in red *before* they run — teach them
to hover the squiggle, and to read the terminal panel, which names the line.

**"I changed it and nothing happened"** — Auto Save is off. Turn it on
(File → Auto Save) rather than teaching them to remember `Cmd/Ctrl+S`.

**VS Code opens a debug configuration picker** — they pressed `F5`. Tell them to use
the **▷** button or `Ctrl+F5` instead; the course never needs the debugger.

**The pet won't move past stone 6** — Working as intended. The garden has a
fence. Turn around.

---

## File map

```
PetPal/
├── SETUP.md                         GIVE THIS TO THE STUDENTS FIRST
│                                      Part 1 = sessions 1-4 (Mac/Linux/Windows)
│                                      Part 2 = session 5 only (conda + git)
├── START_HERE.md                    the short version + the full command list
├── TEACHER_GUIDE.md                 this file
├── CURRICULUM.md                    objectives and skills at a glance
├── check_setup.py                   students run this to prove they're ready
├── petpal.py                        the engine (students don't touch this)
├── demo_show_off.py                 run this in minute 10 of session 1
├── my_pet.py                        free playground
├── session1_meet_your_pet.py        variables and types
├── session2_pet_decisions.py        if / elif / else
├── session3_loops.py                for / while
├── session4_functions_and_lists.py  def / lists / final project
├── solutions_session1..4.py         worked answers to every challenge
├── SESSION5.md                      session 5: packages, environments, git
├── growth_chart.py                  the matplotlib payoff (crashes until installed)
├── pet_park/                        the two-person git project
│   ├── park.py                        shared - pull before you edit
│   ├── tricks_a.py / tricks_b.py      one owner each - this is why merges work
│   ├── README.md                      where the deliberate conflict happens
│   ├── .gitignore
│   └── petpal.py                      a copy, so the repo stands alone
└── handouts/PetPal_Handouts.pdf     printable worksheets + cheat sheet
```
