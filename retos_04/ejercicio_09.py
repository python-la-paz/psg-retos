## 9. 
palabras_sin_contenido = [
    "el", "la", "los", "las", "de", "y", "a", "en", "o", "que",
    "pero", "con", "por", "para", "un", "una", "es", "son",
    "se", "del", "al", "lo"
]
#--
texto_usr=input("Ingrese texto: ").strip().lower().split(" ")
#---
texto_palabras=[]
for palabra in range (len(texto_usr)):
    if texto_usr[palabra] not in palabras_sin_contenido:
        texto_palabras.append(( texto_usr.count(texto_usr[palabra]),texto_usr[palabra]))
#---
ordenados=sorted(list(set(texto_palabras)),reverse=True)
tres_primeras_palabras=[]
#--
for i in range(3):
    tres_primeras_palabras.append(ordenados[i][1])
print(tres_primeras_palabras)