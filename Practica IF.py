print("Programa de evaluacion de notas de alumnos")

nota_alumno=input("Introduce la nota del alumno ")

def evaluacion(nota): #FUNCION EVALUACION
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion
print(evaluacion(int(nota_alumno))) #CONVIERTE nota_alumno EN UN VALOR NUMERICO