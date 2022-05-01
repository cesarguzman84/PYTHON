#Programa para ingresar datos en un array a travez de un ciclo for

datos = []
for i in range(1,7):
    nuevoDato = int( input( "Dime el dato numero {}: ".format(i) ))
    datos.append(nuevoDato)
print ("Los datos al reves son: ")
for i in range(6,0,-1):
    print ( datos[i-1] )