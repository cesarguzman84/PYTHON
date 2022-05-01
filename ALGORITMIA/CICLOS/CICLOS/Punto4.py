#4)	Desarrollar un algoritmo que lea 10 números e imprimir solamente los números positivos. 
# (se imprime dentro del ciclo, si el usuario ingresa un número positivo se imprime, 
# sino ingresa un número positivo, no se imprime nada y se pide el número siguiente)

for i in range(0,10):
    num=float (input("Ingrese un numero por favor: "))
    if num>0:
        print(num)

print("Fin")