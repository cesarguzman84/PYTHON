# 4)	llene un array con los 100 primeros números enteros y los muestre en pantalla en orden descendente.

numeros=[]

for i in range(1,101):
    numeros.append(i)

numeros.sort(reverse=True)

print(numeros)