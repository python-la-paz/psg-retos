## 7.
#--
almacen={
    "Aspirina": {"cantidad": 50, "precio": 10.99},
    "Ibuprofeno": {"cantidad": 30, "precio": 15.49},
    "Paracetamol": {"cantidad": 20, "precio": 8.99},
    "Amoxicilina": {"cantidad": 10, "precio": 25.00}
}
#--
medicamento_usr=input("Ingrese pedido (medicamento, cantidad): ").strip().split(", ")
medicamento_nombre=medicamento_usr[0].title()
medicamento_cantidad=float(medicamento_usr[1])
#---
existe_medicamento=medicamento_nombre in almacen
confirmacion_de_stock=existe_medicamento*int(almacen.get(medicamento_nombre, {}).get("cantidad", 0)>=medicamento_cantidad)
total=medicamento_cantidad*almacen.get(medicamento_nombre, {}).get("precio", 0)
#--
estado_de_compra=(("Medicamento no encontrado.",("")),(("No hay suficiente stock."),(f"Total de la compra: {total}")))
print(f"{estado_de_compra [existe_medicamento][confirmacion_de_stock]}")
