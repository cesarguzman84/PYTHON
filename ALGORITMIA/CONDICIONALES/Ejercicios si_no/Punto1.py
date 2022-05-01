#1)	Elaborar un algoritmo que permita averiguar si una persona debe sacar su cedula (mayor de 17 años), sabiendo su año de nacimiento.

print ("Programa cedula")

ano_nacimiento=int(input("Introduce tu año de nacimento "))
print(ano_nacimiento)

edad = 2020 - ano_nacimiento

if edad>17:

	print("Debes sacar tu cedula ")

else:

	print("No debes sacar tu cedula ")