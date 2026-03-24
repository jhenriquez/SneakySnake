# ============================================
# Mini-proyecto: Aventura de texto
# ============================================
# Una pequeña aventura donde el jugador explora
# habitaciones y necesita objetos para avanzar.

# Inventario del jugador
tiene_llave = False
tiene_antorcha = False

print("=== La Aventura de la Puerta Secreta ===")
print()
print("Estás en un pasillo oscuro. Hay tres caminos.")

while True:
    print()
    print("¿A dónde quieres ir?")
    print("  izquierda - Un cuarto pequeño")
    print("  derecha   - Un cuarto con algo brillante")
    print("  adelante  - Una puerta grande y misteriosa")
    print("  salir     - Terminar el juego")

    eleccion = input("Tu elección: ")

    if eleccion == "salir":
        print("Gracias por jugar. ¡Hasta luego!")
        break

    elif eleccion == "izquierda":
        print("Entras al cuarto pequeño.")
        # TODO: Si el jugador NO tiene la llave (usa "not"),
        # imprime "¡Encontraste una llave oxidada!" y cambia tiene_llave a True.
        # Si ya la tiene, imprime "El cuarto está vacío."


    elif eleccion == "derecha":
        print("Entras al cuarto brillante.")
        # TODO: Si el jugador NO tiene la antorcha (usa "not"),
        # imprime "¡Encontraste una antorcha encendida!" y cambia tiene_antorcha a True.
        # Si ya la tiene, imprime "El cuarto está vacío."


    elif eleccion == "adelante":
        print("Te acercas a la puerta grande.")
        # TODO: Si el jugador tiene la llave Y la antorcha (usa "and"),
        # imprime "¡La puerta se abre! Has escapado. ¡Felicidades!" y usa break.
        # Si solo tiene la llave (pero no la antorcha),
        # imprime "Tienes la llave, pero está muy oscuro para ver la cerradura."
        # Si solo tiene la antorcha (pero no la llave),
        # imprime "Puedes ver la cerradura, pero no tienes la llave."
        # Si no tiene ninguno,
        # imprime "La puerta está cerrada. Necesitas algo para abrirla..."


    else:
        print("No entiendo esa opción. Intenta de nuevo.")
