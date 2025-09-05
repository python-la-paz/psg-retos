libros = (
    ("978-3-16-148410-0", "EL QUIJOTE", "Miguel de Cervantes", 1605),
    ("978-0-14-044913-6", "LA ODISEA", "Homero", -800),
    ("978-0-452-28423-4", "1984", "George Orwell", 1949),
    ("978-0-7432-7356-5", "EL GRAN GATSBY", "F. Scott Fitzgerald", 1925)
)

catalogo = {
    "978-3-16-148410-0": ("EL QUIJOTE", "Miguel de Cervantes", 1605),
    "978-0-14-044913-6": ("LA ODISEA", "Homero", -800),
    "978-0-452-28423-4": ("1984", "George Orwell", 1949),
    "978-0-7432-7356-5": ("EL GRAN GATSBY", "F. Scott Fitzgerald", 1925)
}

isbn = input()

datos = catalogo.get(isbn)
print(
    (datos and "Título: " + datos[0].title() + ", Autor: " + datos[1] + ", Año: " + str(datos[2]))
    or "Libro no encontrado."
)
