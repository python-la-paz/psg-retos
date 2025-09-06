jose = input().split(", ")
carlos = input().split(", ")

set_jose = set(jose)
set_carlos = set(carlos)

comunes = set_jose & set_carlos

exclusivas_jose = set_jose - set_carlos
exclusivas_carlos = set_carlos - set_jose

tipos = ["Amigos con Buen Gusto", "Almas Gemelas Musicales"]
indice = (len(comunes) * 2 > len(set_jose) + len(set_carlos))
tipo_amistad = tipos[indice]

print("Canciones en común: " + ", ".join(comunes))
print("Canciones exclusivas de Jose: " + ", ".join(exclusivas_jose))
print("Canciones exclusivas de Carlos: " + ", ".join(exclusivas_carlos))
print("Son " + tipo_amistad + ".")


