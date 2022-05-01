#Listas

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

lista.append("Sabado")

lista.insert(4, "Juernes")

lista.extend([1,2,3,4,5,1,2,1,1,1,2])

print(lista[3])
print(lista) 
print(lista.count(1))   

lista.pop(4)
print(lista)

lista.remove(1)
print(lista)

lista.reverse()
print(lista)

lista1= [5,4,-7,2.8,10,13,1,0]
lista1.sort()
print(lista1)

lista1.sort(reverse=True)
print(lista1)