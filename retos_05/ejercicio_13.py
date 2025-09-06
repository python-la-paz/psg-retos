ordenar_palabras = lambda frase: sorted(set(
    palabra.strip(".").lower()
    for palabra in frase.split()
))

frase = input()
print(ordenar_palabras(frase))