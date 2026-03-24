# ============================================
# Mini-proyecto: Adivina el número
# ============================================
# El programa elige un número secreto y el jugador
# intenta adivinarlo. El programa dice si el intento
# es muy alto, muy bajo o correcto.

# El número secreto
secret_number = 42

print("¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 100.")

while True:
    guess = int(input("Tu intento: "))

    if guess > secret_number:
        print("Muy alto.")
    elif guess < secret_number:
        print("Muy bajo.")
    else:
        print("¡Correcto! Adivinaste.")
        break
