def factorial_y_doble(n: int):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    doble = factorial * 2
    return factorial, doble

entrada = input()

numero = int(entrada)
factorial, doble = factorial_y_doble(numero)
print(f"Factorial: {factorial}, Doble: {doble}")