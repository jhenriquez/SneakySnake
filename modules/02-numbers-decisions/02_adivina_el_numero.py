# ============================================
# Mini-proyecto: Adivina el número
# ============================================
# El programa elige un número secreto y el jugador
# intenta adivinarlo. El programa dice si el intento
# es muy alto, muy bajo o correcto.

# El número secreto (cámbialo si quieres)
secret_number = 42

print("¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 100.")

# Este bucle repite el juego hasta que el jugador adivine.
# Vamos a aprender cómo funciona en el Módulo 3.
# Por ahora solo necesitas saber que todo lo que está
# dentro del bucle se repite, y "break" lo detiene.
while True:
    # Esta línea pide al jugador que escriba un número.
    # int() convierte el texto a número para poder comparar.
    guess = int(input("Tu intento: "))

    # TODO: Compara "guess" con "secret_number".
    # Si guess es mayor que secret_number, imprime "Muy alto".
    # Si guess es menor que secret_number, imprime "Muy bajo".
    # Si son iguales, imprime "¡Correcto! Adivinaste." y usa "break" para terminar.

