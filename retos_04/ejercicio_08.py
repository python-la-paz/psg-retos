v, p, e = input().split(",")
vehiculos = int(v)
peatones = len(p)
emergencia = e.lower().strip() == "true"
print(emergencia, e)

print("Semáforo:",
    (emergencia and "Verde") or
    ((vehiculos > 70) and "Verde") or
    ((peatones > 5) and "Rojo") or
    "Amarillo"
)
