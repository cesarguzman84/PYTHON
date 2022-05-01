#3.	Se tiene un código, número de artículos vendidos y el valor del artículo con ese código. 
# Calcule el valor de la compra, teniendo en cuenta lo siguiente: 
# si la compra es de 50 o más artículos se le da al cliente 10% de descuento; 
# si la compra es menor de 50 artículos no se hace descuento. Mostrar el código, 
# el total de la compra y el valor del descuento.

codigo = int(input("Ingrese el codigo del articulo: "))
cantidad = int(input("Ingrese la cantidad: "))
valor = int(input("Ingrese el valor: "))

if cantidad>=50:
    precio = cantidad*valor  
    descuento= precio*0.1  
    precio_descuento = precio-descuento
    print("El valor toral de la compra para el codigo " + str(codigo)+ " es: " + str(precio_descuento) + " y el valor del descuento fue de: " + str(descuento) )
else:
    precio=cantidad*valor
    print("El valor toral de la compra para el codigo " + str(codigo)+ " es: " + str(precio))
