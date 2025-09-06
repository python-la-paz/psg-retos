equivalencias = {
    "tz": "tazas",
    "cda": "cucharadas",
    "l": "litros",
    "gr": "gramos",
    "kg": "kilogramos",
    "u": "unidades"
}

def estandarizar_ingredientes(ingredientes: list):
    salida = "Ingredientes\n------------"
    for nombre, cantidad, unidad in ingredientes:
        unidad_estandar = equivalencias.get(unidad, unidad)
        salida += f"\n* {nombre.capitalize()} {cantidad} {unidad_estandar}"
    return salida

receta = input()

ingredientes_lista = receta.split(", ")

ingredientes = []
for ingrediente in ingredientes_lista:
    partes = ingrediente.split("=")
    nombre = partes[0]
    cantidad = "".join([c for c in partes[1] if c.isdigit()])
    unidad = "".join([c for c in partes[1] if c.isalpha()])
    ingredientes.append((nombre, cantidad, unidad))

print(estandarizar_ingredientes(ingredientes))