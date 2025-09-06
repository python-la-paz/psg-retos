stock = {
    "Aspirina": {"cantidad": 50, "precio": 10.99},
    "Ibuprofeno": {"cantidad": 30, "precio": 15.49},
    "Paracetamol": {"cantidad": 20, "precio": 8.99},
    "Amoxicilina": {"cantidad": 10, "precio": 25.00}
}

med, cant = input().split(", ")
cant = int(cant)

item = stock.get(med)

print(
    (not item and "Medicamento no encontrado.") or
    (item and (item["cantidad"] < cant) and "No hay suficiente stock.") or
    (item and (item["cantidad"] >= cant) and (
        "Total de la compra: " + str(round(cant * item["precio"], 2))
    ))
)
