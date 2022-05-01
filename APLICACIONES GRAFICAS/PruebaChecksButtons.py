from tkinter import *


root=Tk()

root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def opcionesViaje():
    
    opcionEscogida=""
    
    if(playa.get()==1):
        opcionEscogida+=" playa"
    
    if(montagna.get()==1):
        opcionEscogida+=" montaña"
    
    if(turismoRural.get()==1):
        opcionEscogida+=" turismo Rural"
    
    textoFinal.config(text=opcionEscogida)

frame=Frame(root)
frame.pack()

Label(frame, text="Elige Destino", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal= Label(frame)
textoFinal.pack()

root.mainloop()