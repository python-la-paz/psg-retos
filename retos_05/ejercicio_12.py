equivalencias = {
    "tz": "tazas",
    "cda": "cucharadas",
    "l": "litros",
    "gr": "gramos",
    "kg": "kilogramos",
    "u": "unidades"
}

linea = input()
print("Ingredientes")
print("------------")
ingredientes = linea.split(", ")
for ing in ingredientes:
    nombre, cantidad = ing.split("=")
    numero = ""
    unidad = ""
    for c in cantidad:
        if c in "1234567890":
            numero += c
        else:
            unidad += c
    unidad_estandar = equivalencias.get(unidad, unidad)
    print("*", nombre.capitalize(), numero, unidad_estandar)
