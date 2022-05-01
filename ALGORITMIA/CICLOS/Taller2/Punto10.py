#10.	Para una cantidad desconocida de registros, se lee: nombre, edad, sexo, estado civil (1=soltero, 2=casado, 3= unión libre, 4=viudo), carrera (1=sistemas, 2=programación, 3=mantenimiento, 4=diseño).
"""Elabore un algoritmo que encuentre e imprima:
a) 	Nombre de la mujer de sistemas más joven.
b) 	Nombre del hombre más viejo en sistemas.
c) 	Promedio de edad de las personas de programación que son casadas
d) 	Porcentaje que representan los menores de edad que estudian mantenimiento respecto a todas las personas de mantenimiento.
e) 	Cuantas personas de diseño son mujeres mayores de edad."""

edadMujerSistemas=0
edad = 0
contTotal=0
contMujerSistemas=0
edadHombreSistemas=0
contHombreSistemas=0
contTSistemas=0

edadProgramacionCasadas=0
contProgramacionCasados=0

edadMenorMantenimiento=0
contMenorMantenimiento=0
contTMantenimiento=0

edadMujerMayorDiseno=0
contMujerMayorDiseno=0

edadTotal=0

pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))

while pregunta==1:
    nombre=str(input('Ingresa nombre =>'))
    edad = int(input('Ingresa edad =>'))
    genero = str(input('1=>hombre 2=>mujer =>'))
    estado_civil=str(input('aEstado civil:\n1=soltero, 2=casado, 3= unión libre, 4=viudo=>'))
    carrera = str (input('Ingresa tu carrera =>\n 1=sistemas, 2=programación, 3=mantenimiento, 4=diseño'))
    
    edadTotal = edadTotal+edad
    if carrera=='1':
        contTotal=contTotal+1
        if genero==2:
            contMujerSistemas=contMujerSistemas+1
            print('Natacion')
    if carrera== '2':
        contTotal=contTotal+1
        contProgramacionCasados=contProgramacionCasados+1
        edadProgramacionCasadas=edadProgramacionCasadas+edad
        print('Futbol')
    if carrera =='3':
        contTotal=contTotal 
        
        if edad <18:
            contMenorMantenimiento=contMenorMantenimiento+1
            porcentaje = (contMenorMantenimiento/contTotal)*100
    if carrera=='4':
        contTotal = contTotal+1
        if genero =='2' and edad>=18:
            contMujerMayorDiseno= contMujerMayorDiseno+1
            
        print('patinaje')
    pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))
    

if(contMujerSistemas>0):
    MujeresCiclismo=(contMujerSistemas/contMujerSistemas)*100

if(contTotal>0):
    PromedioEdadTotal=edadTotal/contTotal

print("La mujer de sistemas mas joven es:", )
print("El hombre mas viejo de sistemas es: ",)
print("El Promedio de edad de las personas de programación que son casadas:", )
print("El Porcentaje que representan los menores de edad que estudian mantenimiento respecto a todas las personas de mantenimiento.", )
print("Las personas de diseño son mujeres mayores de edad",)

