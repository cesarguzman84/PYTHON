# 3.	Elabore un algoritmo que lea para un grupo de 15 personas el nombre y la edad, e imprima por cada una el nombre y un mensaje que imprima si es mayor o menor de edad.

conta=0
while conta<=15:
    nombre=str(input('Ingresa nombre =>'))
    edad = int(input('Ingresa la edad =>'))
    if edad>=18:
        print("Nombre: ", nombre)
        print("Es mayor de edad")
    else:
        print("Nombre: ", nombre)
        print("Es menor de edad")
    
    conta=conta+1
    