edad=int(input("introduce edad: "))

while edad<5 or edad>100:
	print("Has introducido una edad incorrecta. Vuelve a intentarlo")
	edad=int(input("introduce edad: "))

print("Puedes pasar")
print("Edad del aspirante " + str(edad))