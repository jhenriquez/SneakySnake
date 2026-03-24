---
title: "Módulo 1 — ¡Hola, Python!"
nav_order: 1
layout: default
---

# Módulo 1 — ¡Hola, Python!

Imagina que pudieras darle instrucciones a tu computadora y que ella las siguiera al pie de la letra. Eso es exactamente lo que hace un programador, y hoy vas a escribir tu primer programa. Al final de este módulo, tu computadora te va a saludar por tu nombre.

## Lo que aprenderás

En este módulo vas a descubrir qué es la programación, cómo ejecutar un programa en Python y cómo usar `print()` para mostrar mensajes en la pantalla. También vas a aprender qué son las variables y cómo usarlas para guardar información como texto y números.

## ¿Qué es programar?

Programar es escribir instrucciones que una computadora puede seguir. Estas instrucciones se escriben en un lenguaje especial — en nuestro caso, **Python**. Python es uno de los lenguajes de programación más populares del mundo, y una de las razones es que se lee casi como inglés.

A lo largo de este curso, vas a usar Python para construir un juego de Snake completo. Pero primero, empecemos con lo más básico.

## Tu primer programa: `print()`

La instrucción más simple en Python es `print()`. Sirve para mostrar texto en la pantalla. Prueba escribir esto en un archivo llamado `hola.py` y ejecútalo:

```python
print("¡Hola, mundo!")
```

Cuando lo ejecutes, verás en la terminal:

```
¡Hola, mundo!
```

¡Felicidades! Acabas de escribir tu primer programa. La palabra `print` le dice a Python "muestra esto en la pantalla", y el texto entre comillas es lo que se va a mostrar. A ese texto entre comillas le llamamos **cadena de texto** (o simplemente *string*).

Puedes usar `print()` varias veces para mostrar varias líneas:

```python
print("Primera línea")
print("Segunda línea")
print("Tercera línea")
```

Cada `print()` muestra su texto y luego baja a la siguiente línea automáticamente.

## Variables: guardar información

Ahora imagina que estás creando un juego y necesitas recordar el nombre del jugador. No puedes escribir el nombre directamente cada vez — necesitas un lugar donde guardarlo. Para eso existen las **variables**.

Una variable es como una caja con etiqueta. Le pones un nombre a la caja, guardas algo adentro, y después puedes usar ese nombre para acceder a lo que guardaste.

```python
animal = "gato"
print(animal)
```

Esto muestra:

```
gato
```

En la primera línea creamos una variable llamada `animal` y le guardamos el texto `"gato"`. En la segunda línea le pedimos a Python que muestre lo que hay dentro de `animal`. Fíjate que cuando usamos la variable **no** ponemos comillas — si escribieras `print("animal")`, Python mostraría la palabra "animal", no "gato".

Puedes cambiar el valor de una variable en cualquier momento:

```python
color = "azul"
print(color)
color = "rojo"
print(color)
```

Esto muestra:

```
azul
rojo
```

La variable `color` primero tenía `"azul"` y luego le pusimos `"rojo"`. Python siempre recuerda el valor más reciente.

## Guardar números

Las variables no solo guardan texto. También pueden guardar números:

```python
edad = 15
print(edad)
```

Esto muestra `15`. Fíjate que los números **no** llevan comillas. Si escribes `"15"` con comillas, Python lo trata como texto, no como un número. Por ahora la diferencia parece pequeña, pero en el siguiente módulo vamos a hacer operaciones matemáticas y ahí será muy importante.

## Mostrar varias cosas con `print()`

Puedes mostrar texto y variables juntos separándolos con comas dentro de `print()`:

```python
nombre = "Carlos"
print("Hola,", nombre)
```

Esto muestra:

```
Hola, Carlos
```

Python automáticamente pone un espacio entre cada cosa que separas con coma. Puedes combinar texto y números sin problema:

```python
fruta = "manzanas"
cantidad = 5
print("Tengo", cantidad, fruta)
```

Esto muestra:

```
Tengo 5 manzanas
```

En nuestro juego de Snake vamos a usar exactamente este patrón para mostrar el nombre del jugador y su puntaje. Por ejemplo, el juego va a imprimir algo como `Bienvenido, Player` y `Tu puntaje actual es: 0`. Esas dos líneas usan variables — una para el nombre y otra para el número.

## Errores comunes

El error más frecuente en este módulo es olvidar las comillas alrededor del texto. Si escribes `print(Hola)` sin comillas, Python piensa que `Hola` es el nombre de una variable, y como no existe, te muestra un error. Recuerda: el texto siempre va entre comillas (`"Hola"`), pero los nombres de variables nunca llevan comillas.

Otro error común es escribir `Print()` con la P mayúscula. Python distingue entre mayúsculas y minúsculas, así que `print` y `Print` son cosas diferentes. Siempre escríbelo en minúscula: `print()`.

Por último, cuidado con los paréntesis. `print "Hola"` sin paréntesis no funciona en Python 3. Siempre necesitas los paréntesis: `print("Hola")`.

## Mini-proyecto: Saludo personalizado

Es hora de poner en práctica lo que aprendiste. Vas a crear un programa que:

1. Guarda un nombre en una variable.
2. Muestra un saludo personalizado con ese nombre.
3. Muestra una línea con el puntaje actual (que por ahora es 0).

El resultado debe verse así:

```
Bienvenido, María
Tu puntaje actual es: 0
```

[Descarga el archivo inicial](mini_project.py) — tiene la estructura del programa con comentarios que te indican dónde escribir tu código. El programa también incluye una línea con `input()` que te permite escribir tu nombre cuando ejecutas el programa. No te preocupes por entender `input()` todavía — es una línea que viene pre-escrita para ti.

Cuando termines, puedes comparar tu solución con la [solución completa](solution.py).

---

¡Tu primer programa funciona! Ya sabes cómo mostrar mensajes y guardar información en variables. En el siguiente módulo vamos a aprender a hacer operaciones matemáticas y a que tu programa tome decisiones — ingredientes clave para que nuestro Snake sepa dónde está y hacia dónde va.
