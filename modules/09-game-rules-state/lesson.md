---
title: "Módulo 9 — Reglas del juego y estado"
nav_order: 9
layout: default
---

# Módulo 9 — Reglas del juego y estado

En el módulo anterior, tu `@` se movía libremente por la pantalla. Pero Snake no funciona así — la serpiente se mueve sola en una dirección constante, las flechas solo cambian esa dirección, no puedes darte vuelta sobre ti mismo, y chocar con las paredes termina el juego. En este módulo vamos a agregar todas esas reglas.

## Lo que aprenderás

En este módulo vas a aprender a manejar el estado de dirección de la serpiente, a prevenir que cambie a la dirección opuesta (lo que causaría una colisión instantánea), a detectar cuando la serpiente choca con las paredes, y a usar una bandera de "game over" para terminar la partida limpiamente.

## Dirección como estado

En el Módulo 8, la serpiente solo se movía cuando presionabas una tecla. Si no presionabas nada, se quedaba quieta. En Snake real, la serpiente siempre se está moviendo. Para lograr esto, necesitamos una variable que recuerde en qué dirección va:

```python
current_direction = "RIGHT"
```

La serpiente empieza moviéndose hacia la derecha. En cada cuadro del juego, se mueve en la dirección almacenada en `current_direction`, sin importar si el jugador presionó algo o no:

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

Fíjate en la diferencia con el Módulo 8: antes movíamos según `key` (la tecla presionada). Ahora movemos según `current_direction` (el estado actual). Las teclas solo cambian `current_direction`, y el movimiento siempre sucede.

## Cambiando de dirección

Las flechas del teclado ahora actualizan `current_direction` en vez de mover directamente:

```python
key = get_key_pressed()

if key == "UP":
    current_direction = "UP"
elif key == "DOWN":
    current_direction = "DOWN"
elif key == "LEFT":
    current_direction = "LEFT"
elif key == "RIGHT":
    current_direction = "RIGHT"
```

Si el jugador presiona arriba, la dirección cambia a `"UP"`. En el siguiente cuadro (y en todos los siguientes), la serpiente se moverá hacia arriba hasta que el jugador presione otra tecla.

## Prevención de dirección inversa

Hay un problema con el código anterior: si la serpiente va hacia la derecha y el jugador presiona izquierda, la serpiente se daría vuelta sobre sí misma. En Snake, eso no está permitido — sería una colisión instantánea con tu propia cola.

La solución es agregar una condición extra: solo cambiar de dirección si la nueva dirección no es la opuesta a la actual:

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

Aquí usamos el operador `and` del Módulo 4. Cada condición verifica dos cosas: ¿el jugador presionó esta tecla? **Y** ¿la dirección actual no es la opuesta? Solo si ambas son verdaderas, se permite el cambio.

Por ejemplo, si `current_direction` es `"RIGHT"` y el jugador presiona izquierda, la condición `key == "LEFT" and current_direction != "RIGHT"` es `False` (porque `current_direction` sí es `"RIGHT"`), y la dirección no cambia.

## Detección de colisión con paredes

Ahora necesitamos que la serpiente muera al tocar las paredes. Recordemos que las paredes están en:
- Fila 0 (borde superior) y fila `grid_height - 1` (borde inferior)
- Columna 0 (borde izquierdo) y columna `grid_width - 1` (borde derecho)

Después de mover la cabeza, verificamos si está en una posición de borde o más allá:

```python
if (snake_head_row <= 0
        or snake_head_row >= grid_height - 1
        or snake_head_col <= 0
        or snake_head_col >= grid_width - 1):
    is_game_over = True
```

Usamos `<=` y `>=` para cubrir el caso donde la serpiente está exactamente en el borde. Todas las condiciones están conectadas con `or` — basta con que una sea verdadera para que el juego termine.

> **💡 Tip:** Ponemos cada condición en una línea separada para que sea más fácil de leer. Python permite romper una línea después de un paréntesis abierto sin ninguna sintaxis especial.

## La bandera `is_game_over`

En vez de usar `break` inmediatamente cuando detectamos una colisión, primero marcamos una variable:

```python
is_game_over = False  # Al inicio del programa

# ... dentro del bucle, después de la colisión ...
is_game_over = True
```

