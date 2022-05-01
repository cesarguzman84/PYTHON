#Determinar cuánto dinero ahorra una persona en un año si considera que cada semana
#  ahorra 15% de su sueldo (considere cuatro semanas por mes y que no cambia el sueldo)

sueldo = int(input("Indica tu salario semanal: "))
ahorro = sueldo*0.15

ahorro_anual = (ahorro*4)*12

print("Has ahorrado " + str(ahorro_anual) + "en un año")