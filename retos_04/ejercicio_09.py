palabras_sin_contenido = [
    "el", "la", "los", "las", "de", "y", "a", "en", "o", "que",
    "pero", "con", "por", "para", "un", "una", "es", "son",
    "se", "del", "al", "lo"
]

texto = input("Ingresa un texto: ")

palabras = texto.lower().replace(".", "").replace(",", "").split()

frecuencias = {}
for palabra in palabras:
    if palabra not in palabras_sin_contenido:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

palabras_ordenadas = sorted(frecuencias, key=lambda x: frecuencias[x], reverse=True)

resultado = palabras_ordenadas[:3]

print(resultado)
