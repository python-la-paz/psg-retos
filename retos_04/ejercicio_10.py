## 10. 
entrada_usr="x"
contador_rojo=0
contador_verde=0
contador_plaga=0
print("\n")
#--
while (True):
    entrada_usr=input("Manzanas identificadas: ").strip().lower()
    if entrada_usr=="empacar":
        break
    contador_rojo+=entrada_usr.count("r")
    contador_verde+=entrada_usr.count("v")
    contador_plaga+=entrada_usr.count("p")
#--
print(f"\nCajas empacadas para Rojas: {contador_rojo//12}\nCajas empacadas para Verdes: {contador_verde//12}\nCajas empacadas para Plagas: {contador_plaga}")