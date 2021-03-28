print("asignaturas optativas")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower() #CONVIERTE ASIGNATURA EN MINISCULAS

if asignatura in ("Informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):

	print("Asignatura elegida " + asignatura)
else:
	print("Materia no valida")