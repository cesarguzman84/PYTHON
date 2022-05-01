#Excepciones

try:
    numero = int(input("Digite un numero: "))
    print(f"La suma es: {numero+10}")
except:
    print("Ha ocurrido un error")
    
print("Programa terminado")