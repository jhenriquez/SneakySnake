# Build Your Own Snake Game with Python

## Course Syllabus

A hands-on introductory programming course designed for absolute beginners (ages 13+). Students progressively learn Python fundamentals by building toward a fully functional Snake game as the final project.

> **Prerequisites:** None. No prior coding experience required.
>
> **Final deliverable:** A complete, playable Snake game written in Python (`main.py`).
>
> **Note:** The `keyboard.py` module is provided pre-made. Students focus exclusively on building `main.py`.

---

## Module 1 — Hello, Python!

**Concepts covered:**

- What is programming / what is Python
- Running your first script
- `print()` — displaying text on screen
- Strings and string concatenation
- Variables — storing text and numbers

**Mini-project:** A personalized greeting program ("Bienvenido, [name]")

---

## Module 2 — Numbers & Decisions

**Concepts covered:**

- Integer variables and basic arithmetic (`+`, `-`, `*`, `//`)
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- `if`, `elif`, `else` — making your program choose
- Booleans (`True` / `False`)

**Mini-project:** A number guessing game (random number, player types guesses, program says higher/lower)

---

## Module 3 — Loops

**Concepts covered:**

- `while True` and the infinite loop
- `break` — escaping a loop
- Counters and updating variables inside loops
- `for` loop and `range()`

**Mini-project:** A countdown timer that prints numbers to zero, then says "Blast off!"

---

## Module 4 — Combining Conditions

**Concepts covered:**

- Logical operators: `and`, `or`, `not`
- Compound conditions in `if` statements
- Nested `if` inside loops

**Mini-project:** A simple text-based adventure with multi-condition gates ("You have the key AND the torch, so the door opens…")

---

## Module 5 — Lists & Tuples

**Concepts covered:**

- Lists — creating, appending, reading by index
- List slicing (including negative slicing)
- The `in` operator — checking membership
- Tuples — what they are and how they differ from lists
- Coordinates as tuples `(x, y)`

**Mini-project:** A trail tracker — the player moves on a 1D line and the program remembers every position visited

---

## Module 6 — Nested Loops & the Grid

**Concepts covered:**

- Nested `for` loops — rows inside columns
- Building a 2D grid out of characters
- Printing a bordered rectangle with `+`, `-`, `|`
- Placing a character at a specific `(col, row)` position on the grid

**Mini-project:** A static scene renderer — draw a bordered grid with a `@` player and a `*` item at hardcoded positions

---

## Module 7 — Functions & Imports

**Concepts covered:**

- What is a function and why we use them
- Calling functions (arguments, return values)
- `import` — using code other people wrote
- `random.randint()` — generating random numbers
- `time.sleep()` — pausing the program
- `from module import function` syntax

**Mini-project:** Randomized scene — each run places the `*` item at a different grid position

---

## Module 8 — Real-Time Input & the Game Loop

**Concepts covered:**

- The concept of a game loop (input → update → render → repeat)
- Using the provided `keyboard` module (`setup_keyboard`, `get_key_pressed`)
- Moving a character on screen with arrow keys
- Clearing / redrawing the screen (`\033[H` cursor reset)
- Controlling speed with `time.sleep()`

**Mini-project:** A freely moving `@` on a bordered grid, controlled with arrow keys

---

## Module 9 — Game Rules & State

**Concepts covered:**

- Direction state — storing and updating `current_direction`
- Preventing reverse direction (the `and current_direction != …` pattern)
- Wall collision detection using boundary checks
- Setting a game-over flag and breaking the loop

**Mini-project:** An auto-moving dot that bounces or dies when it hits a wall

---

## Module 10 — Food, Growth & the Tail

**Concepts covered:**

- Spawning food at a valid random position (the `while True` / `break` spawn pattern)
- Detecting food collision and incrementing score
- Growing the tail — appending positions to a list, slicing to length
- Self-collision — checking `in snake_tail`
- Displaying score

**Final project:** The complete Snake game

---

## Module 11 — Polish & Make It Yours (Bonus)

**Ideas for extensions:**

- Speed increase as the snake grows
- High score tracking
- Multiple food items
- Obstacles and levels

**Recap exercise:** Read and understand the full `main.py` code top-to-bottom as a review of every concept learned throughout the course.
