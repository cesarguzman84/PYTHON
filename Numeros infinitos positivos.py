print("Programa de numeros infinitos")
numero=int(input("Introduce un numero: "))
suma=0

while numero > 0:

	suma=suma+numero
	numero=int(input("escriba un nuevo numero "))

print("La suma de los numeros es", str(suma))