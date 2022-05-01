#Determinar cuánto pagará finalmente una persona por un artículo equis, 
# considerando que tiene un descuento de 20%, y debe pagar 19% de IVA 
# (debe mostrar el precio con descuento y el precio final, el descuento se aplica una vez el producto
#  tenga el iva aplicado).

precio=int(input("Introduce por favor el precio del articulo "))
IVA = precio*0.19
descuento = (precio+IVA)*0.2
precio_descuento= precio-descuento

print("El precio con descuento es " + str(precio_descuento))
