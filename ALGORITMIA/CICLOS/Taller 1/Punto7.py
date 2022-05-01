# 7)	 Crear un algoritmo que lea un número entero y sume los números comprendidos entre 1 y el número leído inclusive. Ejemplo: el usuario ingresó en número 8, se debe sumar 1+2+3+4+5+6+7+8

numero = int(input("ingrese un numero: "))
x=1
suma = 0
while x <= numero:
    suma = suma + x
    x = x+ 1
print("La suma de los numeros es", suma)