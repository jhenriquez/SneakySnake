# ============================================
# Mini-proyecto: Jugador móvil
# ============================================
# Un "@" que se mueve libremente en una cuadrícula
# usando las flechas del teclado.

import os
import time
from keyboard import setup_keyboard, get_key_pressed

# Preparar el teclado y limpiar la pantalla
setup_keyboard()
os.system("cls" if os.name == "nt" else "clear")

# Configuración de la cuadrícula
grid_width = 150
grid_height = 30

# Posición inicial del jugador (centro de la cuadrícula)
snake_head_col = grid_width // 2
snake_head_row = grid_height // 2

# Bucle del juego
while True:
    # 1. Entrada
    key = get_key_pressed()

    # 2. Actualización
    if key == "UP":
        snake_head_row -= 1
    elif key == "DOWN":
        snake_head_row += 1
    elif key == "LEFT":
        snake_head_col -= 1
    elif key == "RIGHT":
        snake_head_col += 1

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

    time.sleep(0.1)
