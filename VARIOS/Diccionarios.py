#Diccionarios

diccionario = {"azul": "blue","rojo":"red", "verde":"green"}
diccionario["amarillo"] = "yellow" #agregar elemento
print(diccionario)
print(diccionario["azul"])

del(diccionario["verde"])
print(diccionario)

diccionario1= {"Lina":[33,160], "Jesica":[30,170]}
print(diccionario1)


equipo = {10:"Dvbala", 11:"Costa", 7:"Ronaldo"}
print(equipo[7])
print(equipo.get(10, "No existe"))
print(equipo.get(15, "No existe este jugador"))
print(10 in equipo)
print(15 in equipo)
print(equipo.keys())
print(equipo.values())
print(len(equipo))
equipo.clear()
print(equipo)