# ============================================
# Mini-proyecto: Snake sin cola
# ============================================
# La serpiente se mueve sola, cambia de dirección
# con las flechas (sin reversa), y muere al tocar
# las paredes.

import os
import time
from keyboard import setup_keyboard, get_key_pressed

# Preparar el teclado y limpiar la pantalla
setup_keyboard()
os.system("cls" if os.name == "nt" else "clear")

# Configuración
grid_width = 150
grid_height = 30
snake_head_col = grid_width // 2
snake_head_row = grid_height // 2
is_game_over = False
current_direction = "RIGHT"

# Bucle del juego
while True:
    # 1. Entrada — cambiar dirección (con prevención de reversa)
    key = get_key_pressed()

    if key == "UP" and current_direction != "DOWN":
        current_direction = "UP"
    elif key == "DOWN" and current_direction != "UP":
        current_direction = "DOWN"
    elif key == "LEFT" and current_direction != "RIGHT":
        current_direction = "LEFT"
    elif key == "RIGHT" and current_direction != "LEFT":
        current_direction = "RIGHT"

    # 2. Actualización — mover la cabeza
    if current_direction == "UP":
        snake_head_row -= 1
    elif current_direction == "DOWN":
        snake_head_row += 1
    elif current_direction == "LEFT":
        snake_head_col -= 1
    elif current_direction == "RIGHT":
        snake_head_col += 1

    # Verificar colisión con paredes
    if (snake_head_row <= 0
            or snake_head_row >= grid_height - 1
            or snake_head_col <= 0
            or snake_head_col >= grid_width - 1):
        is_game_over = True

    # 3. Dibujo
    print("\033[H", end="")

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
            else:
                row_chars += " "
        print(row_chars)

    if is_game_over:
        print("Game over")
        break

    time.sleep(0.1)
