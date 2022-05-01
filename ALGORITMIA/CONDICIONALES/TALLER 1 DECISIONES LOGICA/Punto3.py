#3.	Elabore un algoritmo que lea el nombre, el salario bruto, las deducciones y 
# las bonificaciones de dos trabajadores, e imprima (escriba un mensaje) el nombre del
#  que más salario neto tiene.

nombre1= input("Ingrese nombre de empleado 1: ")
salarioBruto1= int(input("Ingrese salario bruto de empleado 1: "))
deducciones1 = int(input("Ingrese las deducciones de empleado 1: "))
bonificaciones1 = int(input("Ingrese las bonoficaciones de empleado 1: "))
salarioneto1= salarioBruto1-deducciones1+bonificaciones1

nombre2= input("Ingrese nombre de empleado 2: ")
salarioBruto2= int(input("Ingrese salario bruto de empleado 2: "))
deducciones2 = int(input("Ingrese las deducciones de empleado 2: "))
bonificaciones2 = int(input("Ingrese las bonoficaciones de empleado 2: "))
salarioneto2= salarioBruto2-deducciones2+bonificaciones2

if salarioneto1>salarioneto2:
    print("El empleado con mayor salario es: " + nombre1 )
else:
    print("El empleado con mayor salario es: " + nombre2 )