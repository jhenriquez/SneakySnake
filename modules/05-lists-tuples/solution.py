# ============================================
# Mini-proyecto: Rastreador de posiciones
# ============================================
# El jugador se mueve en una línea (izquierda/derecha)
# y el programa recuerda todas las posiciones visitadas.

# Posición inicial
position = 5

# Lista de posiciones visitadas
visited = []
visited.append(position)

print("=== Rastreador de posiciones ===")
print("Posición inicial:", position)
print("Escribe 'izquierda', 'derecha' o 'salir'.")

while True:
    print()
    move = input("Movimiento: ")

    if move == "salir":
        print("¡Adiós!")
        break

    if move == "izquierda":
        position = position - 1
    elif move == "derecha":
        position = position + 1
    else:
        print("Movimiento no válido.")
        continue

    visited.append(position)

    print("Posición actual:", position)
    print("Posiciones visitadas:", visited)
