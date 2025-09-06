productos = input()
precios = input()

productos = productos.split(", ")
precios = precios.split(", ")
precios = [float(precios[0]), float(precios[1]), float(precios[2]), float(precios[3])]

total = sum(precios)

indice_mas_caro = precios.index(max(precios))
indice_mas_barato = precios.index(min(precios))
producto_mas_caro = productos[indice_mas_caro]
producto_mas_barato = productos[indice_mas_barato]

combinado = list(zip(precios, productos))
combinado.sort()
precios_ordenados, productos_ordenados = zip(*combinado)

print("Total de la compra:", total)
print("Producto más caro:", producto_mas_caro)
print("Producto más barato:", producto_mas_barato)
print("Productos ordenados por precio:", ", ".join(productos_ordenados))
