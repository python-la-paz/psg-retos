luz_solar = input("Hay luz solar? :")
humedad = int(input("Ingrese la humedad valores entre (0-100): "))

convertido = luz_solar ="True"
activar = convertido != humedad<30

print( activar and "El sistema de riego se activa" or "El sistema de riego no se activa")