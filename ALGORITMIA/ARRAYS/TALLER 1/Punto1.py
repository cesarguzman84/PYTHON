# 1)	Hacer un array de 100 enteros y rellenarlo con números aleatorios. Luego mostrarlos en pantalla.

import random

numeros = []

for i in range(0,100):
    numeros.append(random.randrange(0,100))

print(numeros)