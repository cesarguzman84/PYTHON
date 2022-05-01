#6)	Desarrollar un algoritmo que calcule e imprima la tabla de multiplicar de un número ingresado por el usuario e imprimir el multiplicando, el multiplicador (va de 1 hasta 10) y el producto. 


#Ejemplo: 2x1=2  
#               2x2=4
#               2x3=6
#               Etc….

num=float(input("Ingrese un numero: "))

for i in range(1,11):
    resultado = num*i
    print(f"{num}X{i}={resultado}")