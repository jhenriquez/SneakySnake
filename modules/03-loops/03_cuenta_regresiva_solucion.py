# ============================================
# Mini-proyecto: Cuenta regresiva
# ============================================
# Este programa cuenta del 10 al 0 y luego
# muestra "¡Despegue!". Hay dos versiones:
# una con while y otra con for.

# ----- Versión 1: con while -----
print("--- Cuenta regresiva con while ---")

numero = 10

while numero >= 0:
    print(numero)
    numero = numero - 1

print("¡Despegue!")

print()  # Línea en blanco para separar las dos versiones

# ----- Versión 2: con for -----
print("--- Cuenta regresiva con for ---")

for numero in range(10, -1, -1):
    print(numero)

print("¡Despegue!")
