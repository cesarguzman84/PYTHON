#Realizar un algoritmo que permita leer un vector de tamaño n, imprimirlo en pantalla
#de forma original y luego calcular el promedio de los elementos múltiplos de 3

numeros = int(input("Ingrese los n numeros para el vector "))

array=[]
impares = []
for i in range(0,numeros):
    array.append(int(input('Ingrese un numero entero: ')))


for i in array:
    if i% 3==0:
        impares.append(i)

print(impares)

suma=0
contador=0
for i in impares:
    suma +=i
    contador=contador+1

promedio = suma/contador
print(promedio)

