import sqlite3

conexion= sqlite3.connect("bd1.db")
precio= float(input("Ingrese un precio:"))
cursor = conexion.execute("select descripcion, precio from articulos where precio<?", (precio,))
fila=cursor.fetchall()
if len(filas)>0:
    for filas in filas:
        print(fila)
else:
    print("No existen articulos con un precio menos al ingresado")

conexion.close()