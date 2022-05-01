#4.	Crear un algoritmo que le permita al usuario ingresar los datos de dos buses así:
#  Placa, El número de pasajeros transportado y el valor del pasaje, 
# y el computador le muestre la placa del bus que más dinero recogió.

placa1= input("Ingrese la placa del bus 1: ")
pasajeros1 = int(input("Ingrese el numero de pasajeros del bus 1: "))

placa2= input("Ingrese la placa del bus 2: ")
pasajeros2 = int(input("Ingrese el numero de pasajeros del bus 1: "))

pasaje= int(input("Ingrese el valor del pasaje: "))

dinero1=pasajeros1*pasaje
dinero2=pasajeros2*pasaje

if dinero1>dinero2:
    print("El bus que mas dinero recolecto es el de placa: " + placa1)
else:
    print("El bus que mas dinero recolecto es el de placa: " + placa2)