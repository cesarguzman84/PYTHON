#3) Realizar un algoritmo que permita calcular la media y la mediana de los elementos de
#un vector de tamaño n. Se debe mostrar en pantalla los elementos del vector.
import statistics as stats
numeros = int(input("Ingrese los n numeros para el vector "))

array=[]

for i in range(0,numeros):
    array.append(int(input('Ingrese un numero entero: ')))


print("La media del vector dado es: " + str(stats.mean(array)))

print("La mediana del vector dado es:" + str(stats.median(array)))

