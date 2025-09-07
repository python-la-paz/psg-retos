# Reto 17 - ejercicio_10.py

# Una cinta transportadora clasifica manzanas y las va empacando en cajas según su color. En cada caja se empacan 12 manzanas. La cinta tiene un sensor que detecta el color de cada manzana y envía una cadena con el color de la manzana r para las rojas y v para las verdes. Si el sensor detecta una manzana con plagas envía un p. El programa se detiene cuando el sensor envía "empacar" y devuelve la cantidad de cajas empacadas para cada color y cuantas manzanas con plagas se detectaron.

# 📥 Ejemplo de entrada:

# rvrvrvrpvvrrv
# rrvvvppp
# ppprrrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvr
# empacar

# 🖥️ Ejemplo de salida:

# Cajas empacadas para Rojas: 2
# Cajas empacadas para Verdes: 2
# Cajas empacadas para Plagas: 7

# 🚫 Restricciones:

#     No puedes definir funciones (def, lambda)
#     No puedes utilizar las funciones map, filter o reduce
#     No puedes utilizar excepciones (try, except)

cajas_rojas = 0
cajas_verdes = 0
plagas = 0

contador = {"r": 0, "v": 0}  
while True:
    entrada = input().strip()
    if entrada == "empacar":
        break
    for c in entrada:
        if c in ("r", "v"):
            contador[c] += 1
            if contador[c] == 12:
                if c == "r":
                    cajas_rojas += 1
                else:
                    cajas_verdes += 1
                contador[c] = 0
        elif c == "p":
            plagas += 1

print("Cajas empacadas para Rojas:", cajas_rojas)
print("Cajas empacadas para Verdes:", cajas_verdes)
print("Cajas empacadas para Plagas:", plagas)
