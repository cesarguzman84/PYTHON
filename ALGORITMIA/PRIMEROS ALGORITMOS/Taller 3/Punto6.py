# 6)	 El hotel “Cama Arena” requiere determinar lo que le debe cobrar a un huésped por
#  su estancia en una de sus habitaciones. Realice el algoritmo para determinar ese cobro.

valor_habitacion_diario = int(input("Indica el valor diario de la habitacion "))
dias = int(input("Indica el numero de dias "))

precio = valor_habitacion_diario*dias

print("El valor a pagar es " + str(precio))
