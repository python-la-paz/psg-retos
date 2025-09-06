luz_solar = input()
humedad = input()

luz_solar = luz_solar == "True"
humedad = int(humedad)

activar = (luz_solar or (humedad < 30)) and not (luz_solar and (humedad < 30))

print(("El sistema de riego se activa.", "El sistema de riego no se activa.")[not activar])