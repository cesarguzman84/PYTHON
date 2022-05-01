# Se requiere un algoritmo para determinar cuánto ahorrará en pesos una persona diariamente, y en un año, si ahorra $3 el primero de enero, $9 el dos de enero, $27 el 3 de enero y así sucesivamente todo el año.

conta=0
ahorro=1

while conta<=365:
    ahorro = ahorro*3
    conta= conta+1
    print(ahorro)