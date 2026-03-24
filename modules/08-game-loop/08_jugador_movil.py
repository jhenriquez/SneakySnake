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
    # 1. Entrada — leer qué tecla presionó el jugador
    key = get_key_pressed()

    # 2. Actualización — mover al jugador según la tecla
    # TODO: Si key es "UP", resta 1 a snake_head_row.
    # Si key es "DOWN", suma 1 a snake_head_row.
    # Si key es "LEFT", resta 1 a snake_head_col.
    # Si key es "RIGHT", suma 1 a snake_head_col.


    # 3. Dibujo — redibujar la cuadrícula
    print("\033[H", end="")

    for row in range(grid_height):
        row_chars = ""
        for column in range(grid_width):
            # TODO: Completa las condiciones para dibujar la cuadrícula.
            # Usa las mismas reglas del Módulo 6:
            # - Esquinas: "+"
            # - Bordes horizontales: "-"
            # - Bordes verticales: "|"
            # - Posición del jugador: "@"
            # - Todo lo demás: " "

            row_chars += " "  # Reemplaza esta línea con tus condiciones

        print(row_chars)

    # Controlar la velocidad del juego
    time.sleep(0.1)
