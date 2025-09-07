# Reto 12 - ejercicio_05.py

# Crea un programa que reciba una lista de productos y una lista de precios y retorne:

#     El total de la compra
#     El producto mas caro
#     El producto mas barato
#     La lista de productos ordenados por precio de menor a mayor

# 📥 Ejemplo de entrada:

# Pan, Leche, Queso, Galletas
# 5.49, 3.99, 7.89, 2.49

# 🖥️ Ejemplo de salida:

# Total de la compra: 19.76
# Producto más caro: Queso
# Producto más barato: Galletas
# Productos ordenados por precio: Galletas, Leche, Pan, Queso

# 🚫 Restricciones:

#     No puedes usar estructuras de control (if, for, while)
#     No puedes definir funciones (def, lambda)
#     No puedes utilizar las funciones map, filter o reduce
#     No puedes utilizar excepciones (try, except)

#Entrada
productos = tuple(input().split(", ")) 
precios = eval("(" + input() + ")")    

catalogo = tuple(zip(precios, productos))  

total = sum(precios)
mas_caro = max(catalogo)[1]
mas_barato = min(catalogo)[1]
productos_ordenados = tuple(zip(*sorted(catalogo)))[1]

#Salida
print("Total de la compra:", round(total, 2))
print("Producto más caro:", mas_caro)
print("Producto más barato:", mas_barato)
print("Productos ordenados por precio:", ", ".join(productos_ordenados))




