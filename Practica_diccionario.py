midiccionario={"Alemania":"Berlin","Francia":"Paris", "Reino unido":"Londres","España":"Madrid"}
midiccionario["Italia"]="Roma"
print(midiccionario["Francia"])
print(midiccionario)
del midiccionario["Francia"]  #ELIMINA EL ELEMENTO FRANCIA DEL DICCIONARIO
print (midiccionario)
print (midiccionario.keys()) #MUESTRA LAS CLAVES DEL DICCIONARIO
print(midiccionario.values())#MUESTRA LOS VALORES DEL DICCIONARIO
print(len(midiccionario))#MUESTRA LA LONGITUD DEL DICCIONARIO