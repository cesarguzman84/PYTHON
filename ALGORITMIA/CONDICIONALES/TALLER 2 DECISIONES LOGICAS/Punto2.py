#2.	Crear un algoritmo que le permita al usuario ingresar 3 números diferentes entre sí
#  y el computador se los muestre en orden ascendente

numero1= int(input("Ingrese el numero 1: "))
numero2= int(input("Ingrese el numero 2: "))
numero3= int(input("Ingrese el numero 3: "))

Listanumeros = [numero1, numero2, numero3]

ordenada = sorted(Listanumeros)

print("Los numeros ordenados son: " + str(ordenada))