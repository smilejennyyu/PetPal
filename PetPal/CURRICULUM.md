# PetPal — Curriculum at a glance

**4 sessions × 2 hours · Grade 8 · no prior programming experience · Python 3**

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
```

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

## Habits taught alongside the syntax

These matter as much as the language, and are assessed by observation:

1. **Predict, then run.** Say what will happen before pressing Run.
2. **Read the error.** Out loud, from the top, including the line number.
3. **Change one thing at a time.** The core debugging discipline.
4. **Small steps, run often.** Never write 20 lines before testing.
5. **Comment your intent.** Why, not what.
6. **Make it yours.** Every program should look like the person who wrote it.

---

## Alignment notes

Maps to CSTA K-12 CS Standards, grades 6–8: **2-AP-11** (variables), **2-AP-12**
(control structures: loops and conditionals), **2-AP-13** (decomposition into
procedures), **2-AP-14** (modular programs with procedures), **2-AP-16**
(incorporating existing code and giving attribution), **2-AP-17** (systematic
testing and refinement), **2-AP-19** (documentation).
