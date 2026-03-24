# Agent Instructions — Snake Course Content Generation

You are writing the lesson content for a hands-on introductory Python course. Students build toward a fully functional terminal Snake game over 11 modules. Your job is to write each module's lesson page and, where specified, the accompanying starter and solution code files.

Read these instructions **in full** before writing any content.

---

## 1. Source Files (Do Not Modify)

These files are your source of truth. All code you teach must converge on them exactly.

| File | Role |
|---|---|
| `assets/code/main.py` | The finished Snake game. Module 10's deliverable must match this file. |
| `assets/code/keyboard.py` | Provided helper module. Students never edit or write this. |
| `syllabus.md` | Module titles, concept lists, and mini-project descriptions. Follow precisely. |

---

## 2. Audience & Voice

- **Who:** Absolute beginners, ages 13+. Assume zero programming experience.
- **Language:** Write all prose in **Spanish**. Code comments in **Spanish**. Variable names and Python keywords stay in English (they are part of the language).
- **Tone:** Encouraging, conversational, direct. Talk *to* the student, not *at* them. Use "tú" (informal). Celebrate small wins ("¡Tu primer programa funciona!"). Avoid jargon unless you're actively defining it in that paragraph.
- **Length:** Each module lesson should be roughly **800–1500 words** of prose (not counting code blocks). Enough to teach clearly, short enough to not overwhelm.

---

## 3. Pedagogical Rules

### 3.1 Concept Introduction Pattern

Every new concept follows this sequence:

1. **Motivate** — One or two sentences on *why* this matters. Connect it to the snake game when possible ("Necesitamos que el programa recuerde la posición de la serpiente — para eso existen las variables").
2. **Explain** — Plain-language definition. No formal CS jargon unless you immediately unpack it.
3. **Minimal example** — A short, runnable snippet (≤10 lines) that demonstrates the concept in isolation. These examples should be **standalone** — they should NOT be part of the snake game. Use everyday themes (greetings, food, animals, sports).
4. **Connect to the project** — Show or hint how this concept will appear in the snake game. In early modules this is a teaser; in later modules it's the actual game code.

### 3.2 Strict Ordering

- **Never** use a concept that hasn't been taught yet in the current or a previous module. If a mini-project needs something from a later module, simplify the mini-project instead.
- **Never** show the final `main.py` until Module 10. Before that, students only see the fragments relevant to their current module.

### 3.3 Code Formatting

