# # Reto 11 - ejercicio_04.py
# Tienes un catalogo de libros en la siguiente estructura de datos, donde cada linea representa un libro con su ISBN, título, autor y año de publicación:

# (
#     ("978-3-16-148410-0", "EL QUIJOTE", "Miguel de Cervantes", 1605),
#     ("978-0-14-044913-6", "LA ODISEA", "Homero", -800),
#     ("978-0-452-28423-4", "1984", "George Orwell", 1949),
#     ("978-0-7432-7356-5", "EL GRAN GATSBY", "F. Scott Fitzgerald", 1925)
# )

# Un usuario ingresa por teclado el ISBN de un libro y debes retornar el título en formato Title Case, autor y año de publicación. Si el libro no existe, retorna "Libro no encontrado".

# 📥 Ejemplo de entrada:

# 978-0-14-044913-6
# 978-1-56619-909-4

# 🖥️ Ejemplo de salida:

# Título: La Odisea, Autor: Homero, Año: -800
# Libro no encontrado.

# 🚫 Restricciones:

#     No puedes usar estructuras de control (if, for, while)
#     No puedes definir funciones (def, lambda)
#     No puedes utilizar las funciones map, filter o reduce
#     No puedes utilizar excepciones (try, except)

catalogo = {
    "978-3-16-148410-0": ("El Quijote", "Miguel de Cervantes", 1605),
    "978-0-14-044913-6": ("La Odisea", "Homero", -800),
    "978-0-452-28423-4": ("1984", "George Orwell", 1949),
    "978-0-7432-7356-5": ("El Gran Gatsby", "F. Scott Fitzgerald", 1925)
}

# Entrada
isbn = input()

resultado = catalogo.get(isbn)

# Salida
print(
    resultado and ("Título: " + resultado[0] + ", Autor: " + resultado[1] + ", Año: " + str(resultado[2]))
    or "Libro no encontrado."
)





