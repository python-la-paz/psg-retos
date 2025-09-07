stock = {
    "Aspirina": {"cantidad": 50, "precio": 10.99},
    "Ibuprofeno": {"cantidad": 30, "precio": 15.49},
    "Paracetamol": {"cantidad": 20, "precio": 8.99},
    "Amoxicilina": {"cantidad": 10, "precio": 25.00}
}

compras = [
    ("Aspirina",20),
    ("Ibuprofeno",40),
    ("Diclofenaco",5)
]

med, cant = compras [0]
resultado = med not in stock and "Medicamentos no encontrado" or stock[med]["cantidad"]< cant and "No hay suficiente stock" or stock[med]["precio"]*cant

stock[med]["cantidad"]= resultado != "Medicamentos no encontrado" and resultado != "No hay suficiente stock" and stock[med]["cantidad"] - cant or stock[med]["cantidad"]

print("Total de la compra:", resultado)

med, cant = compras[1]
resultado = med not in stock and "Medicamento no encontrado" or stock[med]["cantidad"]< cant and "No hay suficiente stock" or stock[med]["precio"]*cant
print(resultado)

med, cant = compras[2]
resultado = med not in stock and "Medicamento no encontrado" or stock[med]["cantidad"]< cant and "No hay suficiente stock" or stock[med]["precio"]*cant
print(resultado)
