# Reto 21 - ejercicio_14.py

# Crea una calculador interactiva que permita calcular la suma +, resta -, multiplicación * y division / de dos numero que pueden ser enteros o flotantes.

# Las operaciones que se ingresan tienen el formato numero1, numero2, operador hasta que el usuario ingrese "salir".

# La calculadora debe manejar las siguientes excepciones:

#     ValueError: Si el usuario ingresa valores no válidos.
#     ZeroDivisionError: Si se intenta dividir por cero.
#     IndexError: Si el usuario no ingresa todos los elementos necesarios para realizar la operación.

# 📥 Ejemplo de entrada:

# 10, 5, +
# 20.2, 10.1
# 30, 0.5, a 
# 40, 0, /
# abc, 5, +

# 🖥️ Ejemplo de salida:

# 15.0
# No hay suficientes elementos para realizar la operación.
# Operación no valida.
# No se puede dividir por cero.
# Operación no valida.

# 🚫 Restricciones:

#     No puedes utilizar las funciones map, filter o reduce


entrada = input().strip()

try:
        partes = [x.strip() for x in entrada.split(",")]
        
        if len(partes) < 3:
            raise IndexError
        
        n1 = float(partes[0])
        n2 = float(partes[1])
        op = partes[2]
        
        if op == "+":
            print(n1 + n2)
        elif op == "-":
            print(n1 - n2)
        elif op == "*":
            print(n1 * n2)
        elif op == "/":
            if n2 == 0:
                raise ZeroDivisionError
            print(n1 / n2)
        else:
            print("Operación no valida.")
except ValueError:
        print("Operación no valida.")
except ZeroDivisionError:
        print("No se puede dividir por cero.")
except IndexError:
        print("No hay suficientes elementos para realizar la operación.")
