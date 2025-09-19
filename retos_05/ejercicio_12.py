# Reto 19 - ejercicio_12.py

# Un pastelero necesita estandarizar el formato de sus recetas. Para empezar necesita estandarizar los ingredientes. 
# Para lograrlo debes crear una función que reciba como argumentos los ingredientes de una receta y retorne 
# la lista de ingredientes estandarizada en el siguiente formato:

# Ingredientes
# ------------
# * Harina 2 tazas
# * Azúcar 1 taza
# * Huevo 3 unidades
# * Chocolate 100 gramos

# Usa el siguiente diccionario de equivalencias para estandarizar las unidades:

# equivalencias = {
#     "tz": "tazas",
#     "cda": "cucharadas",
#     "l": "litros",
#     "gr": "gramos",
#     "kg": "kilogramos",
#     "u": "unidades"
# }

# Las recetas no tienen los mismos ingrediente, por ejemplo una receta de pastel de chocolate tiene ingredientes 
# como harina, azúcar, huevo, chocolate, mientras que una receta del flan de vanilla tiene ingredientes como leche, 
# azúcar, huevo, vainilla.

# 📥 Ejemplo de entrada:

# harina=2tz, azúcar=1tz, huevo=3u, chocolate=100gr
# leche=1l, azúcar=1tz, huevo=4u, vainilla=1cda

# 🖥️ Ejemplo de salida:

# Ingredientes
# ------------
# * Harina 2 tazas
# * Azúcar 1 taza
# * Huevo 3 unidades
# * Chocolate 100 gramos

# Ingredientes
# ------------
# * Leche 1 litro
# * Azúcar 1 taza
# * Huevo 4 unidades
# * Vainilla 1 cucharada

# 🚫 Restricciones:

#     No puedes usar argumentos por defecto.
#     No puedes utilizar las funciones map, filter o reduce
#     No puedes utilizar excepciones (try, except)

equivalencias = {
    "tz": ("taza", "tazas"),
    "cda": ("cucharada", "cucharadas"),
    "l": ("litro", "litros"),
    "gr": ("gramo", "gramos"),
    "kg": ("kilogramo", "kilogramos"),
    "u": ("unidad", "unidades")
}

def estandarizar_receta(cadena):
    
    ingredientes = cadena.split(",")
    
    resultado = []
    for item in ingredientes:
        item = item.strip()
        nombre, cantidad = item.split("=")
        nombre = nombre.strip().capitalize()
        numero = ""
        unidad = ""
        for c in cantidad:
            if c.isdigit():
                numero += c
            else:
                unidad += c
        unidad = unidad.strip().lower()

        if unidad in equivalencias:
            singular, plural = equivalencias[unidad]
            if numero == "1":
                unidad_pl = singular
            else:
                unidad_pl = plural
        else:
            unidad_pl = unidad  

        resultado.append("* " + nombre + " " + numero + " " + unidad_pl)

    bloque = "Ingredientes\n------------\n" + "\n".join(resultado)
    return bloque


entrada = input().strip()
print(estandarizar_receta(entrada))


