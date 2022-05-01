# 5)	Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales (primero uno, luego otro, y así hasta que el usuario ingrese -1 como condición de salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.

promedio, total, contar = 0.0, 0, 0

print ("Introduzca un numero (-1 para salir): " )
numero = int(input())	
while numero != -1:
    total = total + numero
    contar = contar + 1
    print ("Introduzca la nota de un estudiante (-1 para salir): ")
    numero = int(input())
ingresos = contar
suma = total
promedio = total / contar
print ("Los numeros ingresado fueron: " + str(ingresos) + " numeros ")
print ("La suma de los numeros ingresados es es " + str(suma))
print ("El promedio de los numeros ingresados es es " + str(promedio))