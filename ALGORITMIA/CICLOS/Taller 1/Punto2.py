# 2)	Crea un programa que calcula la factorial de un nº entero y positivo. Ejemplo factorial de 5= 1.2.3.4.5=120

n=int(input("escriba numero: "))
factorial=1
for i in range(n+1):
	if i==0:
		continue
	else:
		factorial=factorial*i
 
print("resultado",str(factorial))