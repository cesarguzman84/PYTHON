#5.	Elaborar un algoritmo donde el usuario ingrese la placa de un bus, 
# el número de pasajeros transportados y la ruta donde prestó el servicio (A o B) 
# el computador le debe mostrar el dinero que recolectó sabiendo que en la ruta A 
# el pasaje es a $1.200 y en la B a $1.000.

pasajeA= 1200
pasajeB= 1000

placa1= input("Ingrese la placa del bus 1: ")
pasajeros1 = int(input("Ingrese el numero de pasajeros del bus 1: "))
ruta1= input(("Ingrese la ruta donde presto el servicio el bus 1: ").lower())
if ruta1=="a":
    dinero1=pasajeros1*pasajeA
else:
    dinero1=pasajeros1*pasajeB

placa2= input("Ingrese la placa del bus 2: ")
pasajeros2 = int(input("Ingrese el numero de pasajeros del bus 2: "))
ruta2= input(("Ingrese la ruta donde presto el servicio el bus 2: ").lower())
if ruta2=="a":
    dinero2=pasajeros2*pasajeA
else:
    dinero2=pasajeros2*pasajeB

dineroTotal=dinero1+dinero2

print("El dinero total recolectado es: " + str(dineroTotal))



