## 14. 
def calcular_operacion_basica (numero_1,numero_2,operacion):
    if operacion == "+":
        return numero_1 + numero_2
    elif operacion == "-":
        return numero_1 - numero_2
    elif operacion == "*":
        return numero_1 * numero_2
    elif operacion == "/":
        if numero_2 == 0:
            raise ZeroDivisionError
        return numero_1 / numero_2
    else:
        raise ValueError
#---

#---
while True:
    entrada_usr=input("Ingrese numeros y operación separado por comas (o 'salir'): ").strip().lower()
    if entrada_usr == "salir":
        break
    try:
        lista_entrada=entrada_usr.split(",")
        if len(lista_entrada)<3:
            raise IndexError
        
        numero_1=float(lista_entrada[0].strip())
        numero_2=float(lista_entrada[1].strip())
        operacion_usr=lista_entrada[2].strip()

        if operacion_usr not in {"+", "-", "*", "/"}:
            raise ValueError
        
        resultado=calcular_operacion_basica(numero_1,numero_2,operacion_usr)
    except ValueError:
        print("\nOperación no valida.")
    except ZeroDivisionError:
        print("\nNo se puede dividir por cero.")
    except IndexError:
        print("\nNo hay suficientes elementos para realizar la operación.")
    else:
        print(f"\nResultado: {round(resultado,2)}")