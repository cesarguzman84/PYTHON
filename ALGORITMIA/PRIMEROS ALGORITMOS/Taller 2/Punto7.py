#7)	Un productor de leche lleva el registro de lo que produce en litros, 
# pero cuando entrega le pagan en galones. 
# Realice un algoritmo que ayude al productor a saber cuánto recibirá por
#  la entrega de su producción de un día (1 galón = 3.785 litros).

litros = int(input("Por favor introduce el numero de litros "))
precio = int (input("Por favor introduce el precio del galon "))
galones = litros*3.785
valor_a_pagar = precio*galones

print("El dia de hoy recibiras " + str(valor_a_pagar) + " pesos, por tu produccion" )