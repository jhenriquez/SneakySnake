# ============================================
# Mini-proyecto: Escena estática
# ============================================
# Dibuja una cuadrícula de 40x15 con un jugador
# y un objeto en posiciones fijas.

# Tamaño de la cuadrícula
grid_width = 40
grid_height = 15

# Posición del jugador (centro)
player_col = 20
player_row = 7

# Posición del objeto
item_col = 10
item_row = 3

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
