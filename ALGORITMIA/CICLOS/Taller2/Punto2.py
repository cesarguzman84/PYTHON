# 2.	Se tienen 10 registros, cada registro contiene el nombre, salario básico hora, el número de horas trabajadas, el total de deducciones y el total de bonificaciones. Elabore un algoritmo que imprima por cada trabajador el nombre, el salario bruto y el salario neto.

pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))

while pregunta==1:
    nombre=str(input('Ingresa nombre =>'))
    salario_hora = int(input('Ingresa salario x hora =>'))
    horas=int(input('Ingresa numero de horas trabajadas =>'))
    deducciones = int(input('Ingresa deducciones del empleado =>'))
    bonificaciones = int (input('Ingresa bonificaciones del empleado =>'))
    salarioBruto=salario_hora*horas
    salarioNeto = salarioBruto-deducciones+bonificaciones
    print("Nombre del empleado: ", nombre)
    print("Salario bruto: ", salarioBruto)
    print("Salario neto: ", salarioNeto)
    pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))
    
    

