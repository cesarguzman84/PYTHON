# 1.Elabore un algoritmo que permita averiguar cuál es el nombre del mayor de 2 hermanos no gemelos. 
# Como datos de entrada se tiene el nombre y la edad de las 2 personas.

nombre1= input("Ingrese el nombre del hermano 1: ")
edad1= int(input("Ingrese la edad del hermano 1: "))

nombre2= input("Ingrese el nombre del hermano 2 : ")
edad2= int(input("Ingresa la edad del hermano 2 :"))

if edad1>edad2:
    print("El hermano mayor es: " + nombre1)
else:
    print("El hermano mayor es: " + nombre2)