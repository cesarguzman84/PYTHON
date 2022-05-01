#5)	Crear un algoritmo que calculo el precio total a pagar para un usuario del metro que desea recargar la cívica,
# el usuario solo ingresa el número de viajes que quiere comprar, se le debe decir cuánto le cuesta. Suponga que el viaje vale $2.200

print("Programa calculo de precio Civica")

NumeroViajes=int(input("Por favor introduce el nuumero de viajes que deseas comprar "))

PrecioViaje=NumeroViajes*2200

print("Tu tienes que pagar " + str(PrecioViaje) + " Pesos")