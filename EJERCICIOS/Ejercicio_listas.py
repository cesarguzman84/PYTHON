#Ejercicio 1 - Eliminar los elementos repetidos de una lista

lista = [1,2,3, "Lina", 2,1,2, "Lina",3]

print(lista)

conjunto = set(lista)

lista = list(conjunto)

print(lista)

#otra forma:

lista1 = [1,2,3, "Lina", 2,1,2, "Lina",3]

lista1 = list(set(lista1))

print(lista1)