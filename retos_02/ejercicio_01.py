# Reto 08 - ejercicio_01.py

# Crea un programa que reciba dos números enteros por teclado y retorne 
# la suma, resta, multiplicación y división de ambos números.

# 📥 Ejemplo de entrada:

# 10
# 5

# 🖥️ Ejemplo de salida:

# Suma: 15
# Resta: 5
# Multiplicación: 50
# División: 2.0

# 🚫 Restricciones:

#     No puedes usar estructuras de control (if, for, while)
#     No puedes definir funciones (def, lambda)
#     No puedes usar f-strings (f"", format(), %)
#     No puedes utilizar excepciones (try, except)



# Entrada de datos

a = int(input())
b = int(input())


# Operaciones
suma = a + b
resta = a - b
multiplicacion = a * b
# division = a / b
division = (b and a / b) or "no se puede dividir entre 0"


# # Salida
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)