---
title: "Módulo 3 — Bucles"
nav_order: 3
layout: default
---

# Módulo 3 — Bucles

Un juego de Snake no se ejecuta una sola vez y se detiene. La serpiente se mueve, la pantalla se actualiza, el jugador presiona teclas, y todo eso se repite muchas veces por segundo hasta que la partida termina. Para lograr eso necesitamos **bucles** — instrucciones que le dicen a Python "repite esto".

## Lo que aprenderás

En este módulo vas a aprender dos tipos de bucles: `while` (que repite mientras una condición sea verdadera) y `for` con `range()` (que repite un número específico de veces). También vas a aprender a usar `break` para salir de un bucle y a usar contadores para llevar la cuenta de cuántas veces se ha repetido algo.

## El bucle `while`

Un bucle `while` repite un bloque de código mientras su condición sea `True`:

```python
contador = 5
while contador > 0:
    print(contador)
    contador = contador - 1
```

Esto muestra:

```
5
4
3
2
1
```

Python evalúa la condición `contador > 0` antes de cada repetición. Mientras sea verdadera, ejecuta el código indentado. Cuando `contador` llega a `0`, la condición se vuelve `False` y el bucle termina.

Fíjate que dentro del bucle restamos 1 a `contador` en cada vuelta. Si olvidaras esa línea, `contador` siempre sería `5`, la condición siempre sería verdadera, y el programa nunca terminaría. Eso se llama un **bucle infinito**.

## `while True` y `break`

A veces no sabes cuántas veces necesitas repetir algo — por ejemplo, en el juego de adivinar del módulo anterior, no sabes cuántos intentos va a necesitar el jugador. Para esos casos, puedes usar `while True` junto con `break`:

```python
while True:
    respuesta = input("Escribe 'salir' para terminar: ")
    if respuesta == "salir":
        break
    print("Escribiste:", respuesta)

print("¡Adiós!")
```

`while True` crea un bucle que se repite para siempre porque la condición (`True`) nunca cambia. La única manera de salir es usando `break`, que le dice a Python "sal de este bucle ahora mismo". Después del `break`, Python continúa con la siguiente línea fuera del bucle.

Este patrón es exactamente el que usa nuestro juego de Snake. El juego tiene un gran bucle `while True` que se repite en cada cuadro del juego:

```python
while True:
    # ... leer teclas, mover serpiente, dibujar pantalla ...
    break  # cuando el juego termina
```

Cada repetición del bucle es un "cuadro" del juego — como los cuadros de una película. El bucle se repite una y otra vez hasta que la serpiente choca con algo, y en ese momento usamos `break` para salir.

## Contadores dentro de un bucle

Un patrón muy común es usar una variable que lleva la cuenta de cuántas veces se ha repetido algo:

```python
repeticiones = 0
while repeticiones < 3:
    print("Repetición número", repeticiones)
    repeticiones = repeticiones + 1
```

Esto muestra:

```
Repetición número 0
Repetición número 1
Repetición número 2
```

Empieza en `0` y cuenta hasta `2` (tres repeticiones en total). Cada vuelta del bucle incrementa el contador en `1`.

## El bucle `for` y `range()`

Cuando sabes exactamente cuántas veces quieres repetir algo, Python tiene una herramienta más directa: el bucle `for` con `range()`.

```python
for i in range(5):
    print("Vuelta", i)
```

Esto muestra:

```
Vuelta 0
Vuelta 1
Vuelta 2
Vuelta 3
Vuelta 4
```

`range(5)` genera los números del `0` al `4` (cinco números en total). En cada vuelta, la variable `i` toma el siguiente número. Fíjate que empieza en `0`, no en `1` — eso es normal en programación y te va a ser muy útil cuando trabajemos con listas y cuadrículas.

También puedes darle a `range()` un punto de inicio:

```python
for i in range(1, 4):
    print(i)
```

Esto muestra `1`, `2`, `3`. El primer número es dónde empieza y el segundo es dónde se detiene (sin incluirlo).

