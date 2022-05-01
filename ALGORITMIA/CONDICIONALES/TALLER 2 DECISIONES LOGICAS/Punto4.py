#4.	Se necesita un programa que diga si una persona es apta para un equipo de baloncesto o no, 
# para que sea apto debe cumplir que si es hombre sea mayor de edad, que mida más de 1.70 mts., 
# que pese menos de 75 kg., 
# o si es mujer que tenga más de 16 años, que mida como mínimo 1.70 y que pese como máximo 60 kg. 
# Se debe leer el nombre, el sexo (F = femenino, M = masculino), la edad, la estatura y el peso

nombre = input("Favo ingrese el nombre de la persona: ")
genero = input(("Ingrese genero (Femenino/Masculino): ").lower())
estatura = int(input("Ingrese estatura en cms: "))
peso = int(input("Ingrese peso en kg: "))
edad = int(input("Ingrese edad: "))

if genero == "masculino":
    if edad >= 18 and estatura >= 170 and peso<=75:
        print(nombre + " de sexo " + genero + ", edad " + str(edad) + " años , estatura " + str(estatura) + " cms" + " y con un peso de " + str(peso)+ " kg, es APTO para el equipo de baloncesto")
    else:
        print(nombre + " no es apto para el equipo de baloncesto")
elif genero == "femenino":
    if edad >=16 and estatura>=170 and peso<=60:
        print(nombre + " de sexo " + genero + ", edad " + str(edad) + " años, estatura " + str(estatura) + " cms" + " y con un peso de " + str(peso)+ " kg, es APTA para el equipo de baloncesto")
    else:
        print(nombre + " no es apta para el equipo de baloncesto")
else:
    print("error, valida por favor el genero")