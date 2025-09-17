texto = input()

palabras_sin_contenido = [
    "el", "la", "los", "las", "de", "y", "a", "en", "o", "que",
    "pero", "con", "por", "para", "un", "una", "es", "son",
    "se", "del", "al", "lo"
]

for simbolo in ".,;:!¿?¡":
    texto = texto.replace(simbolo, "")

palabras = (texto.lower()).split()

frecuencias = {}
for palabra in palabras:
    if palabra not in palabras_sin_contenido:
        if palabra not in frecuencias:
            frecuencias[palabra] = 0
        frecuencias[palabra] += 1

top3 = list(sorted(frecuencias, key=frecuencias.get))[-3:][::-1]

print(top3)
