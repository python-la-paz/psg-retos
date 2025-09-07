def operacion(numero1, numero2, operador):

    try:
        numero1= float(numero1)
        numero2= float(numero2)
        if operador == "+":
            return numero1 + numero2
        elif operador == "-":
            return numero1 - numero2
        elif operador == "*":
            return numero1*numero2
        elif operador == "/":
            if numero2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            return numero1/numero2
        else:
            raise ValueError("Operación no valida")
    except ZeroDivisionError as e:
        print(e)
    except ValueError:
        print(e)
    except TypeError:
        print("Operación no valida") 
while True:

    calculo = input("Ingresar operacion (formato: numero1, numero2, operador) : ")

    if calculo.lower() == "salir":
        break
    try:
        partes = calculo.split(",")
        if len(partes) != 3:
            raise IndexError("No hay suficientes elementos para realizar la operacion")
        
        numero1 = partes[0].strip()
        numero2 = partes[1].strip()
        operador = partes[2].strip()
        
        resultado = operacion(numero1, numero2, operador)
        if resultado is not None:
            print("Resultado:", resultado)
    except IndexError as e:
        print(e)
    except Exception :
        print("Operación no válida")