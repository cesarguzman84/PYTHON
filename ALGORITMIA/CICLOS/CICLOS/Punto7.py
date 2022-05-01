#7)	Se tiene el nombre y la edad de 3 personas y se desea saber si dentro de ellas hay por lo menos una que sea menor de edad e imprimir Un mensaje que diga “si se encontró un menor de edad” y su nombre. Sino “no hay ningún menor de edad” NOTA, DEBE ROMPER EL CICLO AL ENCONTRAR UN MENOR DE EDAD.

for i in range(0,3):
    nombre =str(input("Ingrese el nombre: "))
    edad=int(input(f"Ingrese la edad de  {nombre} "))

    if edad<18:
        print("Si se encontro un menor de edad")
        break
    elif edad>=18 and i==2:
        print("no encontre")