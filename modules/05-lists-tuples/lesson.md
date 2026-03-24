---
title: "Módulo 5 — Listas y tuplas"
nav_order: 5
layout: default
---

# Módulo 5 — Listas y tuplas

Hasta ahora, cada variable guarda un solo dato — un nombre, un número, un booleano. Pero en el juego de Snake, la serpiente tiene una cola que crece. Necesitamos recordar no una posición, sino muchas posiciones al mismo tiempo. Para eso existen las **listas**.

## Lo que aprenderás

En este módulo vas a aprender a crear listas, agregar elementos con `append()`, acceder a elementos por su posición (índice), y recortar listas con *slicing*. También vas a conocer las tuplas, que son como listas pero que no cambian, y el operador `in` para verificar si algo está dentro de una lista.

## Listas: guardar muchos datos juntos

Una lista es una colección ordenada de elementos. Se crea con corchetes:

```python
frutas = ["manzana", "banana", "naranja"]
print(frutas)
```

Esto muestra `['manzana', 'banana', 'naranja']`. La lista guarda tres textos en un orden específico.

También puedes crear una lista vacía y agregarle cosas después:

```python
compras = []
print(compras)
```

Esto muestra `[]` — una lista sin ningún elemento.

## Agregar elementos con `append()`

Para agregar un elemento al final de una lista, usas `append()`:

```python
compras = []
compras.append("leche")
compras.append("pan")
compras.append("huevos")
print(compras)
```

Esto muestra `['leche', 'pan', 'huevos']`. Cada `append()` agrega un elemento al final.

En nuestro juego de Snake, la cola de la serpiente es una lista. Cada vez que la serpiente se mueve, agregamos su posición actual a la lista:

```python
snake_tail = []
snake_tail.append((75, 15))
```

No te preocupes por los paréntesis dobles todavía — pronto veremos qué son las tuplas.

## Acceder a elementos por índice

Cada elemento de una lista tiene un número de posición llamado **índice**. El primer elemento tiene índice `0`, el segundo tiene `1`, y así:

```python
colores = ["rojo", "verde", "azul"]
print(colores[0])
print(colores[1])
print(colores[2])
```

Esto muestra:

```
rojo
verde
azul
```

También puedes usar índices negativos. El índice `-1` es el último elemento, `-2` es el penúltimo:

```python
colores = ["rojo", "verde", "azul"]
print(colores[-1])
print(colores[-2])
```

Esto muestra:

```
azul
verde
```

## Slicing: recortar listas

El *slicing* (rebanado) te permite obtener una parte de la lista. Se usa con la sintaxis `lista[inicio:fin]`:

```python
numeros = [10, 20, 30, 40, 50]
print(numeros[1:4])
```

Esto muestra `[20, 30, 40]` — los elementos desde el índice 1 hasta el 3 (el índice 4 no se incluye).

Lo más interesante para nuestro juego es el **slicing negativo**. Si escribes `lista[-3:]`, obtienes los últimos 3 elementos:

```python
numeros = [10, 20, 30, 40, 50]
print(numeros[-3:])
```

Esto muestra `[30, 40, 50]`.

En el juego de Snake, la cola tiene un largo máximo. Cada vez que la serpiente se mueve, agregamos una posición, pero solo nos quedamos con las últimas posiciones. Eso se hace así:

```python
snake_tail = snake_tail[-snake_tail_length:]
```

Si `snake_tail_length` es `3`, esto mantiene solo los últimos 3 elementos de la lista. Así la cola nunca crece más de lo que debe.

## Tuplas: datos que no cambian

Una tupla es parecida a una lista, pero una vez creada **no se puede modificar**. Se crea con paréntesis:

```python
coordenada = (5, 10)
print(coordenada)
```

Esto muestra `(5, 10)`. Puedes acceder a cada valor con índices, igual que con una lista:

```python
coordenada = (5, 10)
print(coordenada[0])
print(coordenada[1])
```

Esto muestra `5` y luego `10`.

Las tuplas son perfectas para representar coordenadas `(x, y)` porque una coordenada es un par de valores que van juntos. En el juego de Snake, la posición de la comida es una tupla:

```python
food_item = (30, 12)
print("La comida está en columna", food_item[0], "fila", food_item[1])
```

## El operador `in`: buscar en una lista

El operador `in` verifica si un elemento existe dentro de una lista:

```python
invitados = ["Ana", "Pedro", "Lucía"]
nombre = "Pedro"

if nombre in invitados:
    print(nombre, "está en la lista.")
else:
    print(nombre, "no está invitado.")
```

Esto muestra `Pedro está en la lista.`

También funciona con tuplas dentro de listas. En el juego de Snake, necesitamos verificar si la cabeza de la serpiente chocó con su propia cola:

```python
snake_tail = [(10, 5), (11, 5), (12, 5)]
snake_head = (12, 5)

if snake_head in snake_tail:
    print("¡La serpiente chocó consigo misma!")
```

Como `(12, 5)` está en la lista `snake_tail`, la condición es `True`.

## Errores comunes

El error más común con listas es intentar acceder a un índice que no existe. Si una lista tiene 3 elementos, sus índices son `0`, `1` y `2`. Si intentas acceder al índice `3`, Python te da un error `IndexError`. Siempre verifica que el índice sea menor que la cantidad de elementos.

Otro error frecuente es confundir listas con tuplas. Recuerda: listas usan corchetes `[]` y se pueden modificar; tuplas usan paréntesis `()` y no se pueden cambiar después de crearse. Si intentas hacer `append()` en una tupla, Python te mostrará un error.

Finalmente, cuidado con el slicing negativo. `lista[-0:]` no te da cero elementos — te da la lista completa, porque `-0` es igual a `0`. Si `snake_tail_length` es `0`, `snake_tail[-0:]` devuelve toda la lista en vez de una lista vacía. Por eso en el juego verificamos primero si `snake_tail_length > 0` antes de hacer el recorte.

## Mini-proyecto: Rastreador de posiciones

Vas a crear un programa donde el jugador se mueve en una línea de una dimensión (izquierda/derecha). El programa recuerda todas las posiciones visitadas.

El programa funciona así:

1. El jugador empieza en la posición `5`.
2. En cada turno, el jugador escribe "izquierda" o "derecha".
3. La posición se actualiza: izquierda resta 1, derecha suma 1.
4. La posición actual se agrega a una lista de posiciones visitadas.
5. Después de cada movimiento, el programa muestra la posición actual y la lista completa de posiciones visitadas.
6. El jugador escribe "salir" para terminar.

[Descarga el archivo inicial](mini_project.py) — tiene la estructura con el bucle y la variable de posición ya creadas.

Cuando termines, compara tu resultado con la [solución completa](solution.py).

---

¡Ahora sabes guardar y manipular colecciones de datos! Las listas y tuplas son el corazón del juego de Snake — la cola es una lista de tuplas con coordenadas. En el próximo módulo vamos a usar bucles anidados para dibujar una cuadrícula en la pantalla, que será el tablero del juego.
