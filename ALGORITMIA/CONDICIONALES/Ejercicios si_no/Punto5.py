#5)	Elaborar un algoritmo que pida un número del 1 al 7 y entregue como resultado el nombre del día correspondiente a la semana.

#Por ejemplo:

#Si el usuario ingresa el número 1, entonces se le debe dar como resultado “Lunes”

print("Programa dia de la semana")

dia=int(input("Introduce un numero del 1 al 7 "))

if   dia==1:
	 print("Hoy es lunes")
elif dia==2:
	 print("Hoy es martes")
elif dia == 3:
	 print("Hoy es miercoles")
elif dia == 4:
	 print("Hoy es jueves")
elif dia== 5:
	 print("Hoy es viernes")
elif dia== 6:
    	 print("Hoy es sabado")
elif dia== 7:
    	 print("Hoy es domingo")
else:
	 print("Error, ingreso un numero no valido")
