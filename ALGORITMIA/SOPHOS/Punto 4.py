#4) Realice un algoritmo que permita ordenar un vector de 8 números enteros de menor
#a mayor utilizando el método de la burbuja. Este vector debe contener números
#repetidos.
#Ejemplo: Vnums = {5,3,8,4,3,7,5,9}. Al final se debe mostrar en pantalla el vector original,
#el vector ordenado y la cantidad de elementos repetidos en el vector.

def bubbleSort(array):
    length = len (array) - 1

    for i in range (0,length):

        for j in range(0, length):
            if array[j]> array [j+1]:
                aux = array [j]
                array[j] =array [j+1]
                array[j+1] = aux
    return array
scores = [70, 90, 0, 80, 60, 85]
print("Antes de ordenar: ")
print(scores)
print("Despues de ordenar: ")
print(bubbleSort (scores))