#Desarrolle un algoritmo que permita leer los primeros n números enteros, los almacene en un vector y los imprima en pantalla de forma ascendente y descendente.

numeros = int(input("Ingrese los n numeros para el vector "))

array1=[]

for i in range(0,numeros):
    array1.append(int(input('Ingrese un numero entero: ')))


ascendente = sorted(array1)
descendente = sorted(array1, reverse=True)

print(f'Los numeros del vector ordenados en forma ascendente son: {ascendente}')
print(f'Los numeros del vector ordenados en forma ascendente son: {descendente}')

