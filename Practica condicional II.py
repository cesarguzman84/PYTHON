print ("programa de becas")
distancia_escuela=int(input("Introduce la distancia a la escuela en km "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce numero de hermanos "))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario familiar "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:

	print("tiene derecho a beca ")

else:

	print("no tiene derecho a beca ")