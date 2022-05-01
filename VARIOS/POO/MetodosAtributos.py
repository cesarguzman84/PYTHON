class  FabricaTelefonos():
    marca = "Huawei"        #Estos son atributos
    color = "Negro"         #Estos son atributos (una caracteristica del objeto)
    memoriaRam = 32         #Estos son atributos
    almacenamiento = 128    #Estos son atributos
    
    def llamar(self, mensaje):           #Esto es un metodo (lo que puede hacer el objeto)
        return mensaje
    
    def escucharMusica(self):
        print("Estas escuchando música")
    
telefono = FabricaTelefonos() #Este es el objeto telefono
telefono.marca
telefono.color
telefono.memoriaRam
telefono.almacenamiento

print(telefono.llamar("Hola, ¿con quien hablo?"))
telefono.escucharMusica()
print(telefono.marca)
    