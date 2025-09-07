# Reto 18 - ejercicio_11.py

# Crea una función que reciba un número entero, retorne su factorial y su doble.

# El factorial de un número n es el producto de todos los números enteros desde 1 hasta n. 
# Por ejemplo, el factorial de 5 es 5 * 4 * 3 * 2 * 1 = 120.

# 📥 Ejemplo de entrada:

# 1
# 5
# 12

# 🖥️ Ejemplo de salida:

# Factorial: 1, Doble: 2
# Factorial: 120, Doble: 240
# Factorial: 479001600, Doble: 958003200

# 🚫 Restricciones:

#     No puedes utilizar las funciones map, filter o reduce
#     No puedes utilizar excepciones (try, except)


def factorial_y_doble(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    doble = n * 2
    return factorial, doble

while True:
    entrada = input().strip()
    if entrada.lower() == "":
        break
    n = int(entrada)
    fact, dob = factorial_y_doble(n)
    print("Factorial:", fact, ", Doble:", dob)
