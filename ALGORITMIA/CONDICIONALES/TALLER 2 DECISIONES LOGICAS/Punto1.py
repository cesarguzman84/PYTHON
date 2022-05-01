#1.	Crear un algoritmo que le permita al usuario ingresar el nombre de un estudiante y 
# las 4 notas que obtuvo en una materia y el computador le imprima
#  el nombre, la nota definitiva y un mensaje que le indique si “GANA” O “PIERDE”. 
# (LAS NOTAS SON DE 0 A 5.0, GANA SI LA NOTA ES MAYOR O IGUAL A 3.0 Y PIERDE SI ES MENOR A 3.0)

nombre=input("ingrese el nombre del alumno: ")
materia = input("ingrese el nombre la materia: ")

nota1= float(input("Ingrese e valor de la nota 1: "))
nota2= float(input("Ingrese e valor de la nota 2: "))
nota3= float(input("Ingrese e valor de la nota 3: "))
nota4= float(input("Ingrese e valor de la nota 4: "))

nota_final = (nota1+nota2+nota3+nota4)/4

if nota_final >=3:
    print("El estudiante " + nombre + " tiene para la materia de " + materia + " una nota de " + str(nota_final)+ " y por tanto APRUEBA la materia")
else:
    print("El estudiante " + nombre + " tiene para la materia de " + materia + " una nota de " + str(nota_final)+ " y por tanto REPRUEBA la materia")
