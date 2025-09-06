a1 = set(input().split(", "))
a2 = set(input().split(", "))

comunes = a1 & a2
exclusivas_jose = a1 - a2
exclusivas_carlos = a2 - a1
totCanciones = a1 | a2

compatibilidad = (len(comunes) / len(totCanciones) * 100) > 50

print("Canciones en común: " + ", ".join(comunes))
print("Canciones exclusivas de Jose: " + ", ".join(exclusivas_jose))
print("Canciones exclusivas de Carlos: " + ", ".join(exclusivas_carlos))
print((compatibilidad and "Son Almas Gemelas Musicales.") or (not compatibilidad and "Son Amigos con Buen Gusto."))