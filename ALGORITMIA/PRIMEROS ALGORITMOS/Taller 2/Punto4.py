#4)	Una modista, para realizar sus prendas de vestir, encarga las telas al extranjero. 
#Para cada pedido, tiene que proporcionar las medidas de la tela en pulgadas,
# pero ella generalmente las tiene en metros. 
# Realice un algoritmo para ayudar a resolver el problema, 
# determinando cuantas pulgadas debe pedir con base en los metros que requiere. (1 pulgada = 0.0254 m).

tela_metros = int(input("Ingrese los metros de tela que desea pasar a pulgadas "))

tela_pulgadas = str((tela_metros/0.0254))

print("La tela en pulgadas mide: " + tela_pulgadas)