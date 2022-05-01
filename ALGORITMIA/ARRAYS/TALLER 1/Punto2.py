# 2)	llene un array de 10 enteros con números aleatorios del 0 al 99, luego de eso los muestre en pantalla y diga cuál es el elemento mayor y cuántas veces se repite.

import random
numeros = []
mayor = 0
cont = 0

for i in range(0,10):
    numeros.append(random.randrange(0,100))

print(numeros)

for i in range (0,10):
    if mayor == numeros[i]:
        cont = cont + 1

print(f'el numero mayor es {mayor} y se repite {cont} veces'  )