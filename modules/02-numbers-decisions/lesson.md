---
title: "Módulo 2 — Números y decisiones"
nav_order: 2
layout: default
---

# Módulo 2 — Números y decisiones

Nuestro juego de Snake necesita saber dónde está la serpiente en la pantalla. Eso significa trabajar con números — posiciones, tamaños, puntajes. Y también necesita tomar decisiones: ¿chocó con la pared? ¿se comió la comida? En este módulo vas a aprender a hacer operaciones matemáticas y a que tu programa elija qué hacer según las circunstancias.

## Lo que aprenderás

En este módulo vas a trabajar con números enteros y operaciones aritméticas como suma, resta, multiplicación y división entera. También vas a aprender a comparar valores y a usar `if`, `elif` y `else` para que tu programa tome decisiones. Finalmente, vas a conocer los valores `True` y `False`, que le permiten a Python recordar si algo es verdadero o falso.

## Operaciones con números

En el módulo anterior usaste variables para guardar texto y números. Ahora vamos a operar con esos números. Python puede hacer las operaciones matemáticas que ya conoces:

```python
puntos = 10
bonus = 3
total = puntos + bonus
print("Total:", total)
```

Esto muestra `Total: 13`. Las operaciones disponibles son:

```python
a = 20
b = 6
print(a + b)    # Suma: 26
print(a - b)    # Resta: 14
print(a * b)    # Multiplicación: 120
print(a // b)   # División entera: 3
```

La división entera (`//`) es especial. Divide y se queda solo con la parte entera del resultado, sin decimales. `20 // 6` da `3` porque 6 cabe 3 veces en 20. Este operador es muy útil en nuestro juego — lo usaremos para calcular el centro de la pantalla. Si la pantalla tiene 150 columnas, el centro está en `150 // 2`, que es `75`.

En el juego de Snake, las primeras líneas de código definen el tamaño de la pantalla y la posición inicial de la serpiente justo así:

```python
grid_width = 150
grid_height = 30
snake_head_col = grid_width // 2
```

La serpiente empieza en la columna 75, que es el centro exacto de la pantalla.

## Comparaciones

Para tomar decisiones, Python necesita poder comparar cosas. Los operadores de comparación son:

```python
edad = 15
print(edad == 15)    # ¿Es igual a 15? True
print(edad != 10)    # ¿Es diferente de 10? True
print(edad > 18)     # ¿Es mayor que 18? False
print(edad < 20)     # ¿Es menor que 20? True
print(edad >= 15)    # ¿Es mayor o igual a 15? True
print(edad <= 14)    # ¿Es menor o igual a 14? False
```

Cada comparación produce un resultado que es `True` (verdadero) o `False` (falso). Estos valores se llaman **booleanos**, y son fundamentales — le permiten a Python evaluar condiciones.

> **💡 Tip:** Cuidado con `==` y `=`. Un solo `=` sirve para guardar un valor en una variable (`edad = 15`). Dos signos `==` sirven para comparar (`edad == 15`). Son cosas muy diferentes.

## Booleanos

`True` y `False` son valores que puedes guardar en una variable, igual que un número o un texto:

```python
tiene_hambre = True
print(tiene_hambre)
```

Esto muestra `True`. En nuestro juego vamos a usar un booleano para saber si la partida terminó:

```python
is_game_over = False
```

Empieza en `False` porque el juego está activo. Cuando la serpiente choque con algo, lo cambiaremos a `True`.

## Tomando decisiones: `if`, `elif`, `else`

Ahora viene la parte más poderosa de este módulo. Con `if` le dices a Python: "si esta condición es verdadera, ejecuta este código".

```python
temperatura = 35
if temperatura > 30:
    print("¡Hace mucho calor!")
```

Si `temperatura` es mayor que 30, Python muestra el mensaje. Si no, no hace nada. Fíjate en dos detalles importantes: los dos puntos (`:`) al final de la línea del `if`, y que la línea siguiente está **indentada** (tiene espacios al inicio). Esa indentación le dice a Python cuáles líneas pertenecen al `if`.

