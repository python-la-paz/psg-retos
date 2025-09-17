productos = input().split(", ")
precios = list(eval("[" + input() + "]"))

total = sum(precios)

caro = productos[precios.index(max(precios))]
barato = productos[precios.index(min(precios))]
ordenados = list(dict(sorted(zip(precios, productos))).values())

print("Total de la compra: " + str(round(total, 2)))
print("Producto más caro: " + caro)
print("Producto más barato: " + barato)
print("Productos ordenados por precio: " + ", ".join(ordenados))