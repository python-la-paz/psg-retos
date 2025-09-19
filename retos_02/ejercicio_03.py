# Reto 10 - ejercicio_03.py

# Crea un programa que reciba una frase y retorne:

#     La cantidad de palabras que contiene
#     La cantidad de vocales que contiene
#     Y si la frase es un palíndromo o no

# 📥 Ejemplo de entrada:

# Anita lava la tina

# 🖥️ Ejemplo de salida:

# Cantidad de palabras: 4
# Cantidad de vocales: 8
# Es palíndromo: True

# 🚫 Restricciones:

#     No puedes usar estructuras de control (if, for, while)
#     No puedes definir funciones (def, lambda)
#     No puedes utilizar map, filter o reduce
#     No puedes utilizar excepciones (try, except)


# Entrada
frase = input()

cantidad_palabras = len(frase.split())

cantidad_vocales = (
    frase.lower().count("a") +
    frase.lower().count("e") +
    frase.lower().count("i") +
    frase.lower().count("o") +
    frase.lower().count("u")
)

frase_limpia = "".join(frase.lower().split())
es_palindromo = frase_limpia == frase_limpia[::-1]

# Salida
print("Cantidad de palabras:", cantidad_palabras)
print("Cantidad de vocales:", cantidad_vocales)
print("Es palíndromo:", es_palindromo)
