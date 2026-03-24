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
        # TODO: Completa las condiciones para decidir qué carácter agregar.
        #
        # 1. Si estamos en una esquina (primera o última fila Y primera o última columna):
        #    agrega "+"
        #
        # 2. Si estamos en el borde superior o inferior (primera o última fila):
        #    agrega "-"
        #
        # 3. Si estamos en el borde izquierdo o derecho (primera o última columna):
        #    agrega "|"
        #
        # 4. Si estamos en la posición del jugador (column == player_col y row == player_row):
        #    agrega "@"
        #
        # 5. Si estamos en la posición del objeto (column == item_col y row == item_row):
        #    agrega "*"
        #
        # 6. En cualquier otro caso:
        #    agrega " " (espacio)

        row_chars += " "  # Reemplaza esta línea con tus condiciones

    print(row_chars)
