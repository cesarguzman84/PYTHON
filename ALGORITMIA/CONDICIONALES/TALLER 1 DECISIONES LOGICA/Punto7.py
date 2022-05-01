#7.	Elaborar Un algoritmo que le permita al usuario leer 3 número diferentes entre sí
#  y el computador le imprima el mayor de ellos.

numero1=int(input("Ingrese el numero 1: "))
numero2= int(input("Ingrese el numero 2: "))
numero3 = int(input("Ingrese el numero 3: "))

if numero1>numero2 and numero1>numero3:
    print("El numero mayor es el " + str(numero1))
elif numero2>numero1 and numero2>numero3:
    print("El numero mayor es el " + str(numero2))
else:
    print("El numero mayor es el " + str(numero3))
