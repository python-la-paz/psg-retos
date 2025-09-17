## 8.

entrada_semaforo=input("Ingrese (separado por comas): ").strip().split(",")
#--
sensor_1=int(entrada_semaforo[0].strip())
sensor_2=len(entrada_semaforo[1].strip())
sensor_3=eval(entrada_semaforo[2].title().strip())
#--
condicion_1=sensor_3
condicion_2=(sensor_1>70) and (sensor_2<5) and not condicion_1
condicion_3=(sensor_2>=5) and not condicion_1
#--
indice=(int(condicion_1)*2)+(int(condicion_2)*2)+(int(condicion_3)*0)+ (int(not (condicion_1 or condicion_2 or condicion_3))*1)
#--
colores_semaforo=("Rojo","Amarillo","Verde")
#---
print(f"Semáforo: {colores_semaforo[indice]}")

