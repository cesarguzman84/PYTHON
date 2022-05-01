#Funciones sin retorno de valor

def saludar():
    print("Hola amigo")
        
saludar()

##############################

def saludar1(nombre):
    print(f"Hola {nombre}")
    
saludar1("César")

###############################

def tabla_multiplicar(num):
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")

tabla_multiplicar(5)
print()
tabla_multiplicar(3)

print("------------------------------------------------------")

#Funciones con retorno de valor:

def multiplicar(num1,num2):
    mult = num1*num2
    return mult

mult = multiplicar(3, 4)

print(mult)

print(multiplicar(5, 89))


print("------------------------------------------------------")

