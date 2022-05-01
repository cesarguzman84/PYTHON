# 12)	 Los directivos de equis escuela requieren determinar cuál es la edad promedio de cada uno de los M salones y cuál es la edad promedio de toda la escuela. Realice un algoritmo para determinar estos promedios

pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))
edadsalon=0
sumasalon = 0
edadtotal=0
sumatotal=0
while pregunta== 1:
    edad= int(input("ingrese edad: "))
    edadsalon = edadsalon+edad
    sumasalon = sumasalon+1
    pregunta=int(input('1=> Ingresar datos\n2=>Salir\n=>'))
promedio = edadsalon/sumasalon
print("El promedio de edad es: ",promedio)