- All code blocks use Python fenced syntax (` ```python `).
- Keep snippets short. If a snippet exceeds ~25 lines, break it into smaller pieces with prose between them.
- When showing new code being **added** to an existing file, use a comment like `# --- NUEVO ---` to mark the addition, and include a few lines of surrounding context so the student knows where to place it.

### 3.4 Common Mistakes

Each module should include a short "Errores comunes" section (2–3 items) highlighting mistakes beginners typically make with that module's concepts. Format as a brief paragraph or callout, not a list dump.

---

## 4. Mini-Project Approach (Hybrid Scaffolding)

### Modules 1–6: Starter files provided

Deliver two files per mini-project:

| File | Purpose |
|---|---|
| `mini_project.py` | **Starter** — Contains structure, comments, and `# TODO` markers where the student writes code. Should be runnable as-is (prints nothing, or prints a placeholder) so the student can run it before starting. |
| `solution.py` | **Solution** — The complete working version. |

**Starter file rules:**
- Include `# TODO:` comments in Spanish that tell the student *what* to do, not *how*.
- Provide just enough scaffolding that the student isn't staring at a blank file, but not so much that the exercise is trivial.
- Any code the student hasn't learned yet (e.g., an `input()` call in Module 1) should be **pre-written** in the starter with a brief comment explaining "this line is provided for you."

### Modules 7–11: Instructions only

By Module 7 students have written enough code to start from scratch. The lesson text describes the mini-project requirements clearly, and only a `solution.py` file is provided (no starter).

**Exception:** Module 8 introduces `keyboard.py` for the first time. Provide a starter file for this module that contains the `import` and `setup_keyboard()` lines pre-filled, plus the basic game loop skeleton.

---

## 5. Code Progression Contract

This maps each module to the specific lines and patterns from `main.py` that get introduced. **Follow this mapping exactly.** The mini-project for each module should exercise these concepts even if the mini-project itself is a different program.

### Module 1 — Hello, Python!

**Concepts from main.py introduced:**
```python
player_name = "Player"
print("Bienvenido,", player_name)
print("Tu puntaje actual es:", 0)
```

**Mini-project deliverable:** A script that stores a name in a variable and prints a personalized greeting plus a score line. Output should look like:
```
Bienvenido, María
Tu puntaje actual es: 0
```

---

### Module 2 — Numbers & Decisions

**Concepts from main.py introduced:**
```python
grid_width = 150
grid_height = 30
snake_head_col = grid_width // 2   # integer division
snake_tail_length = 0
is_game_over = False               # booleans
```
Arithmetic operations (`+`, `-`, `*`, `//`), comparisons, `if`/`elif`/`else`.

**Mini-project deliverable:** A number guessing game. The program picks a number, the player guesses, the program says higher/lower/correct. Uses `if`/`elif`/`else` and comparisons. (Note: this requires `input()` and a loop — `input()` can be given without deep explanation as "this is how Python asks the player to type something," and the loop concept is previewed lightly but formally taught in Module 3.)

---

### Module 3 — Loops

**Concepts from main.py introduced:**
```python
while True:
    # ... game loop (just the structure, not the contents yet)
    break  # exit condition
```
```python
for row in range(grid_height):   # preview only — "we'll use this in Module 6"
```

**Mini-project deliverable:** A countdown from 10 to 0 that prints "¡Despegue!" at the end. Demonstrates `while` with a counter, and a `for`/`range` version of the same thing.

---

### Module 4 — Combining Conditions

**Concepts from main.py introduced:**
```python
if key == "UP" and current_direction != "DOWN":
    current_direction = "UP"
```
The `and` / `or` / `not` operators. Compound conditions.

**Mini-project deliverable:** A text adventure where the player has an inventory and doors require multiple conditions to open.

---

### Module 5 — Lists & Tuples

**Concepts from main.py introduced:**
```python
snake_tail = []
snake_tail.append((snake_head_col, snake_head_row))
snake_tail = snake_tail[-snake_tail_length:]   # negative slicing
food_item = (food_col, food_row)               # tuple
(snake_head_col, snake_head_row) in snake_tail  # membership check
```

**Mini-project deliverable:** A 1D trail tracker. The player inputs left/right, a position variable updates, and every visited position is appended to a list. At each step, print the list of visited positions.

---

### Module 6 — Nested Loops & the Grid

**Concepts from main.py introduced:**
```python
for row in range(grid_height):
    row_chars = ""
    for column in range(grid_width):
        if (row == 0 or row == grid_height - 1) and (column == 0 or column == grid_width - 1):
            row_chars += "+"
        elif row == 0 or row == grid_height - 1:
            row_chars += "-"
        elif column == 0 or column == grid_width - 1:
            row_chars += "|"
        elif column == snake_head_col and row == snake_head_row:
            row_chars += "@"
        elif column == food_item[0] and row == food_item[1]:
            row_chars += "*"
        else:
            row_chars += " "
    print(row_chars)
```

**Mini-project deliverable:** A static grid renderer. Hardcoded `grid_width`, `grid_height`, a `@` at a hardcoded position, and a `*` at another. No movement, no game loop — just print the grid once and exit. Use a smaller grid (e.g., 40×15) for readability.

---

### Module 7 — Functions & Imports

**Concepts from main.py introduced:**
```python
import os
import time
import random
from keyboard import setup_keyboard, get_key_pressed

random.randint(1, grid_width - 2)
time.sleep(0.1)
os.system("cls" if os.name == "nt" else "clear")
```

**Mini-project deliverable:** The Module 6 grid, but now the `*` position is randomized with `random.randint()` on each run. Add a `time.sleep()` call to pause before the program ends so the student can see the output.

---

### Module 8 — Real-Time Input & the Game Loop

**Concepts from main.py introduced:**
```python
setup_keyboard()

while True:
    key = get_key_pressed()

    # Move head based on key
    if key == "UP":
        snake_head_row -= 1
    elif key == "DOWN":
        snake_head_row += 1
    elif key == "LEFT":
        snake_head_col -= 1
    elif key == "RIGHT":
        snake_head_col += 1

    # Render (the grid from Module 6)
    print("\033[H", end="")
    # ... grid drawing ...

    time.sleep(0.1)
```

**Mini-project deliverable:** A `@` character that moves freely on a bordered grid using arrow keys. No direction state, no collision, no food — just direct input-to-movement. This is the first "it feels like a game" moment.

**Note:** Provide a starter file for this module (see Section 4 exception).

---

### Module 9 — Game Rules & State

**Concepts from main.py introduced:**
```python
current_direction = "RIGHT"
is_game_over = False

# Direction update with reverse prevention
if key == "UP" and current_direction != "DOWN":
    current_direction = "UP"

# Movement based on direction (replaces direct key-based movement)
if current_direction == "UP":
    snake_head_row -= 1

# Wall collision
if (snake_head_row <= 0
        or snake_head_row >= grid_height - 1
        or snake_head_col <= 0
        or snake_head_col >= grid_width - 1):
    is_game_over = True

if is_game_over:
    print("Game over")
    break
```

**Mini-project deliverable:** The Module 8 project upgraded: the `@` now auto-moves in `current_direction`, arrow keys change direction (with reverse prevention), and hitting a wall ends the game. This is Snake without food or a tail.

---

### Module 10 — Food, Growth & the Tail

**Concepts from main.py introduced:**
All remaining code — food spawning, food collision detection, tail growth, self-collision, score display. The deliverable **is** the complete `main.py`.

```python
# Food spawning (before game loop)
while True:
    food_col = random.randint(1, grid_width - 2)
    food_row = random.randint(1, grid_height - 2)
    if (food_col, food_row) != (snake_head_col, snake_head_row):
        break
food_item = (food_col, food_row)

# Inside game loop — tail update
if snake_tail_length > 0:
    snake_tail.append((snake_head_col, snake_head_row))
    snake_tail = snake_tail[-snake_tail_length:]

# Food collision
if (snake_head_col, snake_head_row) == food_item:
    snake_tail_length += 1
    # re-spawn food...

# Self-collision (added to existing wall check)
or (snake_head_col, snake_head_row) in snake_tail

# Score display
print("Tu puntaje actual es:", snake_tail_length * 5)

# Tail rendering (added to grid)
elif (column, row) in snake_tail:
    row_chars += "o"
```

**Mini-project deliverable:** The finished Snake game. Provide the complete `main.py` as the solution. The lesson walks through adding each piece to the Module 9 project.

---

### Module 11 — Polish & Make It Yours (Bonus)

No new `main.py` concepts. This is a freeform module with extension ideas. Provide code sketches (not full solutions) for:
- Speed increase as the snake grows
- High-score tracking with file I/O
- Multiple food items on screen

End with a full guided read-through of `main.py` as a capstone review.

---

## 6. File Structure & Formatting

### 6.1 Folder Layout

Each module lives in its own folder:

```
modules/
├── 01-hello-python/
│   ├── lesson.md           # The lesson page
│   ├── mini_project.py     # Starter file (Modules 1–6 + 8 only)
│   └── solution.py         # Complete solution
├── 02-numbers-decisions/
│   ├── lesson.md
│   ├── mini_project.py
│   └── solution.py
...
├── 07-functions-imports/
│   ├── lesson.md
│   └── solution.py         # No starter from Module 7 onward
├── 08-game-loop/
│   ├── lesson.md
│   ├── mini_project.py     # Exception — starter provided
│   └── solution.py
...
```

### 6.2 Lesson Markdown Format

Each `lesson.md` must have this Jekyll frontmatter and structure:

```markdown
---
title: "Módulo N — [Title]"
nav_order: N
layout: default
---

# Módulo N — [Title]

[Opening hook — 1-2 sentences connecting to the snake game or a relatable scenario]

## Lo que aprenderás

[Brief paragraph listing what the student will learn — NOT a bullet list]

## [Concept sections — use descriptive H2 headings]

[Follow the Motivate → Explain → Example → Connect pattern from Section 3.1]

## Errores comunes

[2-3 common mistakes as a brief discussion]

## Mini-proyecto: [Project name]

[Clear description of what the student will build]

[If Modules 1-6 or 8: mention the starter file and explain the TODOs]
[If Modules 7+: list the requirements the student's program must meet]

---

[Closing encouragement + teaser of next module]
```

### 6.3 Writing Rules for Lessons

- Use `##` for section headings. Avoid `###` unless truly nesting (keep hierarchy flat).
- Use fenced code blocks (` ```python `) for all code.
- Use blockquotes (`>`) for tips and callouts. Prefix with **💡 Tip:** or **⚠️ Cuidado:** as appropriate.
- Do NOT use bullet lists for explanatory prose. Write in paragraphs. Reserve lists only for sequential steps in the mini-project instructions.
- Keep paragraphs short — 3-5 sentences max.
- Every code snippet must be **runnable on its own** or clearly marked as a fragment with `# ...` for omitted context.

---

## 7. What NOT To Do

1. **Don't explain `keyboard.py` internals.** Students use it as a black box. Say "this module reads which key you pressed" and move on.
2. **Don't use type hints, f-strings, list comprehensions, classes, or any advanced Python.** Stick to the constructs in `main.py`.
3. **Don't introduce concepts out of syllabus order.** If Module 2 needs something from Module 3, restructure the example — don't "borrow forward."
4. **Don't show the complete `main.py` before Module 10.** Students should feel the satisfaction of assembling it themselves.
5. **Don't write English prose.** All lesson text, comments, and instructions are in Spanish. Only Python keywords, variable names, and string literals that appear in the original code stay in English.
6. **Don't make mini-project starters trivial.** A starter with 90% of the code filled in defeats the purpose. Aim for roughly 40–60% scaffolding in early modules, decreasing over time.
7. **Don't use `input()` extensively.** The course moves toward real-time keyboard input. `input()` is fine for Modules 1–5 mini-projects but should be treated as a temporary tool, not a core concept.

---

## 8. Generation Workflow

Write modules **one at a time, in order.** Before writing Module N:

1. Re-read the Module N section of `syllabus.md`.
2. Re-read the code progression entry for Module N (Section 5 above).
3. Review the previous module's lesson to ensure continuity — no repeated explanations, no gaps, natural transitions.
4. Write `lesson.md` first, then the starter file (if applicable), then `solution.py`.
5. Verify that `solution.py` is runnable and uses only concepts from Modules 1 through N.
6. Verify that the starter file is also runnable as-is (even if it does nothing useful).

---

## 9. Jekyll / GitHub Pages Notes

- The site uses the `just-the-docs` theme (configured in `_config.yml`).
- Navigation order is controlled by `nav_order` in frontmatter.
- The landing page is `index.md` at the repo root.
- Code files (`*.py`) inside module folders are for download, not rendered as pages. Only `lesson.md` files become pages.
- If you need to link to a downloadable file from the lesson, use a relative path: `[Descarga el archivo inicial](mini_project.py)`.
