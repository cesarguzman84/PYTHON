#4)	Elaborar un algoritmo para un trabajador que necesita calcular su salario semanal, el cual se obtiene de la siguiente manera: 
#-	Si trabaja 40 horas o menos se le paga $300 por hora

#-	Si trabaja más de 40 horas se le paga $300 por cada una de las primeras 40 horas y $500 por cada hora extra.


print ("Programa Salario Semanal")

horas_trabajadas=int(input("Introduce el numero de horas trabajadas esta semana por el empleado: "))
print(horas_trabajadas)


if horas_trabajadas<=40:

    salario = horas_trabajadas*300

    print("El salario de esta semana para el empleado es: " + str(salario))

else:

    salario = (40*300)+((horas_trabajadas-40)*500)
    
    print("El salario de esta semana para el empleado es: " + str(salario))