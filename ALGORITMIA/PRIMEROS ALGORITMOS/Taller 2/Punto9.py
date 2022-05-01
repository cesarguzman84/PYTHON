#9)	Se requiere determinar el tiempo que tarda una persona en llegar de una ciudad a otra en bicicleta
#  teniendo como datos los kilómetros a recorrer y la velocidad en km, 
# considerando que lleva una velocidad constante.

distancia = int(input("Introduce los kilometros a recorrer "))
velocidad = int (input("Indica la velocidad "))
tiempo = distancia/velocidad

print("El tiempo del recorrido es " + str(tiempo))