"""9.	Se tiene un grupo de registros, no se conoce cuantos, cada registro contiene el nombre, la edad, estatura, peso, sexo (1=hombre, 2=mujer), deporte (1=natación, 2= fútbol, 3=ciclismo, 4=patinaje, 5=otro deporte). Elabore un algoritmo que imprima:
•	Promedio de edad de las personas que prefieren el fútbol.
•	Porcentaje que representan las mujeres que prefieren el ciclismo respecto a las personas de ciclismo.
•	Nombre de la mujer más alta en patinaje.
•	Cuantos de los que practican natación, pesan menos de 50 kg y miden más de 1.80 mts.
•	Promedio de edad de todas las personas sin importar el deporte que practiquen."""

edadFutbol=0
edad = 0
contTotal=0
contciclismomujer=0
contTciclismo=0
estatura=0
mayorAltura=0
nombreMayorAltura=''
cont50180=0
edadTotal=0
contFutbol=0
PromedioEdadTotal=0
MujeresCiclismo=0
PromedioEdadFutbol=0

pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))

while pregunta==1:
    nombre=str(input('Ingresa tu nombre =>'))
    edad = int(input('Ingresa tu edad =>'))
    estatura=float(input('Ingresa tu estatura =>'))
    genero = str(input('1=>hombre 2=>mujer =>'))
    peso = int (input('Ingresa tu peso =>'))
    depo=str(input('Ingresa tu deporte =>'))
    edadTotal = edadTotal+edad
    if depo=='1':
        contTotal=contTotal+1
        if peso<50 and estatura >1.80:
            cont50180=cont50180+1
            print('Natacion')
    if depo == '2':
        contTotal=contTotal+1
        contFutbol=contFutbol+1
        edadFutbol=edadFutbol+edad
        print('Futbol')
    if depo =='3':
        contTotal=contTotal 
        contTciclismo=contTciclismo+1
        if genero=='2':
            contciclismomujer
    if depo=='4':
        contTotal = contTotal+1
        if genero =='2' and mayorAltura<estatura:
            mayorAltura=estatura
            nombreMayorAltura=nombre
        print('patinaje')

    if depo=='5':
        contTotal=contTotal+1
        print('otro deporte')
    pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))

    if(contFutbol>0) :

        PromedioEdadFutbol= edadFutbol/contFutbol

if(contTciclismo>0):
    MujeresCiclismo=(contciclismomujer/contTciclismo)*100

if(contTotal>0):
    PromedioEdadTotal=edadTotal/contTotal

print("Promedio de edad de las personas que prefieren el futbol :", PromedioEdadFutbol)
print("Porcentaje que representan las mujeres que prefieren el ciclismorespecto a las personas de ciclismo :", MujeresCiclismo)
print("Nombre de la mujer mas alta en patinaje :", nombreMayorAltura)
print("Cuantos de los que practican natacion, pesan menos de 50 kg y miden mas de 1.8 mtrs :", cont50180)
print("Promedio de edad de todas las personas sin importar el deporte que practiquen:", PromedioEdadTotal)

