# 10)	 Una compañía fabrica focos de colores (verdes, blancos y rojos). Se desea contabilizar, de un lote de N focos, el número de focos de cada color que hay en existencia. Desarrolle un algoritmo para determinar esto

sumaverde =0
sumablanco = 0
sumarojo = 0
lote = int(input("Ingrese el numero de focos del lote: "))

for i in range(1,lote+1):
    color =input(f"ingrese el color del foco {i}: ")
    if color == "verde":
        sumaverde=sumaverde+1
    elif color == "blanco":
        sumablanco = sumablanco+1
    elif color == "rojo":
        sumarojo = sumarojo +1
    else:
        print ("Error, valide el color ")

print("El numero de focos verdes es: ", sumaverde)
print("El numero de focos blancos es: ", sumablanco)
print("El numero de focos rojos es: ", sumarojo)
