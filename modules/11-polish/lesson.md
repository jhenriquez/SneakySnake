---
title: "Módulo 11 — Pulir y personalizar"
nav_order: 11
layout: default
---

# Módulo 11 — Pulir y personalizar

¡Felicidades! Construiste un juego de Snake completo desde cero. Eso no es poca cosa — usaste variables, condiciones, bucles, listas, tuplas, funciones e importaciones para crear algo que realmente funciona. En este módulo bonus vas a explorar ideas para hacer tu juego más interesante y vas a hacer una lectura guiada del código completo como repaso final.

## Lo que aprenderás

En este módulo vas a ver tres ideas de extensión para tu juego (velocidad progresiva, puntaje máximo guardado en archivo, y comida múltiple) con bocetos de código que te dan la dirección sin darte todo resuelto. También vas a leer el programa completo de principio a fin como repaso de todos los conceptos del curso.

## Idea 1: Velocidad progresiva

El juego se siente igual de rápido cuando la serpiente tiene 1 segmento que cuando tiene 20. Sería más emocionante que el juego se acelere a medida que creces. La clave está en el `time.sleep()` al final del bucle — si reducimos el tiempo de espera, el juego va más rápido.

```python
# En vez de un valor fijo:
# time.sleep(0.1)

# Calcula la velocidad según el largo de la cola:
speed = 0.1 - (snake_tail_length * 0.002)
if speed < 0.03:
    speed = 0.03
time.sleep(speed)
```

La idea es simple: empezamos con `0.1` segundos y restamos un poquito por cada segmento de cola. El `if` evita que la velocidad baje de `0.03` — sin ese límite, el juego eventualmente iría tan rápido que sería imposible de jugar. Experimenta con los números (`0.002` y `0.03`) para encontrar el equilibrio que más te guste.

## Idea 2: Puntaje máximo con archivo

¿No sería genial que el juego recuerde tu mejor puntaje entre partidas? Para eso necesitas guardar el puntaje en un archivo y leerlo cuando el juego empieza.

Para leer un archivo:

```python
# Intentar leer el puntaje máximo guardado
high_score = 0
try:
    archivo = open("high_score.txt", "r")
    high_score = int(archivo.read())
    archivo.close()
except:
    high_score = 0
```

No te preocupes si no entiendes `try` y `except` — por ahora solo necesitas saber que este bloque intenta leer el archivo, y si el archivo no existe (primera vez que juegas), simplemente pone el puntaje en 0.

Para guardar el puntaje cuando termina el juego:

```python
if is_game_over:
    score = snake_tail_length * 5
    if score > high_score:
        archivo = open("high_score.txt", "w")
        archivo.write(str(score))
        archivo.close()
        print("¡Nuevo récord!", score)
    else:
        print("Récord actual:", high_score)
    print("Game over")
    break
```

`open("high_score.txt", "w")` abre (o crea) un archivo para escritura. `archivo.write(str(score))` guarda el puntaje como texto. `archivo.close()` cierra el archivo.

Para mostrar el récord durante el juego, reemplaza la línea del puntaje:

```python
print("Tu puntaje actual es:", snake_tail_length * 5, "  Récord:", high_score)
```

## Idea 3: Comida múltiple

En vez de una sola comida en pantalla, ¿qué tal tener varias? Necesitarías una lista de comidas en vez de una sola tupla:

```python
# En vez de food_item = (food_col, food_row)
food_items = []

# Generar 3 comidas iniciales
for i in range(3):
    while True:
        food_col = random.randint(1, grid_width - 2)
        food_row = random.randint(1, grid_height - 2)
        if (food_col, food_row) != (snake_head_col, snake_head_row):
            break
    food_items.append((food_col, food_row))
```

Para la detección de comida, tendrías que recorrer la lista:

```python
for food in food_items:
    if (snake_head_col, snake_head_row) == food:
        snake_tail_length += 1
        food_items.remove(food)
        # Generar nueva comida de reemplazo...
        break
```

Y en el dibujo, verificar si la posición actual está en la lista:

```python
elif (column, row) in food_items:
    row_chars += "*"
```

Estos son solo bocetos para que tengas la idea general. El reto es que los implementes y ajustes por tu cuenta.

## Lectura guiada del código completo

Ahora vamos a leer el programa completo de principio a fin. Esta es una oportunidad para repasar cada concepto que aprendiste y ver cómo todos encajan juntos.

```python
import os
import time
import random
from keyboard import setup_keyboard, get_key_pressed
```

Estas son las **importaciones** (Módulo 7). Traemos cuatro módulos: `os` para limpiar la pantalla, `time` para controlar la velocidad, `random` para la comida aleatoria, y `keyboard` para leer las teclas.

```python
setup_keyboard()

os.system("cls" if os.name == "nt" else "clear")
```

