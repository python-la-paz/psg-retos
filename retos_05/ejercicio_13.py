## 13. 

frase_usr=input("Ingrese frase: ").strip()
#--
funcion_anonima= lambda frase: sorted(set(palabra.strip(".,;:!?¡¿").lower()for palabra in frase.split()))
#--
print(funcion_anonima(frase_usr))
#--NOTA: en la salida del inciso indica que es hasta ´pájaro´, sin embargo, es hasta ´y´