contador=0
email=False

miemail=input("Introduce tu direccion de email: ") #EL PROGRAMA VALIDA SI LA DIRECCION DE EMAIL TIENE UN ARROBA O NO

for i in miemail: 

	if (i=="@" or i=="."):

		contador=contador+1
	

if contador==2:

	print("mail es correcto")
else:
	print("mail incorrecto")  