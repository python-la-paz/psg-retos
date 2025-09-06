entrada = input()

vehiculos_str, peatones, emergencia_str = entrada.split(", ")

vehiculos = int(vehiculos_str)
emergencia = emergencia_str == "True"

semaforo = (
    "Verde" if emergencia or vehiculos > 70 else
    "Rojo" if len(peatones) > 5 else
    "Amarillo"
)

print("Semáforo:", semaforo)