Recuerda el patrón que vimos en el Módulo 1: lo que va dentro de los paréntesis es la información que le das a la instrucción. Con `range()` puedes darle uno, dos o tres datos separados por comas, y cada uno cambia su comportamiento.

## Contar hacia atrás con `range()`

Si le das tres datos a `range()`, el tercero le dice **cuánto sumar en cada paso**. Si quieres contar hacia atrás, el tercer dato debe ser negativo:

```python
for i in range(5, 0, -1):
    print(i)
```

Esto muestra:

```
5
4
3
2
1
```

Los tres datos son: **dónde empieza** (5), **dónde se detiene** (0, sin incluirlo), y **cuánto suma en cada paso** (-1). Como el tercer dato es `-1`, en cada vuelta Python le suma `-1` al número actual — es decir, le resta 1. Así va de 5 a 4, de 4 a 3, y así hasta llegar a 1 (se detiene antes de 0).

Otro ejemplo: contar de 10 en 10:

```python
for i in range(0, 50, 10):
    print(i)
```

Esto muestra `0`, `10`, `20`, `30`, `40`. El tercer dato es `10`, así que en cada paso suma 10.

Resumiendo las formas de usar `range()`:

- `range(5)` — genera 0, 1, 2, 3, 4 (un solo dato: cuántos números)
- `range(2, 7)` — genera 2, 3, 4, 5, 6 (dos datos: inicio y fin)
- `range(10, 0, -1)` — genera 10, 9, 8, ..., 1 (tres datos: inicio, fin, y cuánto sumar en cada paso)

En nuestro juego, vamos a usar `for` con `range()` para dibujar la cuadrícula fila por fila. Eso lo veremos en el Módulo 6, pero por ahora ya sabes cómo funciona.

## Comparación: `while` vs `for`

Puedes lograr lo mismo con ambos. Por ejemplo, una cuenta del 1 al 5:

```python
# Con while
numero = 1
while numero <= 5:
    print(numero)
    numero = numero + 1

# Con for (más corto)
for numero in range(1, 6):
    print(numero)
```

Ambos producen el mismo resultado. Usa `for` cuando sepas cuántas veces vas a repetir. Usa `while` cuando la repetición dependa de una condición que puede cambiar en cualquier momento.

## Errores comunes

El error más peligroso con bucles es crear un bucle infinito por accidente. Si usas `while` con una condición que nunca se vuelve `False`, el programa se queda atrapado para siempre. Si eso te pasa, presiona `Ctrl+C` en la terminal para detener el programa. Siempre verifica que algo dentro del bucle haga que la condición eventualmente cambie.

Otro error común es equivocarse por uno con `range()`. Si quieres los números del 1 al 10, necesitas `range(1, 11)`, no `range(1, 10)`. El segundo número nunca se incluye.

Finalmente, recuerda indentar todo el código que pertenece al bucle. Si una línea no tiene indentación, Python la considera fuera del bucle y solo la ejecuta una vez.

## Mini-proyecto: Cuenta regresiva

Vas a crear un programa de cuenta regresiva que:

1. Muestra los números del 10 al 0, uno por uno.
2. Al llegar a 0, muestra "¡Despegue!".

Hazlo de dos maneras:
- Primero con un bucle `while` y un contador.
- Después con un bucle `for` y `range()`.

[Descarga el archivo inicial](03_cuenta_regresiva.py) — tiene la estructura para ambas versiones con indicaciones de dónde escribir tu código.

Cuando termines, compara tu resultado con la [solución completa](03_cuenta_regresiva_solucion.py).

---

¡Ya dominas los bucles! Ahora tu programa puede repetir acciones, que es la base de cualquier juego. En el próximo módulo vamos a aprender a combinar condiciones con `and`, `or` y `not` — lo que le va a permitir a nuestro Snake tomar decisiones más complejas, como "si presionó arriba Y no va hacia abajo, cambia de dirección".
