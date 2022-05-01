# 14. Realice un algoritmo que determine el sueldo semanal de N trabajadores (solo es mostrar la suma de todos los sueldos) considerando que se les descuenta 5% de su sueldo si ganan entre 0 y 150 pesos. Se les descuenta 7% si ganan más de 150 pero menos de 300, y 9% si ganan más de 300 pero menos de 450 (nadie gana más de 449). Los datos son horas trabajadas, sueldo por hora y nombre de cada trabajador.


pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))

while pregunta==1:
    sueldo = int(input('Ingresa el valor del sueldo =>'))
    

    if sueldo > 0 and sueldo<150:
        descuento1=sueldo*0.05
        nuevosueldo1= sueldo-descuento1
        pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))
            
    
    elif sueldo>150 and sueldo<300:
        descuento2= sueldo*0.07
        nuevosueldo2=sueldo-descuento2
        pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))
        
pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))

print("El numero de ventas entre 0 y 10.000 fue:", )
print("El valor de las ventas entre 0 y 10.000 fue:", )
print("El numero de ventas entre 10.000 y 20.000 fue:", )
print("El valor de las ventas entre 10.000 y 20.000 fue:", )