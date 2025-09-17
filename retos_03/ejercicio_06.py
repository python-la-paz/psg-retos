## 6.
estado_de_amistad=("Amigos con Buen Gusto","Almas Gemelas Musicales") 
#--
jose=input ("Canciones (separados por comas): ").strip().title().split(", ")
carlos=input ("Canciones (separados por comas): ").strip().title().split(", ")
#--
set_jose=set(jose)
set_carlos=set(carlos)
#--
canciones_en_comun=set_jose & set_carlos
exclusivas_jose=set_jose-set_carlos
exclusivas_carlos=set_carlos-set_jose
total_canciones=len(set_jose | set_carlos)
#--
veredicto=estado_de_amistad[int(len(canciones_en_comun)>(total_canciones*0.5))]
#--
print(f"Canciones en común: {', '.join(canciones_en_comun)}\nCanciones exclusivas de Jose: {', '.join(exclusivas_jose)}\nCanciones exclusivas de Carlos: {', '.join(exclusivas_carlos)}\n{veredicto}")