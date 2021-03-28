lunes = 24, 24.8, 25, 25, 24.6
martes = 23.7, 24.2, 24, 23.6, 23
miercoles = 24, 24, 23.5, 22, 21
jueves = 22, 23.8, 25, 24.8, 24.6
viernes = 25, 25.5, 26, 26, 25.6
sabado = 25, 25.8, 26.5, 26.5, 26
domingo = 25, 26, 26.7, 27, 26.6

muestras = lunes, martes, miercoles, jueves, viernes, sabado, domingo
dias = "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"

maxima = muestras[0][0]
minima = muestras[0][0]
suma = 0
for i in range(len(dias)):
    print("*** ",dias[i]," ***")
    print("Máxima: ",max(muestras[i]))
    print("Mínima: ",min(muestras[i]))
    print("Media: %.2f" % (sum(muestras[i])/len(muestras[i])))
    print("\n")

    suma = suma + sum(muestras[i])
    if max(muestras[i]) > maxima:
        maxima = max(muestras[i])
    if min(muestras[i]) < minima:
        minima = min(muestras[i])

print("*** Semana: ***")
print("Máxima: ",maxima)
print("Mínima: ", minima)
print("Media: %.2f" % (suma / (len(muestras)*len(muestras[0])) ))
