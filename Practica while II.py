import math
print("Programa del calculo de raiz cuadrada")
numero=int(input("Introduce un numero "))

intentos=0

while numero<0:
	print("No se puede hallar la raiz de un numero negativo ")

	if intentos==2:
		print("Lo has intentado muchas veces. EL programa a finalizado")
		break; #TERMINA EL BUCLE IF

	numero=int(input("Introduce el numero: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))