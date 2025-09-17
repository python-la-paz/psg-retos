sol = input().lower() == "true"
hum = int(input())
sw = (sol and (hum<30))
print(((sw) and "El sistema de riego no se activa.") or ((not sw) and "El sistema de riego se activa."))