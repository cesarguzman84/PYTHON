#4)	 Una empresa desea determinar el monto de un cheque que debe proporcionar a uno de sus empleados 
# que tendrá que ir por equis número de días a la ciudad de Bogotá; los gastos que cubre la empresa son: 
# hotel, comida y 200.000 pesos diarios para otros gastos. El monto debe estar desglosado para cada 
# concepto (mostrar detalle a detalle y el total)

hotel = int(input("Indica el precio diario del hotel "))
comida = int(input("Indica el precio diario de la comida "))
otros_gastos = 200000
dias = int(input("Indica el numero de dias que se han de pagar "))

precio_hotel=hotel*dias
precio_comida = comida*dias
precio_otros_gastos = otros_gastos*dias
cheque = precio_hotel+precio_comida+precio_otros_gastos

print("El valor a pagar al empleado por concepto hotel es: " + str(precio_hotel) + " pesos")
print("El valor a pagar al empleado por concepto comidas es: " + str(precio_comida) + " pesos")
print("El valor a pagar al empleado por concepto otros gastos es: " + str(precio_otros_gastos) + " pesos")
print("El valor a pagar al empleado en total es: " + str(cheque) + " pesos")