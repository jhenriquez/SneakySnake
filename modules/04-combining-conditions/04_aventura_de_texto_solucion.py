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
        if not tiene_llave:
            print("¡Encontraste una llave oxidada!")
            tiene_llave = True
        else:
            print("El cuarto está vacío.")

    elif eleccion == "derecha":
        print("Entras al cuarto brillante.")
        if not tiene_antorcha:
            print("¡Encontraste una antorcha encendida!")
            tiene_antorcha = True
        else:
            print("El cuarto está vacío.")

    elif eleccion == "adelante":
        print("Te acercas a la puerta grande.")
        if tiene_llave and tiene_antorcha:
            print("¡La puerta se abre! Has escapado. ¡Felicidades!")
            break
        elif tiene_llave and not tiene_antorcha:
            print("Tienes la llave, pero está muy oscuro para ver la cerradura.")
        elif not tiene_llave and tiene_antorcha:
            print("Puedes ver la cerradura, pero no tienes la llave.")
        else:
            print("La puerta está cerrada. Necesitas algo para abrirla...")

    else:
        print("No entiendo esa opción. Intenta de nuevo.")
