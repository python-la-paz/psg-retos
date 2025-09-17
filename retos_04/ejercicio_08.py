linea = input("Ingresar los datos del sensor: ").strip()

datos = linea.split(",")
vehiculos = datos[0].strip()
peatones = datos[1].strip()
emergencia = datos[2].strip()

vehiculo_2 = int(vehiculos)
peatones_2 = len(peatones)

emergencia_2 = emergencia in ["True", "1", "true", "TRUE"]

estado = (
    emergencia_2 and "Verde") or ((not emergencia_2 and peatones_2 >5) and "Rojo"
                                  ) or ((not emergencia_2 and peatones_2 >70 )and "Verde"
                                        ) or ((not emergencia_2 and peatones_2 <=70)and "Amarillo"
                                              )

print(f"Semaforo:{estado}")


