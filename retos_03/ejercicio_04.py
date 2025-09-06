catalogo = (
    ("978-3-16-148410-0", "EL QUIJOTE", "Miguel de Cervantes", 1605),
    ("978-0-14-044913-6", "LA ODISEA", "Homero", -800),
    ("978-0-452-28423-4", "1984", "George Orwell", 1949),
    ("978-0-7432-7356-5", "EL GRAN GATSBY", "F. Scott Fitzgerald", 1925)
)

catalogo_dict = dict(
    zip(
        [catalogo[0][0], catalogo[1][0], catalogo[2][0], catalogo[3][0]],
        [
            ("Título: " + catalogo[0][1].title() + ", Autor: " + catalogo[0][2] + ", Año: " + str(catalogo[0][3])),
            ("Título: " + catalogo[1][1].title() + ", Autor: " + catalogo[1][2] + ", Año: " + str(catalogo[1][3])),
            ("Título: " + catalogo[2][1].title() + ", Autor: " + catalogo[2][2] + ", Año: " + str(catalogo[2][3])),
            ("Título: " + catalogo[3][1].title() + ", Autor: " + catalogo[3][2] + ", Año: " + str(catalogo[3][3]))
        ]
    )
)

isbn_input = input()

resultado = catalogo_dict.get(isbn_input, "Libro no encontrado")

print(resultado)
