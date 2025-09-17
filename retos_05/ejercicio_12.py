## 12. 

equivalencias = {
    "tz": "tazas",
    "cda": "cucharadas",
    "l": "litros",
    "gr": "gramos",
    "kg": "kilogramos",
    "u": "unidades"}
#--
def estandarizacion (receta_usr):
    print("\nIngredientes\n------------\n")
    receta_listada=receta_usr.lower().split(",")
    ##---

    ingredientes=[]
    for conjunto in receta_listada:
        ingrediente=conjunto.strip().split("=")[0]
        cantidad=conjunto.strip().split("=")[1]
        ingredientes.append((ingrediente,cantidad))
    ##---
    ##---
    ingrediente_numerico_medida=[]
    for cantidad in ingredientes:
        numerico=""
        medida=""

        for caracter in cantidad[1]:
            if caracter.isdigit() or caracter==".":
                numerico+=caracter
            elif caracter.isalpha():
                medida+=caracter
        if medida in equivalencias:
            verificador=1
            if float(numerico)>1:
                ingrediente_numerico_medida.append([cantidad[0].title(),numerico,equivalencias[medida]])
            else:
                if equivalencias[medida]!="unidades":
                    ingrediente_numerico_medida.append([cantidad[0].title(),numerico,equivalencias[medida][:len(equivalencias[medida])-1]])
                else:
                    ingrediente_numerico_medida.append([cantidad[0].title(),numerico,equivalencias[medida][:len(equivalencias[medida])-2]])
        else:
            print(f"--Medida incorrecta para '{cantidad[0]}': '{medida}' (se omite).--")
            continue
    ##---
    i=0
    while i<len(ingrediente_numerico_medida):
        print("* "+"  ".join(ingrediente_numerico_medida[i]))
        i+=1


#---
receta=input("Ingrese receta: ")   
estandarizacion(receta)