import sqlite3

conexion=sqlite3.connect("bd1.db")
codigo=int(input("Ingrese el código de un artículo:"))
registro=conexion.execute("select descripcion,precio from articulos where codigo=?", (codigo, ))
fila=registro.fetchone()
if fila!=None:
    print(fila)
else:
    print("No existe un artículo con dicho código.")
conexion.close()