Preparamos el teclado para lectura en tiempo real (Módulo 8) y limpiamos la pantalla.

```python
grid_width = 150
grid_height = 30
snake_head_col = grid_width // 2
snake_head_row = grid_height // 2
snake_tail = []
snake_tail_length = 0
player_name = "Player"
is_game_over = False
current_direction = "RIGHT"
```

**Variables iniciales** (Módulos 1, 2 y 5). Definimos el tamaño de la cuadrícula, la posición de la cabeza usando división entera, una lista vacía para la cola, y las banderas de estado del juego.

```python
while True:
    food_col = random.randint(1, grid_width - 2)
    food_row = random.randint(1, grid_height - 2)
    if (food_col, food_row) != (snake_head_col, snake_head_row):
        break
food_item = (food_col, food_row)
```

**Generación de comida** (Módulos 3 y 7). Un bucle `while True` con `break` que genera posiciones aleatorias hasta encontrar una válida. El resultado se guarda en una tupla (Módulo 5).

```python
while True:
    key = get_key_pressed()
```

**El bucle del juego** (Módulo 8). Todo lo que sigue se repite muchas veces por segundo.

```python
    if key == "UP" and current_direction != "DOWN":
        current_direction = "UP"
    elif key == "DOWN" and current_direction != "UP":
        current_direction = "DOWN"
    elif key == "LEFT" and current_direction != "RIGHT":
        current_direction = "LEFT"
    elif key == "RIGHT" and current_direction != "LEFT":
        current_direction = "RIGHT"
```

**Entrada con prevención de reversa** (Módulos 4 y 9). Cada condición usa `and` para verificar que la nueva dirección no sea la opuesta a la actual.

```python
    if snake_tail_length > 0:
        snake_tail.append((snake_head_col, snake_head_row))
        snake_tail = snake_tail[-snake_tail_length:]
```

**Actualización de la cola** (Módulos 5 y 10). Guardamos la posición actual de la cabeza y recortamos la lista al largo correcto usando slicing negativo.

```python
    if current_direction == "UP":
        snake_head_row -= 1
    elif current_direction == "DOWN":
        snake_head_row += 1
    elif current_direction == "LEFT":
        snake_head_col -= 1
    elif current_direction == "RIGHT":
        snake_head_col += 1
```

**Movimiento** (Módulos 2 y 9). La cabeza se mueve según `current_direction`, no según la tecla presionada.

```python
    if (snake_head_row <= 0
            or snake_head_row >= grid_height - 1
            or snake_head_col <= 0
            or snake_head_col >= grid_width - 1
            or (snake_head_col, snake_head_row) in snake_tail):
        is_game_over = True
```

**Detección de colisiones** (Módulos 4, 5 y 9). Verifica paredes con comparaciones y cola con `in`.

```python
    if (snake_head_col, snake_head_row) == food_item:
        snake_tail_length += 1
        while True:
            food_col = random.randint(1, grid_width - 2)
            food_row = random.randint(1, grid_height - 2)
            if (food_col, food_row) not in snake_tail and (food_col, food_row) != (snake_head_col, snake_head_row):
                break
        food_item = (food_col, food_row)
```

**Comida y crecimiento** (Módulo 10). Si la cabeza está en la misma posición que la comida, la cola crece y se genera nueva comida.

```python
    print("\033[H", end="")
    print("Bienvenido,", player_name)
    print("Tu puntaje actual es:", snake_tail_length * 5)
    print()

    for row in range(grid_height):
        row_chars = ""
        for column in range(grid_width):
            # ... condiciones de dibujo ...
        print(row_chars)
        time.sleep(0.001)
```

**Dibujo de la cuadrícula** (Módulos 1, 6 y 8). Bucles anidados que construyen cada fila carácter por carácter y la imprimen.

```python
    if is_game_over:
        print("Game over")
        break

    time.sleep(0.1)
```

**Fin del juego** (Módulo 9). Si `is_game_over` es `True`, mostramos el mensaje y salimos del bucle con `break`.

## ¿Qué sigue?

Has completado el curso. Ahora sabes:

- Mostrar información con `print()` y guardarla en variables.
- Hacer cálculos y tomar decisiones con `if`.
- Repetir acciones con `while` y `for`.
- Combinar condiciones con `and`, `or` y `not`.
- Organizar datos con listas y tuplas.
- Dibujar en la terminal con bucles anidados.
- Usar módulos como `random`, `time` y `os`.
- Construir un bucle de juego con entrada en tiempo real.
- Manejar estado, reglas y colisiones.

Todo eso partiendo de cero. El juego de Snake es tuyo — modifícalo, rómpelo, reconstruyelo. Cada cambio que hagas te enseñará algo nuevo. Si quieres seguir aprendiendo Python, busca proyectos que te emocionen — esa es la mejor manera de crecer como programador.

¡Gracias por completar SneakySnake!
