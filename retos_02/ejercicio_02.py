## 2.

estado_de_sistema_de_riego=("El sistema de riego no se activa.","El sistema de riego se activa.")
#---
luz_solar=eval(input("Luz solar (True/False): "))
humedad=int(input("Humedad: "))
#--
factor_humedad=humedad<30
sistema_de_riego=luz_solar!=(humedad<30)
#---
print(estado_de_sistema_de_riego[sistema_de_riego])
