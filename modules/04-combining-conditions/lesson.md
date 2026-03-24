---
title: "Módulo 4 — Combinando condiciones"
nav_order: 4
layout: default
---

# Módulo 4 — Combinando condiciones

En el módulo anterior aprendiste a repetir código con bucles. Y en el Módulo 2 aprendiste a tomar decisiones con `if`. Ahora vamos a combinar esas habilidades. En nuestro juego de Snake, cuando el jugador presiona "arriba", la serpiente solo debe cambiar de dirección si actualmente no va hacia abajo. Eso requiere verificar dos cosas al mismo tiempo — y para eso existen los operadores lógicos.

## Lo que aprenderás

En este módulo vas a aprender a usar `and`, `or` y `not` para combinar condiciones en una sola línea. También vas a practicar el uso de condiciones compuestas dentro de bucles, que es exactamente el patrón que usa el juego de Snake para procesar las teclas del jugador.

## El operador `and`

`and` combina dos condiciones y solo es `True` cuando **ambas** son verdaderas:

```python
edad = 16
tiene_permiso = True

if edad >= 13 and tiene_permiso:
    print("Puedes entrar al evento.")
else:
    print("No puedes entrar.")
```

Aquí, `edad >= 13` es `True` y `tiene_permiso` es `True`. Como ambas son verdaderas, `and` produce `True` y se ejecuta el primer `print()`.

Si cualquiera de las dos fuera `False`, el resultado sería `False`:

```python
edad = 10
tiene_permiso = True

if edad >= 13 and tiene_permiso:
    print("Puedes entrar.")
else:
    print("No puedes entrar.")  # Se ejecuta esta línea
```

Aunque `tiene_permiso` es `True`, `edad >= 13` es `False`, y `False and True` da `False`.

En nuestro juego de Snake, este patrón aparece cuando procesamos las teclas:

```python
if key == "UP" and current_direction != "DOWN":
    current_direction = "UP"
```

La serpiente solo cambia hacia arriba si el jugador presionó arriba **y** la serpiente no va hacia abajo. Esto evita que la serpiente se dé vuelta sobre sí misma y choque instantáneamente.

## El operador `or`

`or` combina dos condiciones y es `True` cuando **al menos una** es verdadera:

```python
dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("¡Es fin de semana!")
else:
    print("Es día de semana.")
```

Basta con que una de las dos comparaciones sea `True` para que todo sea `True`. Solo cuando ambas son `False`, el resultado es `False`.

```python
dia = "martes"

if dia == "sábado" or dia == "domingo":
    print("¡Es fin de semana!")
else:
    print("Es día de semana.")  # Se ejecuta esta línea
```

## El operador `not`

`not` invierte un valor booleano. Si algo es `True`, `not` lo convierte en `False`, y viceversa:

```python
esta_lloviendo = False

if not esta_lloviendo:
    print("¡Buen día para salir!")
```

`esta_lloviendo` es `False`, pero `not False` es `True`, así que el mensaje se muestra. Es como decir "si NO está lloviendo".

## Combinando varios operadores

Puedes usar `and`, `or` y `not` juntos en la misma condición. Python evalúa `not` primero, después `and`, y por último `or`:

```python
tiene_llave = True
tiene_antorcha = False
puerta_abierta = False

if (tiene_llave and tiene_antorcha) or puerta_abierta:
    print("Puedes pasar.")
else:
    print("No puedes pasar.")
```

Aquí, `tiene_llave and tiene_antorcha` es `False` (porque `tiene_antorcha` es `False`). Y `puerta_abierta` es `False`. Entonces `False or False` da `False`, y el personaje no puede pasar.

> **💡 Tip:** Cuando combinas `and` y `or`, usa paréntesis para dejar claro qué se evalúa primero. Aunque Python tiene reglas de prioridad, los paréntesis hacen el código más fácil de leer.

## Condiciones dentro de bucles

En la práctica, las condiciones compuestas aparecen constantemente dentro de bucles. Por ejemplo, un sistema de acceso que da tres intentos:

```python
intentos = 0
clave_correcta = "python123"

while intentos < 3:
    clave = input("Escribe la clave: ")
    if clave == clave_correcta:
        print("¡Acceso concedido!")
        break
    else:
        intentos = intentos + 1
        print("Clave incorrecta. Intentos restantes:", 3 - intentos)

if intentos == 3:
    print("Acceso bloqueado.")
```

Este ejemplo combina un bucle `while` con condiciones dentro. En cada vuelta del bucle, el programa decide si la clave es correcta. Si lo es, sale con `break`. Si no, suma un intento y sigue.

## Errores comunes

Un error frecuente es escribir `and` o `or` en inglés cuando Python espera exactamente esas palabras, pero intentar usar `&&` o `||` como en otros lenguajes. En Python siempre se escribe `and`, `or` y `not` como palabras completas.

Otro error es construir comparaciones incompletas. Si quieres verificar si `dia` es "sábado" o "domingo", necesitas escribir `dia == "sábado" or dia == "domingo"`. Escribir `dia == "sábado" or "domingo"` no funciona como esperas — Python lo interpreta de manera diferente y siempre da `True`.

Finalmente, cuidado con el orden de evaluación cuando mezclas `and` y `or` sin paréntesis. `True or False and False` da `True` porque `and` se evalúa antes que `or`. Usa paréntesis cuando no estés seguro.

## Mini-proyecto: Aventura de texto

Vas a crear una pequeña aventura de texto donde el jugador explora habitaciones y necesita cumplir condiciones para avanzar. El jugador tiene un inventario simple (variables booleanas) y las puertas requieren combinaciones de objetos.

El juego funciona así:

1. El jugador empieza sin objetos (`tiene_llave = False`, `tiene_antorcha = False`).
2. El programa describe una habitación y ofrece opciones (como "izquierda" o "derecha").
3. Según la elección, el jugador encuentra objetos o llega a puertas.
4. Para pasar por la puerta final, necesita la llave **y** la antorcha.
5. El juego termina cuando el jugador cruza la puerta final o decide salir.

[Descarga el archivo inicial](04_aventura_de_texto.py) — tiene la estructura del juego con el bucle principal y las variables de inventario ya creadas. Tu trabajo es completar las condiciones compuestas en cada decisión.

Cuando termines, compara tu resultado con la [solución completa](04_aventura_de_texto_solucion.py).

---

¡Ahora puedes hacer que tu programa verifique múltiples cosas al mismo tiempo! En el próximo módulo vamos a aprender sobre listas y tuplas — estructuras que nos permiten guardar muchos datos juntos, como todas las posiciones que ha visitado la serpiente.
