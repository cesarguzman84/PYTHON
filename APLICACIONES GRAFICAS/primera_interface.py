from tkinter import *

raiz= Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(0,0) #para impedir que se modifique el tamaño la ventana

#raiz.iconbitmap("mario.ico")

#raiz.geometry("650x350") 

raiz.config(bg="blue")

miFrame = Frame()

miFrame.pack(side="right", anchor="s")

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd=35) #Borde del frame

miFrame.config(relief="groove")

raiz.mainloop()