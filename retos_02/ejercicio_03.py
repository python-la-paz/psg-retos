frase = input()

frase_lower = frase.lower()
arrayFrase =  frase_lower.split()
palabras = len(arrayFrase)

vocales = (
    frase_lower.count("a") +
    frase_lower.count("e") +
    frase_lower.count("i") +
    frase_lower.count("o") +
    frase_lower.count("u")
)

solo_letras = frase_lower.replace(" ", "")

palindromo = solo_letras == solo_letras[::-1]

print("Cantidad de palabras: " + str(palabras))
print("Cantidad de vocales: " + str(vocales))
print("Es palíndromo: " + str(palindromo))