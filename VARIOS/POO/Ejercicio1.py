#Ejercicio 1 Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print("Nombre: {} \nNota: {}".format(self.nombre, self.nota))
        
    def resultados(self):
        if self.nota <7:
            print("Has reprobado")
        else:
            print("Has aprobado")
            
estudiante1 = Estudiante("Lina", 10)
estudiante1.imprimir()
estudiante1.resultados()    

estudiante2 = Estudiante("Jessica", 6)
estudiante2.imprimir()
estudiante2.resultados()