¿Por qué no simplemente `break`? Porque queremos que el programa dibuje un último cuadro mostrando dónde chocó la serpiente, y luego muestre "Game over". Si hiciéramos `break` de inmediato, la pantalla no se actualizaría y el jugador no vería qué pasó.

El patrón completo es: detectar la colisión, marcar `is_game_over = True`, dibujar la cuadrícula una última vez, y **después** del dibujo verificar la bandera:

```python
    # Dibujar la cuadrícula (siempre, incluso en game over)
    # ... código de dibujo ...

    if is_game_over:
        print("Game over")
        break
```

## El programa completo, paso a paso

Juntemos todas las piezas. Al inicio del programa:

```python
import os
import time
from keyboard import setup_keyboard, get_key_pressed

setup_keyboard()
os.system("cls" if os.name == "nt" else "clear")

grid_width = 150
grid_height = 30
snake_head_col = grid_width // 2
snake_head_row = grid_height // 2
is_game_over = False
current_direction = "RIGHT"
```

Ahora tenemos dos variables nuevas: `is_game_over` empieza en `False` y `current_direction` empieza en `"RIGHT"`.

Dentro del bucle del juego, los tres pasos se ven así:

```python
while True:
    # 1. Entrada — cambiar dirección (con prevención de reversa)
    key = get_key_pressed()

    if key == "UP" and current_direction != "DOWN":
        current_direction = "UP"
    elif key == "DOWN" and current_direction != "UP":
        current_direction = "DOWN"
    elif key == "LEFT" and current_direction != "RIGHT":
        current_direction = "LEFT"
    elif key == "RIGHT" and current_direction != "LEFT":
        current_direction = "RIGHT"

    # 2. Actualización — mover y verificar colisiones
    if current_direction == "UP":
        snake_head_row -= 1
    elif current_direction == "DOWN":
        snake_head_row += 1
    elif current_direction == "LEFT":
        snake_head_col -= 1
    elif current_direction == "RIGHT":
        snake_head_col += 1

    if (snake_head_row <= 0
            or snake_head_row >= grid_height - 1
            or snake_head_col <= 0
            or snake_head_col >= grid_width - 1):
        is_game_over = True

    # 3. Dibujo (igual que antes)
    # ... cuadrícula ...

    if is_game_over:
        print("Game over")
        break

    time.sleep(0.1)
```

## Errores comunes

El error más frecuente es poner el movimiento **antes** de la lectura de teclas, o la colisión **antes** del movimiento. El orden correcto es: leer tecla → actualizar dirección → mover → verificar colisión → dibujar → verificar game over. Si cambias este orden, el juego puede comportarse de maneras extrañas, como morir un cuadro tarde o no responder a la última tecla presionada.

Otro error es olvidar inicializar `current_direction`. Si no le das un valor inicial, la serpiente no se moverá hasta que el jugador presione una tecla, lo que no es el comportamiento correcto de Snake.

También cuidado con la verificación de colisión: necesitas usar `<=` y `>=`, no `<` y `>`. Si usas `<`, la serpiente puede quedar en la posición del borde sin morir, lo que se ve raro porque está encima de la pared.

## Mini-proyecto: Snake sin cola

Vas a seguir trabajando en tu `main.py` del Módulo 8 — abre ese mismo archivo y agrégale las reglas del juego. El `@` ahora:

1. Se mueve automáticamente en la dirección actual (empieza hacia la derecha).
2. Cambia de dirección con las flechas, pero no puede invertirse.
3. Muere al tocar cualquier pared, mostrando "Game over".

Esto es Snake sin comida y sin cola — pero ya tiene las reglas fundamentales.

Este módulo no tiene archivo inicial. Abre tu `main.py` y agrega las nuevas funcionalidades directamente ahí. Recuerda que `keyboard.py` debe seguir en la misma carpeta.

Cuando termines, compara tu resultado con la [solución completa](09_snake_sin_cola_solucion.py).

---

¡Tu programa ya tiene reglas! La serpiente se mueve sola, responde a las flechas, y muere al chocar. En el próximo módulo vamos a agregar las últimas piezas: comida que aparece aleatoriamente, una cola que crece, y un puntaje. Después de eso, tendrás un juego de Snake completo.
