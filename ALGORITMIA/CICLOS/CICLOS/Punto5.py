# 5)	Desarrollar un algoritmo que lea 10 números e imprimir cuántos son positivos, 
#  cuántos negativos y cuántos ceros.

contp=0
contn=0
cont0=0

for i in range(0,10):
    num = float(input("Ingrese un numero por favor: "))
    if num>0:
        contp=contp+1
    elif num <0:
        contn = contn+1
    elif num==0:
        cont0=cont0+1
print(f"---------RESULTADOS--------\nHay {contp} numeros positivos\nHay {contn} numeros negativos\nHay {cont0} numeros ceros")
