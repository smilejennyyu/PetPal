# PetPal — Curriculum at a glance

**4 sessions × 2 hours, + an optional Session 5 · Grade 8 · no prior experience · Python 3**

Every concept is taught through one continuous artefact: an electronic pet the
student builds and owns. Concepts are introduced only when the pet needs them.

---

## Concept map

```
SESSION 1          SESSION 2          SESSION 3          SESSION 4
variables    ──►   conditions   ──►   repetition   ──►   abstraction
                                                          + collections

str  name          ==  !=  <  >       for / range        def
int  age           if                 loop variable      parameters
float size         if / else          counters           return
bool is_hungry     if / elif / else   while              lists
print()            and / or / not     nested loops       indexing, len
f-strings          ask()                                 append
comments           int() / str()                         random
                                                         dictionaries

                   SESSION 5 (optional) - how programmers actually work
                   ───────────────────────────────────────────────────
                   packages · conda environments · reproducibility
                   git: commit, history, remote, pull/push, conflicts
```

**Sessions 1–4 require nothing but a Python install** — PetPal uses only the
standard library, no pip, no conda, no virtual environment. That is deliberate:
tooling is introduced in Session 5, *after* the students have hit the problem it
solves.

Each session ends with a mini-project that *requires* everything from the
sessions before it. Nothing is taught and then abandoned.

---

## Session 1 — Meet Your Pet

**Big idea:** A program is a list of instructions, and data has kinds.

| Skill | Evidence it landed |
|---|---|
| Create and assign a variable | Names her own pet, changes it, re-runs |
| Distinguish `str` / `int` / `float` / `bool` | Predicts the type tag before it appears |
| Use quotes correctly | Stops asking why `2` has no quotes |
| `print()` vs displayed output | Uses `print()` to check a value |
| Build a string with `+` and with f-strings | Prefers f-strings by the end |
| Read a runtime error | Finds the line number unprompted |

**Mini-project:** a pet profile — name, age, size, colour, and a one-line
self-introduction built with an f-string.

---

## Session 2 — Pet Decisions

**Big idea:** Programs choose. A condition is a question whose answer is a bool.

| Skill | Evidence it landed |
|---|---|
| Write comparisons (`==`, `!=`, `<`, `>`, `<=`, `>=`) | Explains `=` vs `==` correctly |
| `if` with correct colon + indentation | Fixes her own indentation errors |
| `if` / `else` | Predicts which branch runs |
| `if` / `elif` / `else` chains | Knows the first match wins and the rest are skipped |
| Combine with `and`, `or`, `not` | Writes a two-part condition that works |
| Input and type conversion (`ask()`, `int()`) | Understands why `int()` is needed |

**Mini-projects:** the Feeding Machine (hunger decides the action) and the
Personality Quiz (three questions → a score → a branch).

---

## Session 3 — Loops

**Big idea:** Computers are for repetition. Say it once, run it many times.

| Skill | Evidence it landed |
|---|---|
| `for i in range(n)` | Reaches for a loop without being told |
| Zero-indexing and `range(a, b, step)` | Predicts the numbers a range produces |
| Use the loop variable in the body | Uses `i` inside an f-string |
| Accumulator / counter pattern | Writes `total = total + 1` correctly |
| `while` loops | Explains how to stop one being infinite |
| `if` inside a loop | Builds the growth simulator and explains the run counts |
| Nested loops | Correctly predicts total iterations |

**Mini-projects:** the Growth Simulator (grow until age 3, then stop — the loop +
condition combination) and the Pet Olympics routine.

---

## Session 4 — Functions, Lists and Your Own Game

**Big idea:** Name a chunk of work and reuse it. Group data together.

| Skill | Evidence it landed |
|---|---|
| Define a function with `def` | Understands defining ≠ running |
| Parameters | Calls the same function with different arguments |
| `return` a value | Distinguishes doing from answering |
| Create, index and loop a list | Knows the first item is `[0]` |
| `len()`, `.append()` | Uses them without prompting |
| `random.choice` / `randint` | Adds unpredictability on purpose |
| Read a dictionary | Retrieves a value by key |
| Design a small program | Plans it before typing |

**Final project:** a self-designed pet program that must contain at least 3
variables of 2+ types, one `if`/`elif`/`else`, one loop, one student-written
function, one list, and one `ask()`.

---

## Session 5 (optional) — Beyond the Fence

**Big idea:** Other people wrote code you can use, and other people will work on
code with you. Both need tools.

Run as **two ~2-hour halves**; they're independent.

### Part A — packages and environments

| Skill | Evidence it landed |
|---|---|
| Explain what a package is and where it comes from | Can name the difference between `random` and `matplotlib` |
| Install one with `conda install` | Reads the dependency list and asks why there are twelve |
| Explain why environments exist | Can retell the two-projects-two-versions problem |
| Create, activate, deactivate, list environments | Checks the `(petpal)` prompt before debugging an import |
| Use matplotlib to plot data she generated | Recognises the plotting script as Session 3 code plus 8 lines |
| Export an environment | Can say why a scientist would need `environment.yml` |

**Mini-project:** the pet's growth chart — the Session 3 growth rule, recorded into
lists and plotted as a curve.

### Part B — git and collaboration

| Skill | Evidence it landed |
|---|---|
| Explain repo / commit / remote | Describes a commit as a snapshot, not a file |
| `init`, `status`, `add`, `commit`, `log` | Runs `git status` when confused, unprompted |
| Recover a file with `git restore` | Willing to try a risky change because undo exists |
| `clone`, `push`, `pull` | Completes an edit→commit→pull→push cycle unaided |
| Work in parallel on one project | Understands why file ownership prevents conflicts |
| Resolve a merge conflict | Deletes the markers and keeps both versions, calmly |
| Write a useful commit message | Can say why "update" is a bad one |

**Mini-project:** Pet Park — a two-pet show where each student owns her own trick
module, plus one deliberate merge conflict in the shared README.

---

## Habits taught alongside the syntax

These matter as much as the language, and are assessed by observation:

1. **Predict, then run.** Say what will happen before pressing Run.
2. **Read the error.** Out loud, from the top, including the line number.
3. **Change one thing at a time.** The core debugging discipline.
4. **Small steps, run often.** Never write 20 lines before testing.
5. **Comment your intent.** Why, not what.
6. **Make it yours.** Every program should look like the person who wrote it.
7. **(Session 5) Check which environment you're in** before you debug an import.
8. **(Session 5) Commit early, commit often** — and say what you changed.

---

## Alignment notes

Maps to CSTA K-12 CS Standards, grades 6–8: **2-AP-11** (variables), **2-AP-12**
(control structures: loops and conditionals), **2-AP-13** (decomposition into
procedures), **2-AP-14** (modular programs with procedures), **2-AP-16**
(incorporating existing code and giving attribution), **2-AP-17** (systematic
testing and refinement), **2-AP-19** (documentation).
