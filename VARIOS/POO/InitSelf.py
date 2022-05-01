class FabricaTelefonos():
    marca = "Samsung"
    
    def ElaborarHuawei(self):
        self.marca = "Huawei"

telefono = FabricaTelefonos()
telefono.ElaborarHuawei()
print(telefono.marca)

print("-----------------------------")

class FabricaTelefonos1():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        
   
        
telefono1 = FabricaTelefonos1("Huawei", "Negro")
print(telefono1.marca)
print(telefono1.color)
