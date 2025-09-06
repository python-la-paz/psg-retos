stock = {
    "Aspirina": {"cantidad": 50, "precio": 10.99},
    "Ibuprofeno": {"cantidad": 30, "precio": 15.49},
    "Paracetamol": {"cantidad": 20, "precio": 8.99},
    "Amoxicilina": {"cantidad": 10, "precio": 25.00}
}

pedido = input()

medicamento = pedido.split(", ")[0]
cantidad = int(pedido.split(", ")[1])

existe = medicamento in stock
suficiente = existe and stock[medicamento]["cantidad"] >= cantidad

mensaje = (
    "Medicamento no encontrado.",
    ("No hay suficiente stock.",
     f"Total de la compra: {stock[medicamento]['precio']*cantidad:.2f}")[suficiente]
)[existe]

suficiente and stock.update({medicamento: {"cantidad": stock[medicamento]["cantidad"] - cantidad, "precio": stock[medicamento]["precio"]}})

print(mensaje)
