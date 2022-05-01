#Programa que pide el nombre y lo almacena en un array:
nombre = input( "Dime tu nombre: " )
print ( "Con espacios sería" )
for i in range(0, len(nombre)):
    print ( nombre[i], end="" )
    print ( " ", end="" )
print()
print("Y las letras 2ª a 4ª son:")
print(nombre[1:4])