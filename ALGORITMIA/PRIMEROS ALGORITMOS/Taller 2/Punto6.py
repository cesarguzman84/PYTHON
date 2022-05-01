#6)	Un amigo suyo acaba de iniciar un negocio de venta de zapatos. 
# Por ahora sólo vende tres tipos de zapatos: sandalias con un valor de $100,
#  tenis con un valor de $200 y mocasines con un valor de $300.
#  Cuando un cliente llega le dice la cantidad que desee de cada uno de ellos . 
# El cliente tiene derecho a un 8% de descuento sobre la compra que realiza. 
# Ayúdele a su amigo a crear un programa que, para un cliente dado, muestre su nombre, 
# el valor de la venta sin descuento, el descuento, 
# valor de la venta con descuento y valor de la venta incluyendo IVA (venta neta final)

nombre =input("Introduce el nombre del cliente por favor ")
sandalias = int(input("Introduce el numero de sandalias a comprar "))
tenis = int (input("Introduce el numero de tenis a comprar "))
mocasines = int(input("Introduce el numero de mocasines a comprar "))

sin_descuento = ((sandalias*100)+(tenis*200)+(mocasines*300))

descuento =sin_descuento*0.08

con_descuento = sin_descuento-descuento

iva = sin_descuento*0.19

valor_final=con_descuento+iva

print("Nombre del cliente: " + nombre)
print("El valor de la venta sin descuento es " + str(sin_descuento))
print("El valor del descuento es " + str(descuento))
print("El valor de la venta con descuento es " + str(con_descuento))
print("El valor final de la venta con el IVA es " + str(valor_final))

