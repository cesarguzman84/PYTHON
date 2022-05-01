#5)	Un estacionamiento requiere determinar el cobro que debe aplicar a las personas que lo utilizan. 
#Considere que el cobro es con base en las horas Realizar el algoritmo que permita determinar el cobro.

tiempo_estacionamiento = int(input("Por favor introduzca el tiempo que ha permanecido en el estacionamiento "))

valor_hora = int(input("Por favor introduzca el valor de la hora "))

precio_final =(tiempo_estacionamiento*valor_hora)

print("El valor a pagar por el estacionamiento es de " + str(precio_final))