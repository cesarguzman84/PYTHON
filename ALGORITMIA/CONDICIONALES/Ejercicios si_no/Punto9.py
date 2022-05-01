#9)	Elaborar un algoritmo que muestre un menú que contemple las opciones “Archivo”, “Buscar” y “Salir”, en caso de que no se introduzca una opción correcta se notificará por pantalla.

menu = input(("Seleccione una opcion:\n Archivo, Buscar, Salir\n").lower())

if menu == "archivo":
    print("Usted selecciono archivo ")
elif menu == "buscar":
    print("Usted selecciono buscar ")
elif menu == "salir":
    print("Usted selecciono salir ")
else:
    print("Error")