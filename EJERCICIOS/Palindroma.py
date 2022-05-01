#Hacer un programa que determine si una palabra o frase es palindroma

cadena = input("Digite una palabra o frase: ")

#Primero, quitar los espacios en blanco:
cadena = cadena.replace(" ", "")

#Segundo, invertir la cadena:
cadena2 = cadena[::-1]

print(f"La cadena invertida es: {cadena2}")

if cadena==cadena2:
    print("La cadena es un palindromo")
else:
    print("La cadena no es un palindromo")