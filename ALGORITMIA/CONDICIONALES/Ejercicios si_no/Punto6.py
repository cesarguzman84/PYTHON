#6)	Elaborar un algoritmo que permita el login (inicio de sesión) en una red social. 

#Nota: Debe crear una variable con el nombre de usuario y otra con la contraseña.

user = "Cesar"
passw = "12345"

usuario = input ("Ingrese el nombre del usuario por favor: ")
contrasena = str(input("Ingrese la contraseñapor favor: "))

if user == usuario and passw == contrasena:
    print("Bienvenido")
else:
    print("Datos incorrectos")
