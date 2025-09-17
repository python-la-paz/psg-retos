rojas = 0
verdes = 0
plagas = 0

while True:
    entrada = input().lower().strip()
    if entrada == "empacar":
        break
    for color in entrada:
        if color == "r":
            rojas += 1
        elif color == "v":
            verdes += 1
        elif color == "p":
            plagas += 1

print("Cajas empacadas para Rojas:", rojas // 12)
print("Cajas empacadas para Verdes:", verdes // 12)
print("Cajas empacadas para Plagas:", plagas) # no se divide por el ejemplo de salida
#print("manzanas detectadas con plagas", plagas) deberia ser la salida

