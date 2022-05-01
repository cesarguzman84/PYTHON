#Realice un algoritmo que permita buscar un elemento en una matriz de tamaño N x
#N y escriba en pantalla la posición de ese elemento y cuántas veces se encuentra
#repetido.


from random import *

fil=3
col=3

a=[[randint(1,100) for i in range (fil)]for j in range(col)]

#for f in range(fil):
#    for c in range(col):
#        print (a[f][c], end= ' ')
#    print()
for f in a:
    print(f)
c = int (input('Digite columna a obtener'))
b=[]

for f in range (len(a)):
    b.append(a[f][c])

print(b)