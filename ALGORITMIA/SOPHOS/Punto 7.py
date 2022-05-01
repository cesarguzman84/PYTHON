#7) Realice un algoritmo que permita calcular el promedio de los elementos de una matriz
#de tamaño N x N y escriba en pantalla todos los elementos de esta.


matriz = [
    [7.8, 2.5, 10],
    [20, 15.2, 12],
    [89, 9, 6.77],
]

elementos = 0
sumatoria = 0
for fila in matriz:
    for elemento in fila:
        sumatoria += elemento
        elementos += 1

promedio = sumatoria / elementos
print(
    f"La suma es {sumatoria} y el promedio es {promedio}, para la matriz que tiene {elementos} elementos"
)