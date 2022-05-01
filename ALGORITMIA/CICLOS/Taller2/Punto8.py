# 8.	Un empresario del transporte cuenta con 30 vehículos entre buses, busetas y colectivos. Al final del día se elabora por cada vehículo un registro con la placa, el tipo (1= bus, 2= buseta, 3= colectivo) y el número de pasajeros transportados. Elabore un algoritmo que imprima por cada vehículo la placa, el dinero recolectado y el pago para el conductor que es el 20 % del total recolectado. También tenga en cuenta que el precio del pasaje en Bus es de $1800, en Buseta es de $ 2000 y en Colectivos es de $2200

conta=0
while conta<=30:
    placa=str(input('Ingresa la placa del vehiculo =>'))
    tipo = int(input('Ingresa el tipo de vehiculo:\n Bus=1\n Buseta=2\n colectivo=3\n  =>'))
    pasajeros = int(input('Ingresa el numero de pasajeros  =>'))
    
  
    if tipo == 1:
        dinero_recogido= pasajeros*1800
        pago_conductor =dinero_recogido*0.2
        print("El dinero recogido para el veiculo con placa: " + placa + " es de " + str(dinero_recogido))
        print("El salario de este conductor es de ", pago_conductor)    
    
    elif tipo == 2:
        dinero_recogido= pasajeros*2000
        pago_conductor =dinero_recogido*0.2
        print("El dinero recogido para el veiculo con placa: " + placa + " es de " + str(dinero_recogido))
        print("El salario de este conductor es de ", pago_conductor)

    elif tipo == 3:
        dinero_recogido= pasajeros*2200
        pago_conductor =dinero_recogido*0.2
        print("El dinero recogido para el veiculo con placa: " + placa + " es de " + str(dinero_recogido))
        print("El salario de este conductor es de ", pago_conductor)
        
        
    conta=conta+1