import os
import time
import random
from keyboard import setup_keyboard, get_key_pressed

setup_keyboard()

os.system("cls" if os.name == "nt" else "clear")

grid_width = 150
grid_height = 30
snake_head_col = grid_width // 2
snake_head_row = grid_height // 2
snake_tail = []
snake_tail_length = 0
player_name = "Player"
is_game_over = False
current_direction = "RIGHT"

# Place first food item
while True:
    food_col = random.randint(1, grid_width - 2)
    food_row = random.randint(1, grid_height - 2)
    if (food_col, food_row) != (snake_head_col, snake_head_row):
        break
food_item = (food_col, food_row)

while True:
    key = get_key_pressed()

    if key == "UP" and current_direction != "DOWN":
        current_direction = "UP"
    elif key == "DOWN" and current_direction != "UP":
        current_direction = "DOWN"
    elif key == "LEFT" and current_direction != "RIGHT":
        current_direction = "LEFT"
    elif key == "RIGHT" and current_direction != "LEFT":
        current_direction = "RIGHT"

    # --- Update tail ---
    if snake_tail_length > 0:
        snake_tail.append((snake_head_col, snake_head_row))
        snake_tail = snake_tail[-snake_tail_length:]

    # --- Move head ---
    if current_direction == "UP":
        snake_head_row -= 1
    elif current_direction == "DOWN":
        snake_head_row += 1
    elif current_direction == "LEFT":
        snake_head_col -= 1
    elif current_direction == "RIGHT":
        snake_head_col += 1

    # --- Collision check ---
    if (snake_head_row <= 0
            or snake_head_row >= grid_height - 1
            or snake_head_col <= 0
            or snake_head_col >= grid_width - 1
            or (snake_head_col, snake_head_row) in snake_tail):
        is_game_over = True

    # --- Food check ---
    if (snake_head_col, snake_head_row) == food_item:
        snake_tail_length += 1
        while True:
            food_col = random.randint(1, grid_width - 2)
            food_row = random.randint(1, grid_height - 2)
            if (food_col, food_row) not in snake_tail and (food_col, food_row) != (snake_head_col, snake_head_row):
                break
        food_item = (food_col, food_row)

    # --- Render ---
    print("\033[H", end="")
    print("Bienvenido,", player_name)
    print("Tu puntaje actual es:", snake_tail_length * 5)
    print()

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
            elif (column, row) in snake_tail:
                row_chars += "o"
            else:
                row_chars += " "
        print(row_chars)
        time.sleep(0.001)

    if is_game_over:
        print("Game over")
        break

    time.sleep(0.1)
