# 🐍 Retos para Postulantes al Python Study Group OOP

¡Hola, pythonista! 👋
Bienvenida/o al repositorio de retos para postulantes al **Python Study Group Object Oriented Programming (OOP)**.

Aquí encontrarás una serie de desafíos diseñados para evaluar si cuentas con las habilidades necesarias para ser parte del **Python Study Group OOP**.

Recuerda revisar el [código de conducta de la comunidad Python La Paz](https://pylapaz.org/coc/) y los [términos y condiciones de Python Study Group 2025](https://pylapaz.org/python-study-group-2025/) antes de comenzar.

---

## 🧠 ¿Qué habilidades necesitas para unirte?

Para formar parte del Python Study Group OOP, es importante que tengas conocimientos previos en los siguientes temas:

1. Gestión de archivos y directorios
2. Manejo básico de **Git** y **GitHub**
3. Uso de **Markdown** para documentación técnica
4. Fundamentos sólidos en Python:
     * Tipos de datos
     * Estructuras de datos
     * Estructuras de control
     * Funciones
     * Manejo de excepciones

---

## 🧪 ¿Cómo se evaluarán tus habilidades?

Deberás completar una serie de retos prácticos. Cada reto evalúa aspectos específicos de los temas mencionados.

Cada reto incluye:

* 📄 **Enunciado del reto**: descripción del problema a resolver
* 🧮 **Ejemplos de entrada y salida**: para guiarte en la lógica esperada
* 🚫 **Restricciones**: condiciones que debes respetar al resolverlo

## 📝 Puntuación de los retos

La puntuación de los retos es la siguiente:

* **Git y GitHub**: 4 puntos
* **Estructura de Carpetas y Archivos**: 6 puntos
* **Markdown**: 2 puntos
* **Tipos de Datos en Python**: 3 puntos
* **Estructuras de Datos en Python**: 4 puntos
* **Estructuras de Control en Python**: 3 puntos
* **Funciones en Python**: 3 puntos
* **Manejo de Excepciones en Python**: 1 punto
* **Total**: 26 puntos

Para aprobar los retos debes haber resuelto exitosamente el **80%** de los retos, lo que equivale a **21 puntos**.

## 📅 Fechas importantes

* **Apertura del formulario de postulación**: 22 de Agosto del 2025
* **Cierre del formulario de postulación**: 06 de Septiembre del 2025

---

## 🚀 Instrucciones de entrega

* Una vez que hayas completado todos los retos deberás ingresar la pagina de postulación de Python Study Group OOP y enviar el enlace a tu repositorio de GitHub en el formulario de postulación.
* El formulario de postulación estará abierta hasta las **23:00 (GMT-04) del 06 de septiembre del 2025**.
* Si tienes alguna duda puede escribirnos al correo electrónico **<hello@pylapaz.org>**.

---

## 🧩 Retos

Lee atentamente cada enunciado y respeta la estructura de carpetas y archivos solicitada. Recuerda que cada reto tiene restricciones específicas que debes cumplir.

### Git y GitHub - 4 puntos

* **Reto 01:** Realiza un **Fork** de este repositorio a tu cuenta personal de GitHub.

* **Reto 02:** Clona tu repositorio (resultado del fork) en tu máquina local.

* **Reto 03:** Crea una nueva rama con el siguiente formato: `tu-usuario-de-github`

* **Reto 04:** Una vez que hayas completado todos los retos, publica esta rama en tu repositorio personal.

📌 **Importante**

* Todas tus soluciones a los retos deben estar en la rama que creaste en esta sección.
* Debes realizar los commits de cada retos para dar seguimiento a tu progreso y evitar contratiempos.

---

### Estructura de Carpetas y Archivos - 6 puntos

#### Reto 05

Crea la siguiente estructura de carpetas y archivos para organizar los retos:

``` bash
retos_01/
    ejercicio_01.md
    ejercicio_02.md
retos_02/
    ejercicio_01.py
    ejercicio_02.py
    ejercicio_03.py
retos_03/
    ejercicio_04.py
    ejercicio_05.py
    ejercicio_06.py
    ejercicio_07.py
retos_04/
    ejercicio_08.py
    ejercicio_09.py
    ejercicio_10.py
retos_05/
    ejercicio_11.py
    ejercicio_12.py
    ejercicio_13.py
retos_06/
    ejercicio_14.py
```

---

### Markdown (retos\_01) - 2 puntos

#### Reto 06 - `ejercicio_01.md`

Utilizando Markdown escribe tu **biografía** incluyendo los siguientes elementos:

* Encabezados
* Negritas
* Cursivas
* Listas numeradas y no numeradas
* Imágenes

#### Reto 07 - `ejercicio_02.md`

Utilizando Markdown resume tu **libro favorito** incluyendo los siguientes elementos:

* Encabezados
* Listas numeradas y no numeradas
* Enlaces
* Imágenes
* Citas

---

### Tipos de Datos en Python (retos\_02) - 3 puntos

#### Reto 08 -  `ejercicio_01.py`

Crea un programa que reciba dos números enteros por teclado y retorne la suma, resta, multiplicación y división de ambos números.

**📥 Ejemplo de entrada:**

``` bash
10
5
```

**🖥️ Ejemplo de salida:**

``` bash
Suma: 15
Resta: 5
Multiplicación: 50
División: 2.0
```

🚫 **Restricciones**:

* No puedes usar estructuras de control (`if`, `for`, `while`)
* No puedes definir funciones (`def`, `lambda`)
* No puedes usar f-strings (`f""`, `format()`, `%`)
* No puedes utilizar excepciones (`try`, `except`)

#### Reto 09 -  `ejercicio_02.py`

Un jardín cuenta con un sistema de riego automático que se activa cuando hay luz solar o cuando la humedad del suelo es menor al 30%, pero no debe activarse si ambas condiciones se cumplen al mismo tiempo. Crea un programa que reciba un valor booleano `luz_solar` y un valor entero `humedad` (0-100) y retorne si el sistema de riego debe activarse o no.

**📥 Ejemplo de entrada:**

``` bash
True
25

False
20
```

**🖥️ Ejemplo de salida:**

``` bash
El sistema de riego no se activa.
El sistema de riego se activa.
```

🚫 **Restricciones**:

* Solo puedes utilizar operadores lógicos: `and`, `or`, `not`
* No puedes usar estructuras de control (`if`, `for`, `while`)
* No puedes definir funciones (`def`, `lambda`)
* No puedes usar f-strings (`f""`, `format()`, `%`)
* No puedes utilizar excepciones (`try`, `except`)

#### Reto 10 -  `ejercicio_03.py`

Crea un programa que reciba una frase y retorne:

* La cantidad de palabras que contiene
* La cantidad de vocales que contiene
* Y si la frase es un palíndromo o no

**📥 Ejemplo de entrada:**

``` bash
Anita lava la tina
```

**🖥️ Ejemplo de salida:**

``` bash
Cantidad de palabras: 5
Cantidad de vocales: 7
Es palíndromo: True
```

🚫 **Restricciones**:

* No puedes usar estructuras de control (`if`, `for`, `while`)
* No puedes definir funciones (`def`, `lambda`)
* No puedes utilizar `map`, `filter` o `reduce`
* No puedes utilizar excepciones (`try`, `except`)

### Estructuras de datos en Python (retos\_03) - 4 puntos

#### Reto 11 -  `ejercicio_04.py`

Tienes un catalogo de libros en la siguiente estructura de datos, donde cada linea representa un libro con su ISBN, título, autor y año de publicación:

``` bash
(
    ("978-3-16-148410-0", "EL QUIJOTE", "Miguel de Cervantes", 1605),
    ("978-0-14-044913-6", "LA ODISEA", "Homero", -800),
    ("978-0-452-28423-4", "1984", "George Orwell", 1949),
    ("978-0-7432-7356-5", "EL GRAN GATSBY", "F. Scott Fitzgerald", 1925)
)
```

Un usuario ingresa por teclado el ISBN de un libro y debes retornar el título en formato `Title Case`, autor y año de publicación. Si el libro no existe, retorna "Libro no encontrado".

**📥 Ejemplo de entrada:**

``` bash
978-0-14-044913-6
978-1-56619-909-4
```

**🖥️ Ejemplo de salida:**

``` bash
Título: La Odisea, Autor: Homero, Año: -800
Libro no encontrado.
```

🚫 **Restricciones**:

* No puedes usar estructuras de control (`if`, `for`, `while`)
* No puedes definir funciones (`def`, `lambda`)
* No puedes utilizar las funciones `map`, `filter` o `reduce`
* No puedes utilizar excepciones (`try`, `except`)

#### Reto 12 -  `ejercicio_05.py`

Crea un programa que reciba una lista de productos y una lista de precios y retorne:

* El total de la compra
* El producto mas caro
* El producto mas barato
* La lista de productos ordenados por precio de menor a mayor

**📥 Ejemplo de entrada:**

``` bash
Pan, Leche, Queso, Galletas
5.49, 3.99, 7.89, 2.49
```

**🖥️ Ejemplo de salida:**

``` bash
Total de la compra: 19.76
Producto más caro: Queso
Producto más barato: Galletas
Productos ordenados por precio: Galletas, Leche, Pan, Queso
```

🚫 **Restricciones**:

* No puedes usar estructuras de control (`if`, `for`, `while`)
* No puedes definir funciones (`def`, `lambda`)
* No puedes utilizar las funciones `map`, `filter` o `reduce`
* No puedes utilizar excepciones (`try`, `except`)

#### Reto 13 -  `ejercicio_06.py`

Jose y Carlos utilizan Spotipy para escuchar música. Cada uno tiene su propia lista de reproducción con sus canciones favoritas.

Jose quiere saber qué canciones tienen en común con Carlos y cuáles son exclusivas de cada uno.

Si su cantidad de canciones en común es mayor al 50% de sus canciones totales, entonces son "Almas Gemelas Musicales", de lo contrario son "Amigos con Buen Gusto".

Crea un programa que reciba dos listas de canciones (una para cada usuario) y retorne:

* Las canciones en común
* Las canciones exclusivas de Jose
* Las canciones exclusivas de Carlos
* Si son "Almas Gemelas Musicales" o "Amigos con Buen Gusto"

**📥 Ejemplo de entrada:**

``` bash
Shape of You, Blinding Lights, Levitating, Peaches
Blinding Lights, Save Your Tears, Peaches, Drivers License
```

**🖥️ Ejemplo de salida:**

``` bash
Canciones en común: Blinding Lights, Peaches
Canciones exclusivas de Jose: Shape of You, Levitating
Canciones exclusivas de Carlos: Save Your Tears, Drivers License
Son Amigos con Buen Gusto.
```

🚫 **Restricciones**:

* No puedes usar estructuras de control (`if`, `for`, `while`)
* No puedes definir funciones (`def`, `lambda`)
* No puedes utilizar las funciones `map`, `filter` o `reduce`
* No puedes utilizar excepciones (`try`, `except`)

#### Reto 14 -  `ejercicio_07.py`

Una farmacia almacena los medicamentos de su stock en la siguiente estructura de datos:

``` bash
{
    "Aspirina": {"cantidad": 50, "precio": 10.99},
    "Ibuprofeno": {"cantidad": 30, "precio": 15.49},
    "Paracetamol": {"cantidad": 20, "precio": 8.99},
    "Amoxicilina": {"cantidad": 10, "precio": 25.00}
}
```

Un cliente quiere comprar un medicamento y el programa debe verificar si hay suficiente cantidad en stock. Si hay suficiente, debe calcular el total de la compra y actualizar el stock. Si no hay suficiente, debe retornar "No hay suficiente stock".Si un medicamento no existe, debe retornar "Medicamento no encontrado".

**📥 Ejemplo de entrada:**

``` bash
Aspirina, 20
Ibuprofeno, 40
Diclofenaco, 5
```

**🖥️ Ejemplo de salida:**

``` bash
Total de la compra: 219.80
No hay suficiente stock.
Medicamento no encontrado.
```

🚫 **Restricciones**:

* No puedes usar estructuras de control (`if`, `for`, `while`)
* No puedes definir funciones (`def`, `lambda`)
* No puedes utilizar las funciones `map`, `filter` o `reduce`
* No puedes utilizar excepciones (`try`, `except`)

### Estructuras de control en Python (retos\_04) - 3 puntos

#### Reto 15 -  `ejercicio_08.py`

Tienes un sistema de semáforos que controla el tráfico de una ciudad mediante un programa que recibe información de tres sensores. El primer sensor envía un valor entero de 0 a 100 que representa la cantidad de vehículos frente a él. El segundo sensor envía una cadena de guiones `-` que representa la cantidad de peatones esperando para cruzar. El tercer sensor envía un valor entero que indica si hay una emergencia `1` o no `0`.

El programa debe determinar el estado del semáforo (Verde, Amarillo, Rojo) según las siguientes reglas:

* Si hay una emergencia, el semáforo debe estar en Verde.
* Si no hay emergencia y la cantidad de vehículos es mayor a 70, el semáforo debe estar en Verde.
* Si no hay emergencia y la cantidad de vehículos es menor o igual a 70, el semáforo debe estar en Amarillo.
* Si no hay emergencia y hay más de 5 peatones esperando, el semáforo debe estar en Rojo.

**📥 Ejemplo de entrada:**

``` bash
80, ----, False
20,, True
50, --, False
50 , -----, False
```

**🖥️ Ejemplo de salida:**

``` bash
Semáforo: Verde
Semáforo: Verde
Semáforo: Amarillo
Semáforo: Rojo
```

🚫 **Restricciones**:

* Utiliza el valor de Truthiness para los tipos de datos en Python.
* No puedes usar estructuras de control (`for`, `while`)
* No puedes definir funciones (`def`, `lambda`)
* No puedes utilizar las funciones `map`, `filter` o `reduce`
* No puedes utilizar excepciones (`try`, `except`)

#### Reto 16 -  `ejercicio_09.py`

Un analista de textos quiere encontrar las palabras más frecuentes de un texto, pero quiere evitar palabras sin contenido como `el`, `o`, `y`, `pero`, etc. Crea un programa que reciba un texto y retorne una lista con las 3 palabras más frecuentes, excluyendo las palabras sin contenido.

Utiliza la siguiente lista de palabras sin contenido:

``` python
palabras_sin_contenido = [
    "el", "la", "los", "las", "de", "y", "a", "en", "o", "que",
    "pero", "con", "por", "para", "un", "una", "es", "son",
    "se", "del", "al", "lo"
]
```

**📥 Ejemplo de entrada:**

``` bash
El gato y el perro son amigos. El gato es muy juguetón y el perro es tranquilo. Ambos son amigos.
```

**🖥️ Ejemplo de salida:**

``` bash
['gato', 'perro', 'amigos']
```

🚫 **Restricciones**:

* No puedes definir funciones (`def`, `lambda`)
* No puedes utilizar las funciones `map`, `filter` o `reduce`
* No puedes utilizar excepciones (`try`, `except`)

#### Reto 17 -  `ejercicio_10.py`

Una cinta transportadora clasifica manzanas y las va empacando en cajas según su color. En cada caja se empacan 12 manzanas. La cinta tiene un sensor que detecta el color de cada manzana y envía una cadena con el color de la manzana `r` para las rojas y `v` para las verdes. Si el sensor detecta una manzana con plagas envía un `p`. El programa se detiene cuando el sensor envía "empacar" y devuelve la cantidad de cajas empacadas para cada color y cuantas manzanas con plagas se detectaron.

**📥 Ejemplo de entrada:**

``` bash
rvrvrvrpvvrrv
rrvvvppp
ppprrrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvr
empacar
```

**🖥️ Ejemplo de salida:**

``` bash
Cajas empacadas para Rojas: 2
Cajas empacadas para Verdes: 2
Cajas empacadas para Plagas: 7
```

🚫 **Restricciones**:

* No puedes definir funciones (`def`, `lambda`)
* No puedes utilizar las funciones `map`, `filter` o `reduce`
* No puedes utilizar excepciones (`try`, `except`)

### Funciones en Python (retos\_05) - 3 puntos

#### Reto 18 -  `ejercicio_11.py`

Crea una función que reciba un número entero, retorne su factorial y su doble.

El factorial de un número `n` es el producto de todos los números enteros desde `1` hasta `n`. Por ejemplo, el factorial de `5` es `5 * 4 * 3 * 2 * 1 = 120`.

**📥 Ejemplo de entrada:**

``` bash
1
5
12
```

**🖥️ Ejemplo de salida:**

``` bash
Factorial: 1, Doble: 2
Factorial: 120, Doble: 240
Factorial: 479001600, Doble: 958003200
```

🚫 **Restricciones**:

* No puedes utilizar las funciones `map`, `filter` o `reduce`
* No puedes utilizar excepciones (`try`, `except`)

#### Reto 19 -  `ejercicio_12.py`

Un pastelero necesita estandarizar el formato de sus recetas. Para empezar necesita estandarizar los ingredientes. Para lograrlo debes crear una función que reciba como argumentos los ingredientes de una receta y retorne la lista de ingredientes estandarizada en el siguiente formato:

``` markdown
Ingredientes
------------
* Harina 2 tazas
* Azúcar 1 taza
* Huevo 3 unidades
* Chocolate 100 gramos
```

Usa el siguiente diccionario de equivalencias para estandarizar las unidades:

``` python
equivalencias = {
    "tz": "tazas",
    "cda": "cucharadas",
    "l": "litros",
    "gr": "gramos",
    "kg": "kilogramos",
    "u": "unidades"
}
```

Las recetas **no** tienen los mismos ingrediente, por ejemplo una receta de pastel de chocolate tiene ingredientes como `harina`, `azúcar`, `huevo`, `chocolate`, mientras que una receta del flan de vanilla tiene ingredientes como `leche`, `azúcar`, `huevo`, `vainilla`.

**📥 Ejemplo de entrada:**

``` bash
harina=2tz, azúcar=1tz, huevo=3u, chocolate=100gr
leche=1l, azúcar=1tz, huevo=4u, vainilla=1cda
```

**🖥️ Ejemplo de salida:**

``` bash
Ingredientes
------------
* Harina 2 tazas
* Azúcar 1 taza
* Huevo 3 unidades
* Chocolate 100 gramos

Ingredientes
------------
* Leche 1 litro
* Azúcar 1 taza
* Huevo 4 unidades
* Vainilla 1 cucharada
```

🚫 **Restricciones**:

* No puedes usar argumentos por defecto.
* No puedes utilizar las funciones `map`, `filter` o `reduce`
* No puedes utilizar excepciones (`try`, `except`)

#### Reto 20 -  `ejercicio_13.py`

Crea una función anónima que reciba una frase y devuelva las palabras ordenadas alfabéticamente, sin repetir palabras y en minúsculas.

**📥 Ejemplo de entrada:**

``` bash
Las orugas comen hojas, los pájaros comen orugas y los gatos comen pájaros.
```

**🖥️ Ejemplo de salida:**

``` bash
['comen', 'gatos', 'hojas', 'las', 'los', 'orugas', 'pájaros']
```

🚫 **Restricciones**:

* No puedes utilizar las funciones `map`, `filter` o `reduce`
* No puedes utilizar excepciones (`try`, `except`)

### Manejo de Excepciones en Python (retos\_06) - 1 punto

#### Reto 21 -  `ejercicio_14.py`

Crea una calculador interactiva que permita calcular la suma `+`, resta `-`, multiplicación `*` y division `/` de dos numero que pueden ser enteros o flotantes.

Las operaciones que se ingresan tienen el formato `numero1, numero2, operador` hasta que el usuario ingrese "salir".

La calculadora debe manejar las siguientes excepciones:

* `ValueError`: Si el usuario ingresa valores no válidos.
* `ZeroDivisionError`: Si se intenta dividir por cero.
* `IndexError`: Si el usuario no ingresa todos los elementos necesarios para realizar la operación.

**📥 Ejemplo de entrada:**

``` bash
10, 5, +
20.2, 10.1
30, 0.5, a 
40, 0, /
abc, 5, +
```

**🖥️ Ejemplo de salida:**

``` bash
15.0
No hay suficientes elementos para realizar la operación.
Operación no valida.
No se puede dividir por cero.
Operación no valida.
Operación no valida.
```

🚫 **Restricciones**:

* No puedes utilizar las funciones `map`, `filter` o `reduce`

----

## 📝 Contribuidores

<a href="https://github.com/python-la-paz/psg-retos/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=python-la-paz/psg-retos" />
</a>

### Con mucho ❤️ Python La Paz 🐍

[![Pagina Web](https://img.shields.io/badge/Web-Python%20La%20Paz-blue.svg)](https://pylapaz.org/)
[![Comunidad WhatsApp](https://img.shields.io/badge/Comunidad-WhatsApp-green.svg)](https://chat.whatsapp.com/JmcjxMqqH5NDmh5APFWahM)
[![Comunidad en Discord](https://img.shields.io/badge/Comunidad-Discord-blue.svg)](https://discord.gg/TV5tHvdUKt)

[![Facebook](https://img.shields.io/badge/Facebook-Python%20La%20Paz-blue.svg)](https://www.facebook.com/PythonLaPaz)
[![Twitter](https://img.shields.io/badge/Twitter-Python%20La%20Paz-blue.svg)](https://twitter.com/PythonLaPaz)
[![Instagram](https://img.shields.io/badge/Instagram-Python%20La%20Paz-blue.svg)](https://instagram.com/pythonlapaz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Python%20La%20Paz-blue.svg)](https://www.linkedin.com/company/python-la-paz/)
