---
title: "Módulo 8 — Entrada en tiempo real y el bucle del juego"
nav_order: 8
layout: default
---

# Módulo 8 — Entrada en tiempo real y el bucle del juego

Este es el módulo donde todo cambia. Hasta ahora, tus programas esperaban a que el jugador escribiera algo y presionara Enter. Pero un juego de Snake no funciona así — la serpiente se mueve constantemente y el jugador la controla con las flechas del teclado sin necesidad de presionar Enter. En este módulo vas a combinar todo lo que has aprendido para hacer que un `@` se mueva en la pantalla en tiempo real.

## Lo que aprenderás

En este módulo vas a aprender cómo funciona un bucle de juego (el ciclo de entrada → actualización → dibujo que se repite muchas veces por segundo). Vas a usar el módulo `keyboard` que te proporcionamos para leer las teclas de flecha, y vas a aprender a redibujar la pantalla rápidamente para crear la ilusión de movimiento.

## El concepto del bucle de juego

Todos los videojuegos — desde Snake hasta los juegos más complejos — funcionan con el mismo patrón básico. Se llama el **bucle del juego** (*game loop*) y tiene tres pasos que se repiten sin parar:

1. **Entrada** — ¿Qué tecla presionó el jugador?
2. **Actualización** — Mover la serpiente, verificar colisiones, actualizar el puntaje.
3. **Dibujo** — Redibujar la pantalla con las posiciones nuevas.

Estos tres pasos se repiten muchas veces por segundo. Cada repetición es un **cuadro** (*frame*), como los cuadros de una película. Si el bucle se repite 10 veces por segundo, el jugador ve 10 actualizaciones de la pantalla por segundo, que es suficiente para que el movimiento se vea fluido.

En código, el bucle del juego se ve así:

```python
while True:
    # 1. Entrada
    key = get_key_pressed()

    # 2. Actualización
    # ... mover al jugador según la tecla ...

    # 3. Dibujo
    # ... dibujar la cuadrícula ...

    time.sleep(0.1)
```

El `time.sleep(0.1)` al final controla la velocidad — espera 0.1 segundos (una décima) entre cada cuadro.

## El módulo `keyboard`

Para leer las teclas de flecha sin que el jugador tenga que presionar Enter, vamos a usar un módulo especial llamado `keyboard`. Este módulo te lo proporcionamos ya hecho — no necesitas escribirlo ni entender cómo funciona por dentro. Solo necesitas saber cómo usarlo.

Primero, descarga el archivo `keyboard.py` y ponlo en la misma carpeta que tu programa. Después, importa y prepara el teclado al inicio de tu archivo:

```python
from keyboard import setup_keyboard, get_key_pressed

setup_keyboard()
```

`setup_keyboard()` prepara la terminal para poder leer teclas individuales. Solo necesitas llamarla una vez, al inicio del programa.

Después, dentro del bucle del juego, usas `get_key_pressed()` para saber qué tecla presionó el jugador:

```python
key = get_key_pressed()
```

Esta función devuelve `"UP"`, `"DOWN"`, `"LEFT"`, `"RIGHT"`, o `None` (si no se presionó ninguna tecla de flecha). Puedes usar `if` para decidir qué hacer con cada tecla.

> **⚠️ Cuidado:** El archivo `keyboard.py` debe estar en la misma carpeta que tu programa. Si Python no lo encuentra, verás un error `ModuleNotFoundError`.

## Moviendo al jugador

Ahora que podemos leer teclas, mover al jugador es simple. Si presiona arriba, restamos 1 a la fila. Si presiona abajo, sumamos 1. Izquierda resta 1 a la columna, derecha suma 1:

```python
if key == "UP":
    snake_head_row = snake_head_row - 1
elif key == "DOWN":
    snake_head_row = snake_head_row + 1
elif key == "LEFT":
    snake_head_col = snake_head_col - 1
elif key == "RIGHT":
    snake_head_col = snake_head_col + 1
```

Fíjate que arriba **resta** a la fila, no suma. Esto es porque en la terminal, la fila 0 está arriba y los números crecen hacia abajo. Entonces "mover hacia arriba" significa ir a una fila con número más pequeño.

## Redibujando la pantalla

En el Módulo 6 dibujaste la cuadrícula una vez. Ahora necesitas redibujarla muchas veces por segundo para mostrar la nueva posición del jugador. Pero si simplemente imprimes la cuadrícula de nuevo, cada cuadro aparece debajo del anterior y la pantalla se llena de texto.

La solución es mover el cursor de la terminal al inicio de la pantalla antes de dibujar. Para eso usamos un código especial:

```python
print("\033[H", end="")
```

