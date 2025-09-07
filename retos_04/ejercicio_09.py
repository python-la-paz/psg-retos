# Reto 16 - ejercicio_09.py

# Un analista de textos quiere encontrar las palabras más frecuentes de un texto, 
# pero quiere evitar palabras sin contenido como el, o, y, pero, etc. Crea un programa que reciba un texto y retorne una 
# lista con las 3 palabras más frecuentes, excluyendo las palabras sin contenido.

# Utiliza la siguiente lista de palabras sin contenido:

# palabras_sin_contenido = [
#     "el", "la", "los", "las", "de", "y", "a", "en", "o", "que",
#     "pero", "con", "por", "para", "un", "una", "es", "son",
#     "se", "del", "al", "lo"
# ]

# 📥 Ejemplo de entrada:

# El gato y el perro son amigos. El gato es muy juguetón y el perro es tranquilo. Ambos son amigos.

# 🖥️ Ejemplo de salida:

# ['gato', 'perro', 'amigos']

# 🚫 Restricciones:

#     No puedes definir funciones (def, lambda)
#     No puedes utilizar las funciones map, filter o reduce
#     No puedes utilizar excepciones (try, except)


# Lista de palabras sin contenido
palabras_sin_contenido = [
    "el", "la", "los", "las", "de", "y", "a", "en", "o", "que",
    "pero", "con", "por", "para", "un", "una", "es", "son",
    "se", "del", "al", "lo"
]

# Entrada
texto = input()

texto = texto.lower()
for signo in [".", ",", ";", ":", "!", "¡", "¿", "?", "(", ")", "\"", "'"]:
    texto = texto.replace(signo, "")

palabras = texto.split()

frecuencia = {}
for palabra in palabras:
    if palabra not in palabras_sin_contenido:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

frecuencia_items = []
for clave in frecuencia:
    frecuencia_items.append((clave, frecuencia[clave]))

for i in range(len(frecuencia_items)):
    for j in range(i + 1, len(frecuencia_items)):
        if frecuencia_items[j][1] > frecuencia_items[i][1]:
            frecuencia_items[i], frecuencia_items[j] = frecuencia_items[j], frecuencia_items[i]

resultado = []
for i in range(min(3, len(frecuencia_items))):
    resultado.append(frecuencia_items[i][0])
# Salida
print(resultado)





