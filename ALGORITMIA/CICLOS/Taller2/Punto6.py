# 6.	Elabore un algoritmo que lea el nombre, la edad y la estatura de un grupo de 20 personas, e imprima el nombre solo de las personas que sean mayores de edad y que su estatura sea mayor de 1.80 mts. (se ingresa los datos de cada persona, si es mayor de edad y mide mas de 1.80 mts inmediatamente se imprime el nombre, sino, seguir pidiendo los datos de la siguiente persona)

conta=0
while conta<=20:
    nombre=str(input('Ingresa nombre =>'))
    edad = int(input('Ingresa la edad =>'))
    estatura = float(input('Ingresa la estatura =>'))
    if edad>=18 and estatura > 1.8:
        print("Nombre: ", nombre)
        print("Es mayor de edad")
    
    
    conta=conta+1