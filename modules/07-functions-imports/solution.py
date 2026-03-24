# ============================================
# Mini-proyecto: Escena aleatoria
# ============================================
# La cuadrícula del Módulo 6, pero ahora el objeto
# aparece en una posición aleatoria cada vez.

import random
import time

# Tamaño de la cuadrícula
grid_width = 40
grid_height = 15

# El jugador empieza en el centro
player_col = grid_width // 2
player_row = grid_height // 2

# El objeto aparece en una posición aleatoria dentro de los bordes
item_col = random.randint(1, grid_width - 2)
item_row = random.randint(1, grid_height - 2)

# Dibujar la cuadrícula
for row in range(grid_height):
    row_chars = ""
    for column in range(grid_width):
        if (row == 0 or row == grid_height - 1) and (column == 0 or column == grid_width - 1):
            row_chars += "+"
        elif row == 0 or row == grid_height - 1:
            row_chars += "-"
        elif column == 0 or column == grid_width - 1:
            row_chars += "|"
        elif column == player_col and row == player_row:
            row_chars += "@"
        elif column == item_col and row == item_row:
            row_chars += "*"
        else:
            row_chars += " "
    print(row_chars)

# Pausa para que se pueda ver el resultado
time.sleep(3)
