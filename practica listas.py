milista=["maria","pepe","martha","antonio"]#CREACION DE LA LISTA
print(milista[:])#IMPRIME TODOS LOS ELEMENTOS DE LA LISTA
print(milista[3])#IMPRIME EL ELEMENTO 3 DE LALISTA
milista.append("cesar")#AÑADE UN NUEVO ELEMENTO A LA LISTA
print(milista[:])
milista.insert(2,"lina")#AÑADE UN NUEVO ELEMENTO A LA LISTA EN LA POSICION 2
print(milista[:])
milista.extend(["leidy","luz","tatiana"])#CONCATENA MILISTA CON OTRA LISTA
print(milista[:])
print(milista.index("leidy"))#ME INDICA EL NUMERO DE LA LISTA EN QUE SE ENCUENTRA LEIDY
print("lina" in milista)#INDICA SI UN ELEMENTO SE ENCUNTRA EN LA LISTA
milista.remove("luz")#REMUEVE A LIZ DE MI LISTA
print(milista[:])
milista2=["jesica",5]
milista3=milista+milista2
print(milista3[:])
