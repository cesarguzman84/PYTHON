# Escribir un programa que reciba una a una las notas del usuario, preguntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.

promedio, total, contar = 0.0, 0, 0

print ("Introduzca la nota de un estudiante (-1 para salir): " )
grado = int(input())	
while grado != -1:
    total = total + grado
    contar = contar + 1
    print ("Introduzca la nota de un estudiante (-1 para salir): ")
    grado = int(input())
promedio = total / contar
print ("Promedio de notas del grado escolar es: " + str(promedio))