Si quieres que Python haga algo diferente cuando la condición no se cumple, usas `else`:

```python
temperatura = 15
if temperatura > 30:
    print("¡Hace mucho calor!")
else:
    print("El clima está agradable.")
```

Y si tienes más de dos opciones, usas `elif` (que viene de "else if"):

```python
temperatura = -5
if temperatura > 30:
    print("¡Hace mucho calor!")
elif temperatura > 15:
    print("El clima está agradable.")
elif temperatura > 0:
    print("Hace un poco de frío.")
else:
    print("¡Está helando!")
```

Python revisa las condiciones de arriba hacia abajo. En cuanto encuentra una que sea verdadera, ejecuta ese bloque y se salta todos los demás. Si ninguna condición es verdadera, ejecuta el `else`.

## Convertir texto a número con `int()`

Cuando usas `input()` para pedirle algo al usuario, el resultado siempre es texto — incluso si el usuario escribe un número. Para poder hacer operaciones matemáticas con ese valor, necesitas convertirlo a número con `int()`:

```python
texto = input("Escribe un número: ")
numero = int(texto)
print(numero + 1)
```

Si el usuario escribe `7`, `texto` contiene `"7"` (texto), pero `numero` contiene `7` (número). Sin `int()`, Python no podría sumarle 1.

## Conectando con el juego

En el juego de Snake, las decisiones son constantes. Cuando el jugador presiona una tecla, el programa necesita decidir qué hacer:

```python
if key == "UP":
    snake_head_row = snake_head_row - 1
```

Todavía no vamos a escribir esta parte del juego — eso viene en módulos futuros. Pero ya puedes ver que `if` y las comparaciones son piezas fundamentales.

## Errores comunes

El error más frecuente es olvidar los dos puntos (`:`) al final de `if`, `elif` o `else`. Python te mostrará un error de sintaxis si los omites. Acuérdate: cada línea que empieza con `if`, `elif` o `else` termina con `:`.

Otro error muy común es confundir `=` con `==`. Si escribes `if edad = 15:` Python te dará un error porque `=` es para asignar, no para comparar. Para preguntar "¿es igual?" necesitas `==`.

También cuidado con la indentación. Todo el código que pertenece a un `if` debe tener la misma cantidad de espacios al inicio (normalmente 4 espacios). Si una línea tiene 4 espacios y la siguiente tiene 3, Python se confunde y marca error.

## Mini-proyecto: Adivina el número

Vas a crear un juego donde el programa elige un número secreto y el jugador intenta adivinarlo. El programa le dice si su intento es muy alto, muy bajo, o correcto.

El juego funciona así:

1. El programa tiene un número secreto guardado en una variable (por ahora, ponlo fijo — por ejemplo, `42`).
2. El jugador escribe un número.
3. El programa compara el intento con el número secreto y dice "Muy alto", "Muy bajo", o "¡Correcto!".
4. Si el jugador no adivina, puede intentar de nuevo (el programa repite los pasos 2 y 3).

[Descarga el archivo inicial](02_adivina_el_numero.py) — encontrarás la estructura del juego con un bucle `while True` ya escrito. Ese bucle hace que el programa repita los pasos automáticamente. No te preocupes por entender el bucle todavía — lo vamos a estudiar a fondo en el siguiente módulo. Por ahora, solo necesitas saber que todo lo que esté dentro del bucle se repite una y otra vez hasta que pongas `break`.

Cuando termines, compara tu solución con la [solución completa](02_adivina_el_numero_solucion.py).

---

¡Excelente! Ya sabes hacer cálculos y tomar decisiones. En el próximo módulo vas a aprender a repetir acciones con bucles — la herramienta que hace posible que un juego corra sin parar hasta que el jugador pierda.