`"\033[H"` es una secuencia especial que le dice a la terminal "mueve el cursor a la esquina superior izquierda". El `end=""` evita que `print()` agregue un salto de línea extra. Al imprimir la cuadrícula encima de la anterior, se crea la ilusión de movimiento.

También usamos `os.system("clear")` (o `"cls"` en Windows) una sola vez al inicio para limpiar cualquier texto previo:

```python
import os
os.system("cls" if os.name == "nt" else "clear")
```

## El programa completo

Aquí tienes la estructura completa del programa, paso a paso:

```python
import os
import time
from keyboard import setup_keyboard, get_key_pressed

# Preparar el teclado y limpiar la pantalla
setup_keyboard()
os.system("cls" if os.name == "nt" else "clear")

# Configuración
grid_width = 150
grid_height = 30
snake_head_col = grid_width // 2
snake_head_row = grid_height // 2
```

Estas son las variables de configuración. La cuadrícula es de 150 columnas por 30 filas (el tamaño real del juego), y el jugador empieza en el centro.

```python
# Bucle del juego
while True:
    # 1. Entrada
    key = get_key_pressed()

    # 2. Actualización
    if key == "UP":
        snake_head_row -= 1
    elif key == "DOWN":
        snake_head_row += 1
    elif key == "LEFT":
        snake_head_col -= 1
    elif key == "RIGHT":
        snake_head_col += 1
```

> **💡 Tip:** `snake_head_row -= 1` es lo mismo que `snake_head_row = snake_head_row - 1`. Es una forma más corta que vas a ver con frecuencia.

```python
    # 3. Dibujo
    print("\033[H", end="")

    for row in range(grid_height):
        row_chars = ""
        for column in range(grid_width):
            if (row == 0 or row == grid_height - 1) and (column == 0 or column == grid_width - 1):
                row_chars += "+"
            elif row == 0 or row == grid_height - 1:
                row_chars += "-"
            elif column == 0 or column == grid_width - 1:
                row_chars += "|"
            elif column == snake_head_col and row == snake_head_row:
                row_chars += "@"
            else:
                row_chars += " "
        print(row_chars)

    time.sleep(0.1)
```

La sección de dibujo es casi idéntica a la del Módulo 6, pero ahora está dentro del bucle y usa `"\033[H"` para redibujar en el mismo lugar.

Cuando ejecutes este programa, verás la cuadrícula y podrás mover el `@` con las flechas. ¡Es tu primer programa interactivo en tiempo real!

## Errores comunes

El error más peligroso es olvidar el `time.sleep()` al final del bucle. Sin esa pausa, el programa intentaría redibujar la pantalla miles de veces por segundo, lo que haría que la terminal se congele o muestre texto ilegible. Siempre incluye `time.sleep(0.1)` como última línea dentro del bucle.

Otro error común es olvidar `setup_keyboard()` al inicio. Si no lo llamas, `get_key_pressed()` no podrá leer las teclas correctamente y siempre devolverá `None`.

Si el `@` deja un rastro o la pantalla se ve desordenada, verifica que tienes `print("\033[H", end="")` antes de dibujar la cuadrícula. Sin esa línea, cada cuadro se dibuja debajo del anterior en vez de encima.

## Mini-proyecto: Jugador móvil

Vas a crear un programa donde el `@` se mueve libremente en una cuadrícula de 150×30 usando las flechas del teclado. No hay comida, no hay cola, no hay colisiones — solo un personaje que se mueve. Este es el primer momento donde tu programa se siente como un juego.

Tu programa debe:

1. Importar `os`, `time`, y las funciones de `keyboard`.
2. Llamar a `setup_keyboard()` y limpiar la pantalla.
3. Definir la cuadrícula de 150×30 y colocar el `@` en el centro.
4. En un bucle `while True`:
   - Leer la tecla presionada.
   - Mover al jugador según la tecla.
   - Redibujar la cuadrícula con `"\033[H"`.
   - Esperar 0.1 segundos.

[Descarga el archivo inicial](mini_project.py) — tiene los imports, el `setup_keyboard()`, y la estructura del bucle ya preparados. También necesitas descargar [keyboard.py](keyboard.py) y ponerlo en la misma carpeta.

Cuando termines, compara tu resultado con la [solución completa](solution.py).

---

¡Increíble! Tu `@` se mueve por la pantalla en tiempo real. Esto ya es un juego. Pero todavía puede atravesar las paredes y no tiene dirección propia. En el próximo módulo vamos a agregar las reglas: la serpiente se moverá sola en una dirección, las flechas solo cambiarán esa dirección, y chocar con una pared terminará la partida.
