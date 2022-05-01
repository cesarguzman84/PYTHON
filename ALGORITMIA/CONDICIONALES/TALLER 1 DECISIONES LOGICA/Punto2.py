#2.	Elaborar un algoritmo que muestre un mensaje según la edad ingresada; 
# niño (menor de 10 años), preadolescente (mayor o igual a 10años  y menor o igual a 14 años), 
# un adolescente (mayor o igual a 15 años  y menor o igual a 18 años), 
# adulto (mayor o igual a 19 años y menor o igual a 50 años), adulto mayor (mayor de 50 años).

print("Programa edad")

edad=int(input("Ingrese la edad de la persona: "))

if edad < 10:
    print("La persona es un niño")
elif edad>= 10 and edad<=14:
    print("La persona es un preadolescente")
elif edad>=15 and edad<=18:
    print("La persona es un adolescente")
elif edad>=19 and edad<=50:
    print("La persona es un adulto")
else:
    print("La persona es un adulto mayor")