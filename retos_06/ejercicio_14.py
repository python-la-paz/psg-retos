while True:
    entrada = input()
    if entrada.lower() == "salir":
        break
    
    try:
        partes = entrada.split(",")
        if len(partes) != 3:
            raise IndexError
        
        num1 = float(partes[0].strip())
        num2 = float(partes[1].strip())
        operador = partes[2].strip()
        
        if operador == "+":
            print(num1 + num2)
        elif operador == "-":
            print(num1 - num2)
        elif operador == "*":
            print(num1 * num2)
        elif operador == "/":
            if num2 == 0:
                raise ZeroDivisionError
            print(num1 / num2)
        else:
            print("Operación no valida.")
    
    except ValueError:
        print("Operación no valida.")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    except IndexError:
        print("No hay suficientes elementos para realizar la operación.")
