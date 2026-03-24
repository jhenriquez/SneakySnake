# ============================================
# Juego de Snake completo
# ============================================
# Este es el resultado final del curso.
# La serpiente se mueve, come, crece, y el juego
# termina al chocar con las paredes o consigo misma.

import os
import time
import random
from keyboard import setup_keyboard, get_key_pressed

# Preparar el teclado y limpiar la pantalla
setup_keyboard()

os.system("cls" if os.name == "nt" else "clear")

# --- Configuración inicial ---
grid_width = 150
grid_height = 30
snake_head_col = grid_width // 2     # Columna central
snake_head_row = grid_height // 2    # Fila central
snake_tail = []                      # Lista de posiciones de la cola
snake_tail_length = 0                # La cola empieza vacía
player_name = "Player"
is_game_over = False
current_direction = "RIGHT"          # La serpiente empieza moviéndose a la derecha

# --- Generar la primera comida ---
# Buscamos una posición aleatoria que no coincida con la cabeza
while True:
    food_col = random.randint(1, grid_width - 2)
    food_row = random.randint(1, grid_height - 2)
    if (food_col, food_row) != (snake_head_col, snake_head_row):
        break
food_item = (food_col, food_row)

# --- Bucle del juego ---
while True:
    # 1. Entrada — leer tecla y cambiar dirección (sin permitir reversa)
    key = get_key_pressed()

    if key == "UP" and current_direction != "DOWN":
        current_direction = "UP"
    elif key == "DOWN" and current_direction != "UP":
        current_direction = "DOWN"
    elif key == "LEFT" and current_direction != "RIGHT":
        current_direction = "LEFT"
    elif key == "RIGHT" and current_direction != "LEFT":
        current_direction = "RIGHT"

    # 2. Actualización

    # Actualizar la cola (antes de mover la cabeza)
    if snake_tail_length > 0:
        snake_tail.append((snake_head_col, snake_head_row))
        snake_tail = snake_tail[-snake_tail_length:]

    # Mover la cabeza según la dirección actual
    if current_direction == "UP":
        snake_head_row -= 1
    elif current_direction == "DOWN":
        snake_head_row += 1
    elif current_direction == "LEFT":
        snake_head_col -= 1
    elif current_direction == "RIGHT":
        snake_head_col += 1

    # Verificar colisión con paredes y con la propia cola
    if (snake_head_row <= 0
            or snake_head_row >= grid_height - 1
            or snake_head_col <= 0
            or snake_head_col >= grid_width - 1
            or (snake_head_col, snake_head_row) in snake_tail):
        is_game_over = True

    # Verificar si la serpiente comió
    if (snake_head_col, snake_head_row) == food_item:
        snake_tail_length += 1
        # Generar nueva comida (no sobre la cabeza ni la cola)
        while True:
            food_col = random.randint(1, grid_width - 2)
            food_row = random.randint(1, grid_height - 2)
            if (food_col, food_row) not in snake_tail and (food_col, food_row) != (snake_head_col, snake_head_row):
                break
        food_item = (food_col, food_row)

    # 3. Dibujo
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
