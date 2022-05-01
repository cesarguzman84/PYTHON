'''7)	Elaborar un algoritmo que pida el número final de la placa de un vehículo y permita determinar que día tiene pico y placa.

PLACAS TERMINADAS EN	DIA
0-1	LUNES
2-7	MARTES
9-4	MIERCOLES
5-3	JUEVES
6-8	VIERNES'''

placa = int(input("Por favor introduzca el ultimo numero de la placa "))

if placa==0 or placa==1:
    print("Tiene pico y placa el dia lunes")
elif placa==2 or placa==7:
    print("Tiene pico y placa el dia martes")
elif placa==9 or placa==4:
    print("Tiene pico y placa el dia miercoles")
elif placa==5 or placa==3:
    print("Tiene pico y placa el dia jueves")
elif placa==6 or placa==8:
    print("Tiene pico y placa el dia viernes")
else:
    print("Datos erroneos")

