catalogo = (
    ("978-3-16-148410-0", "EL QUIJOTE", "Miguel de Cervantes", 1605),
    ("978-0-14-044913-6", "LA ODISEA", "Homero", -800),
    ("978-0-452-28423-4", "1984", "George Orwell", 1949),
    ("978-0-7432-7356-5", "EL GRAN GATSBY", "F. Scott Fitzgerald", 1925)
)

isbn_busqueda = input("Introducir el codigo ISBN del libro: ").strip()

libro_1 = catalogo[0]
libro_2 = catalogo[1]
libro_3 = catalogo[2]
libro_4 = catalogo[3]

libros = {
        libro_1[0]: libro_1,
        libro_2[0]: libro_2,
        libro_3[0]: libro_3,
        libro_4[0]: libro_4
}

libro_encontrado = libros.get(isbn_busqueda)

resultado = (libro_encontrado and f"Titulo: {libro_encontrado[1].title()}, Autor:{libro_encontrado[2]}, Año: {libro_encontrado[3]}" or "Libro no encontrado") 
print(resultado)
