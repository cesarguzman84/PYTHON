# La compañía de luz y sombras (CLS) requiere determinar el pago que debe realizar una 
# persona por el consumo de energía eléctrica, la cual se mide en kilowatts (KW).

kw = int(input("Introduce el numero de kw consumidos "))
precio = int(input("Introduce el precio por kw "))
pago = kw*precio

print("El usuario debe pagar" + str(pago) )