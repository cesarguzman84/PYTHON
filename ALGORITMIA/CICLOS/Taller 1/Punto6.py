# Dado un grupo de 20 estudiantes que cursaron la materia Algoritmos, se desea saber cuál es el promedio del grupo, cual fue la nota más alta y cual la más baja.



suma=0

for i in range(1,21):
    nota =float(input(f"ingrese la nota {i}: "))
    suma = suma+nota

promedio = suma/7

print("El promedio es", promedio)