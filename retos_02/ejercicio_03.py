## 3.
frase_usr=input("Frase: ").lower().strip()
#--
cantidad_de_palabras=len(frase_usr.split())
es_palindromo=(frase_usr.replace(" ","")==frase_usr.replace(" ","")[::-1])
#--
vocal_a=frase_usr.count("a")
vocal_e=frase_usr.count("e")
vocal_i=frase_usr.count("i")
vocal_o=frase_usr.count("o")
vocal_u=frase_usr.count("u")
cantidad_de_vocales=vocal_a+vocal_e+vocal_i+vocal_o+vocal_u
#--
print("Cantidad de palabras: ", cantidad_de_palabras)
print("Cantidad de vocales: ", cantidad_de_vocales)
print("Es palíndromo: ",es_palindromo)