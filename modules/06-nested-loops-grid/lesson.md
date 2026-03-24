---
title: "Módulo 6 — Bucles anidados y la cuadrícula"
nav_order: 6
layout: default
---

# Módulo 6 — Bucles anidados y la cuadrícula

Hasta ahora, todo lo que has impreso en pantalla ha sido texto plano, línea por línea. Pero el juego de Snake necesita una cuadrícula — un rectángulo con bordes, un jugador (`@`) y comida (`*`) colocados en posiciones específicas. En este módulo vas a aprender a dibujar esa cuadrícula usando bucles anidados.

## Lo que aprenderás

En este módulo vas a aprender a poner un bucle `for` dentro de otro (bucles anidados) para recorrer filas y columnas. Vas a construir una cuadrícula de caracteres con bordes, y a colocar símbolos en posiciones exactas usando condiciones. Al final, vas a tener el tablero del juego de Snake dibujado en la terminal.

## ¿Qué es un bucle anidado?

Un bucle anidado es simplemente un bucle dentro de otro. El bucle de adentro se ejecuta completamente por cada repetición del bucle de afuera:

```python
for fila in range(3):
    for columna in range(4):
        print("F" + str(fila) + "C" + str(columna), end="  ")
    print()
```

Esto muestra:

```
F0C0  F0C1  F0C2  F0C3
F1C0  F1C1  F1C2  F1C3
F2C0  F2C1  F2C2  F2C3
```

El bucle externo recorre las filas (0, 1, 2). Para cada fila, el bucle interno recorre las columnas (0, 1, 2, 3). Fíjate que usamos `end="  "` dentro de `print()` para que no salte de línea después de cada dato, y luego un `print()` vacío al final de cada fila para bajar a la siguiente línea.

> **💡 Tip:** `str()` convierte un número a texto. Lo necesitas cuando quieres unir un número con texto usando `+`. En el Módulo 1 usamos comas en `print()` que lo hacen automáticamente, pero cuando construyes una cadena carácter por carácter, necesitas `str()`.

## Construir texto carácter por carácter

En vez de imprimir cada carácter individualmente, es más eficiente construir una línea completa como texto y luego imprimirla de una vez. Esto es lo que hace nuestro juego:

```python
for fila in range(3):
    linea = ""
    for columna in range(5):
        linea = linea + "#"
    print(linea)
```

Esto muestra:

```
#####
#####
#####
```

Empezamos con `linea = ""` (texto vacío) y en cada columna le agregamos un carácter. Cuando terminamos todas las columnas de esa fila, imprimimos la línea completa.

## Dibujando los bordes

Ahora vamos a dibujar un rectángulo con bordes. Las reglas son:

- Las esquinas son `+`.
- El borde superior e inferior son `-`.
- Los bordes izquierdo y derecho son `|`.
- El interior es un espacio en blanco.

```python
ancho = 20
alto = 8

for fila in range(alto):
    linea = ""
    for columna in range(ancho):
        if (fila == 0 or fila == alto - 1) and (columna == 0 or columna == ancho - 1):
            linea = linea + "+"
        elif fila == 0 or fila == alto - 1:
            linea = linea + "-"
        elif columna == 0 or columna == ancho - 1:
            linea = linea + "|"
        else:
            linea = linea + " "
    print(linea)
```

Esto dibuja:

```
+------------------+
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
+------------------+
```

Analicemos las condiciones. Para cada posición `(columna, fila)`, preguntamos:
- ¿Estamos en una esquina? (primera o última fila **y** primera o última columna) → `+`
- ¿Estamos en el borde superior o inferior? (primera o última fila) → `-`
- ¿Estamos en el borde izquierdo o derecho? (primera o última columna) → `|`
- ¿Ninguna de las anteriores? → espacio en blanco

El orden importa. Python revisa las condiciones de arriba hacia abajo y se queda con la primera que sea verdadera. Por eso las esquinas van primero — si no, una esquina se dibujaría como `-` o `|` en lugar de `+`.

## Colocando objetos en la cuadrícula

Ahora agreguemos un jugador (`@`) y un objeto (`*`) en posiciones específicas. Solo necesitamos agregar más condiciones `elif`:

```python
ancho = 20
alto = 8
jugador_col = 10
jugador_fila = 4
objeto_col = 5
objeto_fila = 2

for fila in range(alto):
    linea = ""
    for columna in range(ancho):
        if (fila == 0 or fila == alto - 1) and (columna == 0 or columna == ancho - 1):
            linea = linea + "+"
        elif fila == 0 or fila == alto - 1:
            linea = linea + "-"
        elif columna == 0 or columna == ancho - 1:
            linea = linea + "|"
        elif columna == jugador_col and fila == jugador_fila:
            linea = linea + "@"
        elif columna == objeto_col and fila == objeto_fila:
            linea = linea + "*"
        else:
            linea = linea + " "
    print(linea)
```

Esto muestra una cuadrícula con `@` en la posición (10, 4) y `*` en la posición (5, 2). Fíjate que comparamos `columna` con la posición en X y `fila` con la posición en Y. Es importante poner las condiciones del jugador y el objeto **después** de las condiciones de los bordes, para que los bordes siempre se dibujen correctamente.

Este es exactamente el patrón que usa el juego de Snake. En el código final, la cuadrícula se dibuja así:

```python
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
        elif column == food_item[0] and row == food_item[1]:
            row_chars += "*"
        else:
            row_chars += " "
    print(row_chars)
```

> **💡 Tip:** `row_chars += "+"` es una forma corta de escribir `row_chars = row_chars + "+"`. Hace exactamente lo mismo pero es más breve. Ambas formas son válidas.

## Errores comunes

El error más frecuente con bucles anidados es confundir filas con columnas. Recuerda: el bucle externo recorre las **filas** (de arriba hacia abajo) y el bucle interno recorre las **columnas** (de izquierda a derecha). Si los inviertes, la cuadrícula sale rotada.

Otro error es poner la condición de los objetos antes que la de los bordes. Si el jugador está en la posición `(0, 0)`, queremos ver `+` (la esquina), no `@`. Las condiciones de los bordes deben ir primero.

También cuidado con el orden de `columna` y `fila` al comparar posiciones. En nuestro sistema, `columna` es la posición horizontal (X) y `fila` es la posición vertical (Y). Es fácil invertirlas por accidente y terminar con el jugador en el lugar equivocado.

## Mini-proyecto: Escena estática

Vas a dibujar una cuadrícula de 40 columnas por 15 filas con:

1. Bordes de `+`, `-` y `|`.
2. Un jugador `@` en la posición columna 20, fila 7 (el centro).
3. Un objeto `*` en la posición columna 10, fila 3.

El programa imprime la cuadrícula una vez y termina.

[Descarga el archivo inicial](06_escena_estatica.py) — tiene las variables de tamaño y posiciones ya definidas, y la estructura de los bucles anidados. Tu trabajo es completar las condiciones que deciden qué carácter poner en cada posición.

Cuando termines, compara tu resultado con la [solución completa](06_escena_estatica_solucion.py).

---

¡Acabas de dibujar el tablero del juego! Ahora tiene bordes, un jugador y un objeto. Pero todo está fijo — no se mueve. En el próximo módulo vamos a aprender sobre funciones e importaciones, lo que nos permitirá usar herramientas como números aleatorios y pausas. Paso a paso, esto se está convirtiendo en un juego de verdad.
