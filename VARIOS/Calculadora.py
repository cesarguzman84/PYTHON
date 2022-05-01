# Hacer un programa que pida un número por teclado y guarde en una lista su tabla de multiplicar  hasta el 10

numero = int(input("Digite un numero: "))

lista = []

for i in range(1,11):
    lista.append(i*numero)
    
print(lista)