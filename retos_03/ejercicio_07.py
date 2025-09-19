# Reto 14 - ejercicio_07.py

# Una farmacia almacena los medicamentos de su stock en la siguiente estructura de datos:

# {
#     "Aspirina": {"cantidad": 50, "precio": 10.99},
#     "Ibuprofeno": {"cantidad": 30, "precio": 15.49},
#     "Paracetamol": {"cantidad": 20, "precio": 8.99},
#     "Amoxicilina": {"cantidad": 10, "precio": 25.00}
# }

# Un cliente quiere comprar un medicamento y el programa debe verificar si hay suficiente cantidad en stock. Si hay suficiente, debe calcular el total de la compra y actualizar el stock. Si no hay suficiente, debe retornar "No hay suficiente stock".Si un medicamento no existe, debe retornar "Medicamento no encontrado".

# 📥 Ejemplo de entrada:

# Aspirina, 20
# Ibuprofeno, 40
# Diclofenaco, 5

# 🖥️ Ejemplo de salida:

# Total de la compra: 219.80
# No hay suficiente stock.
# Medicamento no encontrado.

# 🚫 Restricciones:

#     No puedes usar estructuras de control (if, for, while)
#     No puedes definir funciones (def, lambda)
#     No puedes utilizar las funciones map, filter o reduce
#     No puedes utilizar excepciones (try, except)


stock = {
    "Aspirina": {"cantidad": 50, "precio": 10.99},
    "Ibuprofeno": {"cantidad": 30, "precio": 15.49},
    "Paracetamol": {"cantidad": 20, "precio": 8.99},
    "Amoxicilina": {"cantidad": 10, "precio": 25.00}
}

# Entrada
entrada = input().split(", ")
medicamentos, cantidad = entrada[0], int(entrada[1])

datos = stock.get(medicamentos)

mensaje = (
    datos
    and (
        (datos["cantidad"] >= cantidad
         and (
             "Total de la compra: " + str(round(datos["precio"] * cantidad, 2))
             + (stock.update({
                medicamentos: {
                    "cantidad": datos["cantidad"] - cantidad, 
                    "precio": datos["precio"]
                    }
                }) or "")
         )
        )
        or "No hay suficiente stock."
    )
) or "Medicamento no encontrado."

# Salida
print(mensaje)



