manzanas_rojas = 0
manzanas_verdes = 0
manzanas_plagas = 0



while True:
    entrada_datos = input("Copiar los datos del sensor:").strip()
    if entrada_datos == "empacar":
        break
    
    for letra in entrada_datos:
        if letra =="r":
            manzanas_rojas += 1
        elif letra =="v":
            manzanas_verdes +=1
        elif letra =="p":
            manzanas_plagas +=1
cajas_rojas = manzanas_rojas//12
cajas_verdes = manzanas_verdes//12

print(f"Cajas empacadas para rojas: {cajas_rojas}")
print(f"Cajas empacadas para verdes: {cajas_verdes}")
print(f"Cantidad de manzanas con plagas: {manzanas_plagas}")