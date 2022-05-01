#Llenar una lista con los numeros del 1 al 50, luego mostrarl la lista con un bucle for

lista = []

i = 1

#Agregamos a lal list alos elementos del 1 al 50:
while i<50:
    lista.append(i)
    i+=1
#imprimiento los elementos de la lista:
for i in lista:
    print(i, end="-")
    
    
print("-------------------------------------------------")

#otra forma:
#Agregamos a lal list a los elementos del 1 al 50:
lista = list(range(1,51))

#imprimiento los elementos de la lista:
for i in lista:
    print(i, end="-")