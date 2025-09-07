# Reto 20 - ejercicio_13.py

# Crea una función anónima que reciba una frase y devuelva las palabras ordenadas alfabéticamente, 
# sin repetir palabras y en minúsculas.

# 📥 Ejemplo de entrada:

# Las orugas comen hojas, los pájaros comen orugas y los gatos comen pájaros.

# 🖥️ Ejemplo de salida:

# ['comen', 'gatos', 'hojas', 'las', 'los', 'orugas', 'pájaros']

# 🚫 Restricciones:

#     No puedes utilizar las funciones map, filter o reduce
#     No puedes utilizar excepciones (try, except)

procesar = lambda frase: sorted(list(set(frase.lower()
                                         .replace(",", "")
                                         .replace(".", "")
                                         .split())))

entrada = input().strip()

print(procesar(entrada))
