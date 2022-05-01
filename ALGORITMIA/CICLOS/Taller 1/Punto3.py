# 3)	Escribir un programa que realice la pregunta ¿Desea continuar S/N? y que no deje de hacerla hasta que el usuario teclee N.

pregunta = (input("¿Desea continuar S/N? ")).lower()

while pregunta == "s" :
       
    pregunta = (input("¿Desea continuar S/N? ")).lower()
print("Fin del programa")   