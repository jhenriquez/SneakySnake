---
title: "Módulo 7 — Funciones e importaciones"
nav_order: 7
layout: default
---

# Módulo 7 — Funciones e importaciones

En el módulo anterior dibujaste una cuadrícula con un jugador y un objeto en posiciones fijas. Pero un juego necesita que las cosas cambien — que la comida aparezca en un lugar diferente cada vez, que el programa haga pausas, que la pantalla se actualice. Para lograr eso, necesitamos herramientas que otras personas ya crearon. En este módulo vas a aprender a usarlas.

## Lo que aprenderás

En este módulo vas a aprender qué son las funciones, cómo llamarlas con argumentos, y qué son los valores de retorno. También vas a aprender a usar `import` para acceder a código que viene incluido con Python, incluyendo `random.randint()` para generar números aleatorios y `time.sleep()` para hacer pausas.

## ¿Qué es una función?

Ya has usado funciones sin saberlo. `print()` es una función — le das un dato entre paréntesis y ella lo muestra en pantalla. `input()` es otra — le das un mensaje y te devuelve lo que el usuario escribió. `int()` es otra más — le das un texto y te devuelve un número.

Una función es un bloque de código con nombre que hace una tarea específica. Cuando la **llamas** (usas su nombre seguido de paréntesis), se ejecuta. Las cosas que pones dentro de los paréntesis se llaman **argumentos** — son los datos que la función necesita para trabajar.

```python
nombre = "Ana"
print(nombre)
```

Aquí, `nombre` es el argumento que le pasamos a `print()`. La función recibe ese dato y lo muestra en la pantalla.

Algunas funciones **devuelven** un valor. Eso significa que puedes guardar su resultado en una variable:

```python
texto = input("Escribe algo: ")
numero = int("42")
```

`input()` devuelve lo que el usuario escribió. `int()` devuelve el número que corresponde al texto. A este valor devuelto se le llama **valor de retorno**.

## `import`: usar código de otros

Python viene con una enorme colección de módulos — archivos de código que contienen funciones útiles ya escritas. Para usar uno de estos módulos, necesitas **importarlo** con la palabra `import`:

```python
import random

numero = random.randint(1, 10)
print("Número aleatorio:", numero)
```

`import random` le dice a Python "carga el módulo `random` para que pueda usar sus funciones". Después, usas `random.randint(1, 10)` para llamar a la función `randint` que vive dentro del módulo `random`. Esta función recibe dos argumentos (un mínimo y un máximo) y devuelve un número aleatorio entre ellos (incluyendo ambos extremos).

Cada vez que ejecutes este programa, el número será diferente. Pruébalo varias veces.

## El módulo `random`

`random.randint(a, b)` genera un número entero aleatorio entre `a` y `b`:

```python
import random

dado = random.randint(1, 6)
print("Tiraste un", dado)
```

En nuestro juego de Snake, usamos `random.randint()` para colocar la comida en una posición aleatoria dentro de la cuadrícula:

```python
import random

grid_width = 40
grid_height = 15
food_col = random.randint(1, grid_width - 2)
food_row = random.randint(1, grid_height - 2)
```

Usamos `1` como mínimo y `grid_width - 2` como máximo para que la comida nunca caiga encima del borde. Recuerda que la columna 0 es el borde izquierdo y `grid_width - 1` es el borde derecho.

## El módulo `time`

El módulo `time` tiene una función muy útil: `time.sleep()`. Le pasas un número de segundos y el programa se detiene durante ese tiempo:

```python
import time

print("Preparados...")
time.sleep(1)
print("Listos...")
time.sleep(1)
print("¡Fuera!")
```

Este programa muestra "Preparados...", espera 1 segundo, muestra "Listos...", espera otro segundo, y muestra "¡Fuera!". Puedes usar decimales: `time.sleep(0.5)` espera medio segundo, y `time.sleep(0.1)` espera una décima de segundo.

En el juego de Snake, `time.sleep(0.1)` controla la velocidad. Después de dibujar cada cuadro del juego, el programa espera 0.1 segundos antes del siguiente. Sin esa pausa, el juego correría tan rápido que sería imposible jugarlo.

## El módulo `os`

Otro módulo útil es `os`, que permite interactuar con el sistema operativo. En particular, usaremos `os.system()` para limpiar la pantalla:

```python
import os

os.system("cls" if os.name == "nt" else "clear")
```

Esta línea ejecuta un comando del sistema: `cls` en Windows o `clear` en Mac/Linux. `os.name` nos dice en qué sistema estamos — si es `"nt"`, estamos en Windows. No te preocupes por entender todos los detalles de esta línea; lo importante es saber que limpia la pantalla. La usaremos al inicio del juego para empezar con una pantalla vacía.

## Importar funciones específicas con `from`

A veces quieres importar solo una función específica de un módulo. Para eso usas `from ... import ...`:

```python
from random import randint

numero = randint(1, 100)
print(numero)
```

Con esta sintaxis no necesitas escribir `random.randint()` — puedes usar `randint()` directamente. Ambas formas funcionan, pero cada una tiene su momento.

En nuestro juego, usamos esta sintaxis para importar las funciones del módulo de teclado:

```python
from keyboard import setup_keyboard, get_key_pressed
```

Esto importa dos funciones: `setup_keyboard` y `get_key_pressed`. Las vamos a usar en el próximo módulo.

## Errores comunes

El error más frecuente es olvidar el `import`. Si intentas usar `random.randint()` sin haber escrito `import random` al inicio del programa, Python te dará un error diciendo que no conoce `random`. Siempre pon los `import` al principio del archivo.

Otro error común es confundir los límites de `random.randint()`. A diferencia de `range()`, que no incluye el último número, `randint()` **sí lo incluye**. `randint(1, 6)` puede devolver 6. Tenlo en cuenta al calcular posiciones.

Finalmente, cuidado con `time.sleep()` — el argumento son **segundos**, no milisegundos. Si escribes `time.sleep(1000)` pensando que es un segundo, tu programa se va a congelar por más de 16 minutos.

## Mini-proyecto: Escena aleatoria

Vas a tomar la cuadrícula del Módulo 6 y hacerla más interesante: ahora el objeto `*` aparecerá en una posición aleatoria cada vez que ejecutes el programa. También vas a agregar una pausa para poder ver el resultado antes de que el programa termine.

Tu programa debe:

1. Importar `random` y `time`.
2. Definir `grid_width = 40` y `grid_height = 15`.
3. Colocar el jugador `@` en el centro de la cuadrícula.
4. Generar la posición del objeto `*` con `random.randint()`, asegurándote de que caiga dentro de los bordes (no en el borde mismo).
5. Dibujar la cuadrícula completa con los bordes, el jugador y el objeto.
6. Agregar `time.sleep(3)` al final para que la ventana no se cierre inmediatamente.

Ejecuta el programa varias veces y verifica que el `*` aparece en un lugar diferente cada vez.

Este módulo no tiene archivo inicial — es hora de escribir el programa completo por tu cuenta. Puedes basarte en tu solución del Módulo 6 como punto de partida.

Cuando termines, compara tu resultado con la [solución completa](solution.py).

---

¡Ahora tu cuadrícula tiene elementos aleatorios y pausas! Esto ya empieza a parecerse a un juego. En el próximo módulo vamos a dar el gran salto: leer las teclas del jugador en tiempo real y hacer que el `@` se mueva por la pantalla. Es ahí donde tu programa se convierte en algo que realmente se siente como un juego.
