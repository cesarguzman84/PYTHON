# 6)	lea 5 números por teclado, los copie a otro array multiplicados por 2 y muestre el segundo array.

numeros=[]
numerosx2 =[]

for i in range (0,5):
    numeros.append(int(input('Ingrese un numero entero: ')))

print(numeros)

for i in range(0,5):
    numerosx2.append(numeros[i]*2)

print('---------array multiplciado X2')
print(numerosx2)