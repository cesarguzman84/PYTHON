#8)	Lea 10 nombres por teclado, los almacene en un array, lea la edad correspondiente de cada nombre, los almacena en un array, y al final debe mostrar todos los nombres y todas las edades respectivamente. Ejemplo:

#Pepito tiene 15 años
#Lola tiene 28 años

nombres=[]
edades=[]

for i in range(0,10):
    nombres.append(str(input('Por favor ingrese su nombre: ')))
    edades.append(int(input('Por favor ingrese su edad: ')))

for i in range(0,10):
    print(f'{nombres[i]} tiene {edades[i]} años')