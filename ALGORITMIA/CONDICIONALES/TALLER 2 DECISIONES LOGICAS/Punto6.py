#6.	Elaborar un programa que le permita a un usuario ingresar el nombre de un trabajador, 
# el número de horas trabajadas y valor hora, se pide que el programa le imprima 
# el salario bruto, las bonificaciones, las deducciones y el salario neto; 
# teniendo en cuenta que las bonificaciones serán de $20.000 si trabajó como máximo 48 horas, 
# de $50.000 si trabajo entre 49 y 58 horas y de $100.000 si trabajó más de 58 horas. 
# Las deducciones son de $10.000 si el salario básico hora es menor de $5.000, de $20.000 
# si el salario básico hora es mayor de $5.000 y menor de $8.000 y de $ 50.000 si su salario 
# básico hora es de $8.000 o más.

nombre = input("Ingresar nombre del empleado: ")
horas = int(input("Ingresar numero de horas trabajadas: "))
valor = int(input("Ingresar el valor de la hora: "))

if horas<= 48:
    bonificacion = 20000
    if valor<5000:
        deduccion = 10000
        sueldo_bruto = horas*valor
        sueldo_neto = sueldo_bruto+bonificacion-deduccion
        print("Nombre del empleado: " + nombre)
        print("Salario bruto: " + str(sueldo_bruto))
        print("Bonificaciones: " + str(bonificacion))
        print("Deducciones: " + str(deduccion))
        print("Salario neteo: " + str(sueldo_neto))
    elif valor>5000 and valor<8000:
        deduccion = 20000
        sueldo_bruto = horas*valor
        sueldo_neto = sueldo_bruto+bonificacion-deduccion
        print("Nombre del empleado: " + nombre)
        print("Salario bruto: " + str(sueldo_bruto))
        print("Bonificaciones: " + str(bonificacion))
        print("Deducciones: " + str(deduccion))
        print("Salario neteo: " + str(sueldo_neto))
    else :
        deduccion = 50000
        sueldo_bruto = horas*valor
        sueldo_neto = sueldo_bruto+bonificacion-deduccion
        print("Nombre del empleado: " + nombre)
        print("Salario bruto: " + str(sueldo_bruto))
        print("Bonificaciones: " + str(bonificacion))
        print("Deducciones: " + str(deduccion))
        print("Salario neteo: " + str(sueldo_neto))
elif horas>=49 and horas <=58:
    bonificacion = 50000
    if valor<5000:
        deduccion = 10000
        sueldo_bruto = horas*valor
        sueldo_neto = sueldo_bruto+bonificacion-deduccion
        print("Nombre del empleado: " + nombre)
        print("Salario bruto: " + str(sueldo_bruto))
        print("Bonificaciones: " + str(bonificacion))
        print("Deducciones: " + str(deduccion))
        print("Salario neteo: " + str(sueldo_neto))
    elif valor>5000 and valor<8000:
        deduccion = 20000
        sueldo_bruto = horas*valor
        sueldo_neto = sueldo_bruto+bonificacion-deduccion
        print("Nombre del empleado: " + nombre)
        print("Salario bruto: " + str(sueldo_bruto))
        print("Bonificaciones: " + str(bonificacion))
        print("Deducciones: " + str(deduccion))
        print("Salario neteo: " + str(sueldo_neto))
    else :
        deduccion = 50000
        sueldo_bruto = horas*valor
        sueldo_neto = sueldo_bruto+bonificacion-deduccion
        print("Nombre del empleado: " + nombre)
        print("Salario bruto: " + str(sueldo_bruto))
        print("Bonificaciones: " + str(bonificacion))
        print("Deducciones: " + str(deduccion))
        print("Salario neteo: " + str(sueldo_neto))
else:
    bonificacion = 100000
    if valor<5000:
        deduccion = 10000
        sueldo_bruto = horas*valor
        sueldo_neto = sueldo_bruto+bonificacion-deduccion
        print("Nombre del empleado: " + nombre)
        print("Salario bruto: " + str(sueldo_bruto))
        print("Bonificaciones: " + str(bonificacion))
        print("Deducciones: " + str(deduccion))
        print("Salario neteo: " + str(sueldo_neto))
    elif valor>5000 and valor<8000:
        deduccion = 20000
        sueldo_bruto = horas*valor
        sueldo_neto = sueldo_bruto+bonificacion-deduccion
        print("Nombre del empleado: " + nombre)
        print("Salario bruto: " + str(sueldo_bruto))
        print("Bonificaciones: " + str(bonificacion))
        print("Deducciones: " + str(deduccion))
        print("Salario neteo: " + str(sueldo_neto))
    else :
        deduccion = 50000
        sueldo_bruto = horas*valor
        sueldo_neto = sueldo_bruto+bonificacion-deduccion
        print("Nombre del empleado: " + nombre)
        print("Salario bruto: " + str(sueldo_bruto))
        print("Bonificaciones: " + str(bonificacion))
        print("Deducciones: " + str(deduccion))
        print("Salario neteo: " + str(sueldo_neto))