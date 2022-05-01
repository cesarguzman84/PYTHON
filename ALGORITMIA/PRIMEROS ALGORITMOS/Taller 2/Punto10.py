#10)Se requiere determinar el costo que tendrá realizar una llamada telefónica
#  con base en el tiempo que dura la llamada y en el costo por minuto

tiempo = int(input("Indica por favor la duracion de la llamada en minutos "))
costo_min = int(input("Indica por favor el costo de la llamada por minuto "))

precio = tiempo*costo_min

print("El costo total de la llamada fue "+ str(precio))