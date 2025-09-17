## 11.
import math as mth
#--
numero_usr=int(input("Numero: "))
factorial=1
#--
if numero_usr>25:
    factorial=mth.factorial(numero_usr)
else:
    for i in range(1,numero_usr+1):
        factorial*=i
#--
print(f"Factorial: {str(factorial)[:10]},  Doble: {str(factorial*2)[:10]}")