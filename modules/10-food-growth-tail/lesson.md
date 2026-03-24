---
title: "Módulo 10 — Comida, crecimiento y la cola"
nav_order: 10
layout: default
---

# Módulo 10 — Comida, crecimiento y la cola

Este es el momento que has estado esperando. Vas a agregar las últimas piezas que convierten tu programa en un juego de Snake completo: comida que aparece aleatoriamente, una cola que crece cuando comes, detección de colisión con tu propia cola, y un puntaje que sube con cada bocado. Al final de este módulo, habrás construido el juego completo desde cero.

## Lo que aprenderás

En este módulo vas a aprender a generar comida en posiciones válidas usando `while True` con `break`, a detectar cuando la serpiente come, a hacer crecer la cola usando listas y slicing negativo, a verificar colisión con la propia cola, y a mostrar el puntaje del jugador.

## Generando la comida

La comida es un `*` que aparece en una posición aleatoria. Pero no puede aparecer en cualquier lugar — necesita estar dentro de los bordes y no encima de la serpiente. Usamos un patrón que ya conoces, `while True` con `break`:

```python
import random

while True:
    food_col = random.randint(1, grid_width - 2)
    food_row = random.randint(1, grid_height - 2)
    if (food_col, food_row) != (snake_head_col, snake_head_row):
        break
food_item = (food_col, food_row)
```

Generamos una posición aleatoria y verificamos que no coincida con la cabeza de la serpiente. Si coincide, el bucle genera otra posición. Si no coincide, usamos `break` para salir. Finalmente, guardamos la posición como una tupla `food_item`.

Usamos `randint(1, grid_width - 2)` para que la comida caiga dentro de los bordes (columna 1 hasta columna `grid_width - 2`). Recuerda del Módulo 7 que `randint` incluye ambos extremos.

Este código va **antes** del bucle del juego, para colocar la primera comida al inicio de la partida.

## Detectando cuando la serpiente come

Dentro del bucle del juego, después de mover la cabeza, verificamos si está en la misma posición que la comida:

```python
if (snake_head_col, snake_head_row) == food_item:
    snake_tail_length += 1
```

Si la cabeza de la serpiente coincide con la posición de la comida, incrementamos el largo de la cola. Recuerda que `+=` es la forma corta de `snake_tail_length = snake_tail_length + 1`.

Después necesitamos generar nueva comida. Ahora la verificación es más completa — la comida no puede aparecer sobre la cabeza **ni** sobre la cola:

```python
    while True:
        food_col = random.randint(1, grid_width - 2)
        food_row = random.randint(1, grid_height - 2)
        if (food_col, food_row) not in snake_tail and (food_col, food_row) != (snake_head_col, snake_head_row):
            break
    food_item = (food_col, food_row)
```

Usamos `not in snake_tail` para verificar que la posición no esté en la lista de la cola, y `!=` para verificar que no sea la cabeza. Ambas condiciones deben ser verdaderas (unidas con `and`) para que la posición sea válida.

## La cola: una lista de posiciones

La cola de la serpiente es una lista de tuplas, donde cada tupla es una posición `(columna, fila)`. En cada cuadro del juego, antes de mover la cabeza, guardamos su posición actual en la lista:

```python
snake_tail = []           # Al inicio del programa
snake_tail_length = 0     # Empieza sin cola
```

Dentro del bucle, **antes** de mover la cabeza:

```python
if snake_tail_length > 0:
    snake_tail.append((snake_head_col, snake_head_row))
    snake_tail = snake_tail[-snake_tail_length:]
```

Primero verificamos que la cola tenga largo mayor a 0 (si no, no hay nada que guardar). Luego agregamos la posición actual de la cabeza a la lista con `append()`. Finalmente, recortamos la lista para mantener solo las últimas `snake_tail_length` posiciones usando slicing negativo (del Módulo 5).

¿Por qué hacemos esto **antes** de mover la cabeza? Porque queremos guardar dónde estaba la cabeza, no dónde va a estar. Así la cola sigue el camino que recorrió la cabeza.

> **💡 Tip:** Es importante que la actualización de la cola vaya **antes** del movimiento de la cabeza. Si lo pones después, la cola tendría la nueva posición de la cabeza en vez de la anterior, y se vería un espacio vacío entre la cabeza y la cola.

## Colisión con la propia cola

Además de chocar con las paredes, la serpiente también muere si choca consigo misma. Solo necesitamos agregar una condición más al bloque de colisión que ya teníamos:

