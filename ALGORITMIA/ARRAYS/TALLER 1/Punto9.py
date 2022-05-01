#9)	Rellene un array con 20 números al azar y luego busque un número concreto ingresado por el usuario, si el número es encontrado debe imprimir la posición en el que se encontró, por el contrario, imprimir que el número no se encontró.

import random
numeros=[]

for i in range(0,20):
    numeros.append(random.randrange(0,1000))

print(numeros)

buscar=int(input('Ingrese el numero a buscar: '))

try:
    posicion = numeros.index(buscar)
    print(f'Numero encontrado en la posicion {posicion}')
except ValueError as error:
    print('Numero no encontrado')