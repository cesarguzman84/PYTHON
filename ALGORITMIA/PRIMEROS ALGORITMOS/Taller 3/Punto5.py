# 5) Realice el algoritmo para determinar el promedio que obtendrá un alumno 
# considerando que realiza tres exámenes, de los cuales el primero y el segundo tienen una ponderación
#  de 25%, mientras que el tercero de 50%.

examen1= float(input("Indica la nota del examen 1: "))
examen2= float(input("Indica la nota del examen 2: "))
examen3= float(input("Indica la nota del examen 3: "))

nota = (examen1*0.25)+ (examen2*0.25) + (examen3*0.5)

print("La nota del alumno es " + str(nota))