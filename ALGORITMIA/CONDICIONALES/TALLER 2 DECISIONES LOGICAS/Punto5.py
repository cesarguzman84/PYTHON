#5.	Se tienen el área, el valor del metro cuadrado de una propiedad y la forma de pago de la cuota inicial.
#  Se pide calcular el precio de venta de la propiedad y el valor de la cuota inicial, 
# que sería el 20% del valor del precio de venta. 
# Si la forma de pago es 1, se otorga un descuento del 10% sobre la cuota inicial y 
# si la forma de pago es 2, se le recarga un 8% en el valor de la misma. 
# Mostrar el valor del precio de venta y el de la cuota inicial de la propiedad (solo hay 2 formas de pago).

area = int(input("Ingrese el area de la casa: "))
valorm2= int(input("Ingrese el valor del m2: "))
forma_pago = int(input("Ingrese si la forma de pago es 1 o 2: "))
precio = area*valorm2
cuota_inicial = precio*0.2

if forma_pago ==1:
    descuento_cuota =cuota_inicial*0.1
    nueva_cuota= cuota_inicial-descuento_cuota
    precio_final= precio-nueva_cuota
    print("El valor total de la casa con la forma de pago 1 es: " + str(precio_final))
elif forma_pago ==2:
    aumento_cuota = cuota_inicial*0.08
    nueva_cuota = cuota_inicial+aumento_cuota
    precio_final = precio + nueva_cuota
    print("El valor total de la casa con la forma de pago 2 es: " + str(precio_final))
else:
    print("error, introduzca una forma de pago valida")

