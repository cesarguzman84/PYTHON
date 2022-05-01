# 5)	lea 10 números por teclado, 5 para un array y 5 para otro array distinto. Mostrar los 10 números en pantalla mediante un solo array.

array1=[]
array2=[]
array3=[]

for i in range(0,5):
    array1.append(int(input("Ingrese un numero entero: ")))

print('-----------array1---------')
print(array1)

for i in range(0,5):
    array2.append(int(input("Ingrese un numero entero: ")))

print('-----------array2---------')
print(array2)

for i in range(0,10):
    if i<5:
        array3.append(array1[i])
    else:
        array3.append(array2[i-5])

print('-----------array3---------')
print(array3)
