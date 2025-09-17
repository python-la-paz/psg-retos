## 2.


#---
luz_solar=eval(input("Luz solar (True/False): "))
humedad=int(input("Humedad: "))
#--
factor_humedad=humedad<30
sistema_de_riego=luz_solar!=(factor_humedad)
#---
print(("El sistema de riego se activa." * sistema_de_riego) + ("El sistema de riego no se activa." * (not sistema_de_riego)))
