a = frozenset(("Juan","Marta","Raquel","Luis","Pedro"))
b = frozenset(("Ana","Roberto","Alfonso","Diana"))
c = frozenset(("Anselmo","Miguel","María","Sofía"))
coche = frozenset(("Juan","Marta","Alfonso","María"))

oficinas = "Oficina A", "Oficina B", "Oficina C"
empleados = (a,b,c)

for i in range(len(empleados)):
    
    conCoche = empleados[i] & coche
    noCoche = empleados[i] ^ conCoche
    print("** ",oficinas[i]," **")
    print("- Con coche: ")
    for x in conCoche:
        print(x)
    print("- Sin coche: ")
    for x in noCoche:
        print(x)
