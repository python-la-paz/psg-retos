def factorial_doble(numero):

    factorial = 1

    if numero <= 1:
        factorial = 1
    else:
        for i in range(1, numero +1):
            factorial = factorial*i
    doble = factorial*2
    return factorial, doble

numero = int(input ("Ingrese el número :"))

factorial,doble = factorial_doble(numero)

print(f"Factorial: {factorial},Doble: {doble}")