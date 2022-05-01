#7.	En una universidad, cada que se matricula un estudiante se elabora un registro con el número del carné, la cantidad de materias matriculadas y el estrato social al que pertenece, Elabore un algoritmo que imprima por cada estudiante el carné y el valor de la matrícula, teniendo en cuenta que si el número de materias es superior a 5 y el estrato social es igual a 1 se le hace un descuento del 20 %. Cada materia tiene un valor de $100.000 (solo se hace descuento si cumple con las condiciones de tener estrato 1 y matricular más de 5 materias, sino lo hace, el cobro es normal sin descuento para cualquier estrato)

pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))

while pregunta==1:
    nombre=str(input('Ingresa nombre del alumno =>'))
    carne = int(input('Ingresa el numero del carne =>'))
    materias = int(input('Ingresa numero de materias matriculadas =>'))
    estrato = int(input('Ingresa el estrato al que pertenece el alumno =>'))
    valor_materia= 100000

    if materias > 5 and estrato==1:
        valor_sin_descuento= materias*valor_materia
        descuento= valor_sin_descuento*0.2
        nuevo_precio = valor_sin_descuento-descuento
        print("Numero de carné: ", carne)
        print("Valor matricula: ", nuevo_precio)
        pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))    
    
    else:
        valor_sin_descuento= materias*valor_materia
        print("Numero de carné: ", carne)
        print("Valor matricula: ", valor_sin_descuento)
        pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>')) 

        
    