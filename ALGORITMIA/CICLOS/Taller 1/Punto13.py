# 13)	 Un vendedor ha realizado N ventas y desea saber cuántas fueron por 10,000 o menos, cuántas fueron por más de 10,000 pero por menos de 20,000, y cuánto fue el monto de las ventas de cada una y el monto global. Realice un algoritmo para determinar los totales.

conta0_10=0
conta10_20=0
valor_ventas_pequenas=0
valor_ventas_grandes =0
pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))

while pregunta==1:
    venta = int(input('Ingresa el valor de la venta =>'))
    

    if venta > 0 and venta<10000:
        valor_ventas_pequenas= valor_ventas_pequenas+venta
        conta0_10 = conta0_10+1
        pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))    
    
    elif venta>10000 and venta<20000:
        valor_ventas_grandes = valor_ventas_grandes+venta
        conta10_20=conta10_20+1
        pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))
print("El numero de ventas entre 0 y 10.000 fue:",conta0_10 )
print("El valor de las ventas entre 0 y 10.000 fue:",valor_ventas_pequenas )
print("El numero de ventas entre 10.000 y 20.000 fue:",conta10_20 )
print("El valor de las ventas entre 10.000 y 20.000 fue:",valor_ventas_grandes )