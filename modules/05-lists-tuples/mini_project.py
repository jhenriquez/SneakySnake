# ============================================
# Mini-proyecto: Rastreador de posiciones
# ============================================
# El jugador se mueve en una línea (izquierda/derecha)
# y el programa recuerda todas las posiciones visitadas.

# Posición inicial
position = 5

# TODO: Crea una lista vacía llamada "visited" para guardar las posiciones visitadas.


# TODO: Agrega la posición inicial a la lista "visited" usando append().


print("=== Rastreador de posiciones ===")
print("Posición inicial:", position)
print("Escribe 'izquierda', 'derecha' o 'salir'.")

while True:
    print()
    move = input("Movimiento: ")

    if move == "salir":
        print("¡Adiós!")
        break

    # TODO: Si move es "izquierda", resta 1 a position.
    # Si move es "derecha", suma 1 a position.
    # Si no es ninguna de las dos, imprime "Movimiento no válido." y usa "continue"
    # para saltar al siguiente turno.
    # (Nota: "continue" salta al inicio del bucle, como un break que no sale)


    # TODO: Agrega la nueva posición a la lista "visited".


    # TODO: Imprime "Posición actual:" seguido de position.


    # TODO: Imprime "Posiciones visitadas:" seguido de visited.

