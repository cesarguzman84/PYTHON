# 1)	Crea un programa que pida al usuario un código de usuario y una contraseña. Deberá repetirse hasta que el código sea “1” y la contraseña sea “1234”.

usuario = input("Ingrese su usuario: ")
contrasena= input("Ingrese la contraseña: ")

while usuario != "Pepito" or contrasena !="1234" :
   
    print("Usuario o contraseña incorrecto, favor intente de nuevo")
    usuario = input("Ingrese su usuario: ")
    contrasena= input("Ingrese la contraseña: ") 
print("Bienvenido")       