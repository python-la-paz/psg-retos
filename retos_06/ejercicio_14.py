def calcular(num1, num2, operador):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        if num2 == 0:
            raise ZeroDivisionError
        return num1 / num2
    else:
        raise ValueError

entrada = input()
try:
    partes = entrada.split(", ")

    if len(partes) < 3:
        raise IndexError

    num1 = float(partes[0])
    num2 = float(partes[1])
    operador = partes[2]

    resultado = calcular(num1, num2, operador)
    print(resultado)

except ValueError:
    print("Operación no valida.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except IndexError:
    print("No hay suficientes elementos para realizar la operación.")
