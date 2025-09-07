# Reto 13 - ejercicio_06.py

# Jose y Carlos utilizan Spotipy para escuchar música. Cada uno tiene su propia lista de reproducción con sus canciones favoritas.

# Jose quiere saber qué canciones tienen en común con Carlos y cuáles son exclusivas de cada uno.

# Si su cantidad de canciones en común es mayor al 50% de sus canciones totales, entonces son "Almas Gemelas Musicales", de lo contrario son "Amigos con Buen Gusto".

# Crea un programa que reciba dos listas de canciones (una para cada usuario) y retorne:

#     Las canciones en común
#     Las canciones exclusivas de Jose
#     Las canciones exclusivas de Carlos
#     Si son "Almas Gemelas Musicales" o "Amigos con Buen Gusto"

# 📥 Ejemplo de entrada:

# Shape of You, Blinding Lights, Levitating, Peaches
# Blinding Lights, Save Your Tears, Peaches, Drivers License

# 🖥️ Ejemplo de salida:

# Canciones en común: Blinding Lights, Peaches
# Canciones exclusivas de Jose: Shape of You, Levitating
# Canciones exclusivas de Carlos: Save Your Tears, Drivers License
# Son Amigos con Buen Gusto.

# 🚫 Restricciones:

#     No puedes usar estructuras de control (if, for, while)
#     No puedes definir funciones (def, lambda)
#     No puedes utilizar las funciones map, filter o reduce
#     No puedes utilizar excepciones (try, except)


# Entrada
jose = input().split(", ")
carlos = input().split(", ")

set_jose = set(jose)
set_carlos = set(carlos)

comunes = tuple(set_jose & set_carlos)
exclusivas_jose = tuple(set_jose - set_carlos)
exclusivas_carlos = tuple(set_carlos - set_jose)

total_canciones = len(set_jose | set_carlos)
proporcion = len(comunes) / total_canciones


mensaje = (proporcion > 0.5 and "Son Almas Gemelas Musicales.") or "Son Amigos con Buen Gusto."

# Salida
print("Canciones en común:", ", ".join(comunes))
print("Canciones exclusivas de Jose:", ", ".join(exclusivas_jose))
print("Canciones exclusivas de Carlos:", ", ".join(exclusivas_carlos))
print(mensaje)








