palabras_sin_contenido = ["el", "la", "los", "las", "de", "y", "a", "en", "o", "que",
    "pero", "con", "por", "para", "un", "una", "es", "son",
    "se", "del", "al", "lo"]

texto = input("Ingrese el texto: ").strip().lower()

signos = ".,!?;:()"
for signo in signos:
    texto = texto.replace(signo, " ")

palabras = texto.split()

contador = {}
for palabra in palabras:
    if palabra not in palabras_sin_contenido:
        if palabra in contador:
            contador[palabra] = contador[palabra]+1
        else:
            contador[palabra] = 1
lista_frecuencias = []

for palabra in contador:
    frecuencia = contador[palabra]
    tupla = (frecuencia, palabra)
    lista_frecuencias.append(tupla)

lista_ordenada = sorted(lista_frecuencias, reverse=True)

resultado = []

for i in range(min(3, len(lista_ordenada))):
    resultado.append(lista_ordenada[i][1])

print(resultado)
