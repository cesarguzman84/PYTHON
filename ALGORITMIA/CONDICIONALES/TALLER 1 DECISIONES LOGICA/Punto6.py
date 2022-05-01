#6.	Crear un algoritmo que le permita al usuario ingresar el tipo de trabajador (FIJO o TEMPORAL)
#  y con base en esto pueda imprimir el nombre y el salario neto, 
# sabiendo que si es FIJO debe leer el nombre, el número de horas trabajadas, el salario básico hora, 
# el total de deducciones y el total de bonificaciones 
# y si es TEMPORAL solo debe leer el nombre y el número de horas trabajadas; 
# estos trabajadores tienen un salario básico hora fijo de $6.000 y no tienen deducciones ni bonificaciones.

tipo_contrato = input(("Ingrese si el empleado tiene contrato FIJO o TEMPORAL: ").lower())

if tipo_contrato=="fijo":
    nombre = input("Ingrese el nombre del empleado: ")
    horas_trabajadas = int(input("Ingrese el numero de horas trabajadas: "))
    salario_basico_hora= int(input("Ingrese el salario basico por hora del empleado: "))
    deducciones= int(input("Ingrese las deducciones del empleado: "))
    bonificaciones = int(input("Ingrese las bonificaciones del empleado: "))
    sueldo=(horas_trabajadas*salario_basico_hora)-deducciones+bonificaciones
    print("El salario del empleado es: " + str(sueldo))
elif tipo_contrato=="temporal":
    nombre = input("Ingrese el nombre del empleado: ")
    horas_trabajadas = int(input("Ingrese el numero de horas trabajadas: "))
    sueldo = horas_trabajadas*6000
    print("El salario del empleado es: " + str(sueldo))
else:
    print("Error, verifique los datos ingresados para el contrato")

