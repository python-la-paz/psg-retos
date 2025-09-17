frase = input("Ingresa una frasse: ")

palabras = frase.split()
cantidad_palabras = len(palabras)

frase_minusculas = frase.lower()

cantidad_vocales = frase_minusculas.count('a') + frase_minusculas.count('e') + frase_minusculas.count('i') + frase_minusculas.count('o') + frase_minusculas.count('u')

frase_ordenado = frase.replace(" ","").lower()
palindromo = frase_ordenado == frase_ordenado[::-1]

print("Cantidad de Palabras: ", cantidad_palabras)
print("Cantidad de vocales: ", cantidad_vocales)
print("Es palíndromo:",palindromo)