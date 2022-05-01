# 4.	En un almacén, cada que se realiza una venta se elabora un registro con el nombre del artículo, el precio por unidad y la cantidad de artículos vendidos. Suponiendo que se hicieron 20 ventas, elabore un algoritmo que imprima por cada venta el nombre del artículo y el valor total de la venta. 5.	Para el mismo enunciado del ejercicio anterior, suponga que si el valor de la venta es mayor de   50000 se concede un descuento del 10 % sobre el valor de la venta.

conta=0
while conta<=20:
    nombre_articulo=str(input('Ingresa nombre del articulo =>'))
    precio_unidad = int(input('Ingresa precio por unidad =>'))
    numero_unidades = int(input('Ingresa numero de unidades vendidas =>'))
    valor_venta= precio_unidad*numero_unidades
    if valor_venta > 50000:
        valor_venta= precio_unidad*numero_unidades
        descuento= valor_venta*0.1
        nuevo_precio = valor_venta-descuento
        print("Nombre articulo: ", nombre_articulo)
        print("Valor venta: ", nuevo_precio)    
    
    else:
        valor_venta= precio_unidad*numero_unidades
        print("Nombre articulo: ", nombre_articulo)
        print("Valor venta: ", valor_venta)

        
    conta=conta+1