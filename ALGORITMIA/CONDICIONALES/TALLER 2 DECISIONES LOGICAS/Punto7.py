#7.	Para la materia de Destrezas se determinó con los estudiantes que, 
# si la nota del primer quiz era menor que la del segundo, 
# se sustituía la primera nota por la segunda. La tercera y cuarta nota no se modifican. 
# Elabore un algoritmo que le permita al profesor ingresar las 4 notas que obtuvo un alumno
#  y el computador le muestre la nota definitiva y la calificación cualitativa que es:
#  “E” si es mayor o igual a 4.5, “S” si es mayor o igual a 4.0 y menor de 4.5, 
# “B” si es mayor o igual a 3.5 y menor de 4.0, “A” si es mayor o igual a 3.0  y menor de 3.5, 
# “D” si es mayor o igual a 2.0 y menor de 3.0  “I” si es menor de 2.0.

nota1= float(input("Ingrese la nota 1: "))
nota2= float(input("Ingrese la nota 2: "))
nota3= float(input("Ingrese la nota 3: "))
nota4= float(input("Ingrese la nota 4: "))

if nota1<nota2:
    promedio = (nota2+nota2+nota3+nota4)/4
    if promedio>=4.5:
        print("La nota es E")
    elif promedio>=4 and promedio<=4.5:
        print("La nota es S")
    elif promedio>=3.5 and promedio<=4:
        print("La nota es B")
    elif promedio>=3 and promedio<=3.5:
        print("La nota es A")
    elif promedio>=2 and promedio<=3:
        print("La nota es D")
    elif promedio>=0 and promedio<=2:
        print("La nota es I")
else:
    promedio = (nota1+nota2+nota3+nota4)/4
    if promedio>=4.5:
        print("La nota es E")
    elif promedio>=4 and promedio<=4.5:
        print("La nota es S")
    elif promedio>=3.5 and promedio<=4:
        print("La nota es B")
    elif promedio>=3 and promedio<=3.5:
        print("La nota es A")
    elif promedio>=2 and promedio<=3:
        print("La nota es D")
    elif promedio>=0 and promedio<=2:
        print("La nota es I")