```python
if (snake_head_row <= 0
        or snake_head_row >= grid_height - 1
        or snake_head_col <= 0
        or snake_head_col >= grid_width - 1
        or (snake_head_col, snake_head_row) in snake_tail):
    is_game_over = True
```

La nueva línea es `or (snake_head_col, snake_head_row) in snake_tail`. Verifica si la posición actual de la cabeza coincide con alguna posición en la lista de la cola. Si es así, la serpiente se mordió a sí misma.

## Mostrando el puntaje

Vamos a agregar dos líneas de información encima de la cuadrícula — el nombre del jugador y su puntaje:

```python
player_name = "Player"
```

Dentro del bucle, justo después de `print("\033[H", end="")`:

```python
print("Bienvenido,", player_name)
print("Tu puntaje actual es:", snake_tail_length * 5)
print()
```

Cada segmento de cola vale 5 puntos. Si la cola tiene 3 segmentos, el puntaje es `3 * 5 = 15`.

## Dibujando la cola en la cuadrícula

Necesitamos agregar una condición más a nuestro bloque de dibujo para mostrar los segmentos de la cola como `o`:

```python
elif column == snake_head_col and row == snake_head_row:
    row_chars += "@"
elif column == food_item[0] and row == food_item[1]:
    row_chars += "*"
# --- NUEVO ---
elif (column, row) in snake_tail:
    row_chars += "o"
else:
    row_chars += " "
```

La condición `(column, row) in snake_tail` verifica si la posición actual pertenece a la cola. Si es así, dibuja `o`.

Fíjate que también agregamos la comida al dibujo con `food_item[0]` (columna) y `food_item[1]` (fila). Accedemos a los valores de la tupla por índice, como aprendimos en el Módulo 5.

También agregamos un pequeño `time.sleep(0.001)` después de imprimir cada fila para evitar que la terminal se sature:

```python
    print(row_chars)
    time.sleep(0.001)
```

## Armando el programa completo

Ahora juntemos todo. Tu programa del Módulo 9 necesita estos cambios:

1. Agregar `import random` al inicio.
2. Agregar las variables `snake_tail = []`, `snake_tail_length = 0`, y `player_name = "Player"`.
3. Agregar el bloque de generación de comida antes del bucle del juego.
4. Dentro del bucle, agregar la actualización de la cola (antes del movimiento).
5. Agregar la detección de comida (después del movimiento).
6. Agregar la colisión con la cola (en el bloque de colisión existente).
7. Agregar las líneas de puntaje (en la sección de dibujo).
8. Agregar la cola y la comida al bloque de dibujo.

Son muchos cambios, pero cada uno es pequeño y usa conceptos que ya conoces. Tómate tu tiempo para agregar uno a la vez y probar después de cada cambio.

## Errores comunes

El error más común es poner la actualización de la cola en el lugar equivocado. La cola debe actualizarse **antes** de mover la cabeza. Si la actualizas después, la cabeza aparecerá duplicada en la lista y verás un comportamiento extraño.

Otro error frecuente es olvidar verificar `snake_tail_length > 0` antes de actualizar la cola. Si no verificas, el slicing `snake_tail[-0:]` devuelve la lista completa en vez de una lista vacía, y la cola crecerá sin control.

También cuidado al generar la nueva comida — si olvidas verificar que no caiga sobre la cola (`not in snake_tail`), la comida podría aparecer escondida debajo de un segmento de cola y ser invisible para el jugador.

## Mini-proyecto: Snake completo

Es hora de completar el juego. Toma tu programa del Módulo 9 y agrega:

1. Generación de comida en posición aleatoria válida.
2. Una cola que crece cuando la serpiente come.
3. Colisión con la propia cola.
4. Puntaje mostrado encima de la cuadrícula.
5. La comida (`*`) y la cola (`o`) dibujadas en la cuadrícula.

Este módulo no tiene archivo inicial. Construye sobre tu solución del Módulo 9. Recuerda que necesitas [keyboard.py](keyboard.py) en la misma carpeta.

Cuando termines, compara tu resultado con la [solución completa](10_snake_completo_solucion.py). Tu programa debe ser un juego de Snake completamente funcional.

¡Felicidades si llegaste hasta aquí! Has construido un juego completo desde cero, paso a paso, usando solo las herramientas fundamentales de Python.

---

¡Lo lograste! Tienes un juego de Snake completo y funcional. En el siguiente módulo (bonus) vas a explorar ideas para personalizar y mejorar tu juego — pero lo más importante ya está hecho. Construiste esto tú mismo, línea por línea.
