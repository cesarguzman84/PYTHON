# 7)	lea 10 números por teclado, los almacene en un array y muestre el promedio.

array1=[]

for i in range(0,10):
    array1.append(int(input('Ingrese un numero entero: ')))

promedio=sum(array1)/len(array1)

print(f'El promedio es {promedio}')