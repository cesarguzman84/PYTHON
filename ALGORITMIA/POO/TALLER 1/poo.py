class persona:
    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre=nombre
        self.edad =edad
        self.sexo=sexo
        self.peso=peso
        self.altura=altura

    def calcularIMC(self):
        self.peso=self.peso/(self.altura*self.altura)
        if self.peso<20:
            return -1
        elif self.peso>=20 and self.peso<=25:
            return 0
        else:
            return 1
    def esMayorDeEdad(self):
        if self.edad>17:
            return True
        else:
            return False
    def comprobarSexo(self):
        if self.sexo!="H" and self.sexo!="M":
            self.sexo="H"
    def generaCC(self):
        import random
        self.cc=random.randrange(00000000,99999999)

#main
sexo=str(input("Ingrese su sexo: "))
nombre= str(input("Ingrese su nombre: "))
edad=int(input("Ingrese su edad: "))
altura= float(input("Ingrese su altura, por ejemplo 1.80: "))
peso=float(input("Ingrese su peso en kg, por ejemplo 70.5: "))

a= persona(nombre, edad, sexo, peso, altura )
respuesta=0
respuesta=a.calcularIMC()
if respuesta==-1:
    print("Estas en tu peso ideal")
elif respuesta==0:
    print("Estas por debajo de tu peso ideal")
else:
    print("Tienes sobrepeso")

respuesta=a.esMayorDeEdad()
if respuesta==True:
    print("Usted es mayor de edad")
if respuesta==False:
    print("Usted es menor de edad ")

a.comprobarSexo()
print(f"Usted es del sexo {a.sexo}")

a.generaCC()
print(f"Su cedula se genero correctamente y es {a.cc}")