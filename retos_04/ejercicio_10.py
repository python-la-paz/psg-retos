rojas = 0
verdes = 0
plagas = 0

cajas_rojas = 0
cajas_verdes = 0
manzanas = ""

while(manzanas != "empacar") :
    for manzana in manzanas:
        if manzana == "r":
            rojas += 1
            if rojas == 12:
                cajas_rojas += 1
                rojas = 0
        elif manzana == "v":
            verdes += 1
            if verdes == 12:
                cajas_verdes += 1
                verdes = 0
        elif manzana == "p":
            plagas += 1
            
    manzanas = input()

print("Cajas empacadas para Rojas:", cajas_rojas)
print("Cajas empacadas para Verdes:", cajas_verdes)
print("Cajas empacadas para Plagas:", plagas)