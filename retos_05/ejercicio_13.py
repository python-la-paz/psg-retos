frase = input().lower()
for simbolo in ".,;:!?":
    frase = frase.replace(simbolo, "")
palabras = frase.split()
palabras_unicas = []
for palabra in palabras:
    if palabra not in palabras_unicas:
        palabras_unicas.append(palabra)
palabras_unicas.sort()
print(palabras_unicas)

