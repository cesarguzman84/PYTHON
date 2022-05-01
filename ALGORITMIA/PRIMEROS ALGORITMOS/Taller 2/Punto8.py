#8)	La compañía de autobuses “La curva loca” requiere determinar el costo que tendrá
#  el boleto de un viaje sencillo, esto basado en los kilómetros por recorrer y en el costo por kilómetro.

kilometros = int(input("Introduce el numero de kilometros del viaje "))

costo_km = int(input("Introduce el costo por kilometro "))

precio_boleto= kilometros*costo_km

print("El precio del boleto es " + str(precio_boleto))