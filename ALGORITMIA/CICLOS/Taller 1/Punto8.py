#8) Escribir un programa que lea 10 datos desde el teclado y sume sólo aquellos que sean negativos.

suma=0

for i in range(1,11):
    numero =float(input(f"ingrese el numero {i}: "))
    if numero<=0:
        suma = suma+numero


print("La suma de los numeros negativos es: ", suma)