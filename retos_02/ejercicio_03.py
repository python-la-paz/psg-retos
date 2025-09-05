frase = input().lower()
palabras = frase.split()
frase = frase.replace(" ", "").lower()
rev = frase[::-1]

vocales=(
    frase.count("a") + frase.count("e") + frase.count("i") + 
    frase.count("o") + frase.count("u")
       )
print("Cantidad de palabras:", len(palabras))
print("Cantidad de vocales:", vocales)
print("Es palíndromo:", (frase == rev))