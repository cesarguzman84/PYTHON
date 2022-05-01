#3)	Desarrollar un algoritmo que calcule el promedio de un alumno que tiene
#  7 calificaciones en la materia de química.

suma=0

for i in range(1,8):
    nota =float(input(f"ingrese la nota {i}: "))
    suma = suma+nota

promedio = suma/7

print("El promedio es", promedio)