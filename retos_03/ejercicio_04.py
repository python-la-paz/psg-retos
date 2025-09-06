## 3. 

catalogo_de_libros=(
    ("978-3-16-148410-0", "EL QUIJOTE", "Miguel de Cervantes", 1605),
    ("978-0-14-044913-6", "LA ODISEA", "Homero", -800),
    ("978-0-452-28423-4", "1984", "George Orwell", 1949),
    ("978-0-7432-7356-5", "EL GRAN GATSBY", "F. Scott Fitzgerald", 1925)
)
busqueda_de_libros={}
#--
isbn_usr=input("ISBN: ")
#--
busqueda_de_libros[catalogo_de_libros[0][0]]=[catalogo_de_libros[0][1],catalogo_de_libros[0][2],catalogo_de_libros[0][3]]
busqueda_de_libros[catalogo_de_libros[1][0]]=[catalogo_de_libros[1][1],catalogo_de_libros[1][2],catalogo_de_libros[1][3]]
busqueda_de_libros[catalogo_de_libros[2][0]]=[catalogo_de_libros[2][1],catalogo_de_libros[2][2],catalogo_de_libros[2][3]]
busqueda_de_libros[catalogo_de_libros[3][0]]=[catalogo_de_libros[3][1],catalogo_de_libros[3][2],catalogo_de_libros[3][3]]
#--
libro = busqueda_de_libros.get(isbn_usr)
#--
print((libro and "Título: "+libro[0]+", Autor: "+libro[1]+", Año: "+str(libro[2])) or "Libro no encontrado.")