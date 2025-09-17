def factorial_y_doble(n):
    factorial = 1
    if(n>0):
        for i in range(1, n + 1):
            factorial *= i
    elif (n<0):
        print("no hay factorial de un numero negativo")
        factorial=0
        doble=0
        return factorial, doble
    doble = factorial * 2
    return factorial, doble
n = int(input())
fact, dob = factorial_y_doble(n)
print(f"Factorial: {fact}, Doble: {dob}")
