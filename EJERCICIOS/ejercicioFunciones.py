#Desarrollar un programa que pueda calcular el valor del tipo de cambio de moneda

def cambio_Pesos_Dolares(Pesos):
    return Pesos/4000

def cambio_Dolares_Pesos(Dolares):
    return Dolares*4000

while True:
    print("""\t.:MENU:.
1. Convertir Pesos a Dolares
2. Convertir de Dolares a Pesos
3. Salir""")
    opcion = int(input("Digite una opcion: "))
    
    print()
    
    if opcion ==1 :
        Pesos = float(input("Digite la cantidad de Pesos: "))
        print(f"Dolares -> ${cambio_Pesos_Dolares(Pesos):.2f}")
    
    elif opcion == 2:
        Dolares = float(input("Digite la cantidad de dólares: "))
        print(f"Pesos -> P/{cambio_Dolares_Pesos(Dolares):.2f}")
    
    elif opcion == 3:
        break
    
    else:
        print("Se equivoco de opcion de menu")
    
    print()