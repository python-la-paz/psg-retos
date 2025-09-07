# Reto 09 - ejercicio_02.py

# Un jardín cuenta con un sistema de riego automático que se activa cuando 
# hay luz solar o cuando la humedad del suelo es menor al 30%, pero no debe activarse 
# si ambas condiciones se cumplen al mismo tiempo. Crea un programa que reciba un valor 
# booleano luz_solar y un valor entero humedad (0-100) y retorne si el sistema de riego 
# debe activarse o no.

# 📥 Ejemplo de entrada:

# True
# 25

# False
# 20

# 🖥️ Ejemplo de salida:

# El sistema de riego no se activa.
# El sistema de riego se activa.

# 🚫 Restricciones:

#     Solo puedes utilizar operadores lógicos: and, or, not
#     No puedes usar estructuras de control (if, for, while)
#     No puedes definir funciones (def, lambda)
#     No puedes usar f-strings (f"", format(), %)
#     No puedes utilizar excepciones (try, except)


# Entrada
luz_solar = eval(input())
humedad = int(input())

condicion_luz = luz_solar
condicion_humedad = humedad < 30

activar = (condicion_luz or condicion_humedad) and not (condicion_luz and condicion_humedad)

# Salida
print("El sistema de riego se activa." * activar + "El sistema de riego no se activa." * (not activar))
