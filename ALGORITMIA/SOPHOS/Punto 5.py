#Realice un algoritmo que permita leer los elementos de una matriz de tamaño M x N
#y escriba en pantalla los elementos de esta elevados a la potencia 2.

import numpy as np

a = np.array([ [1,1],
               [0,1] ])
result = np.linalg.matrix_power(a, 2)
print(result)