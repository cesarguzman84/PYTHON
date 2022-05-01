'''
Construir un programa que simule el funcionamiento de una calculadora que puede realizar las 4 operaciones aritmeticas básicas (suma, resta, multiplicación y división). El usuario debe especificar la operación con el primer caracter del nombre de la operacion 
'''

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

operacion = input("Digite el primer digito de la operacion que desea realizar: ").lower()

if operacion == "s":
    suma= num1+num2
    print(suma)

elif operacion == "r":
    resta = num1-num2
    print(resta)
    
elif operacion == "m":
    multiplicacion = num1*num2
    print(multiplicacion)

elif operacion =="d":
    division = num1/num2
    print(division)