import sqlite3

conexion = sqlite3.connect("bd1.db")

conexion.execute("insert into articulos(descripcion, precio) values(?,?)", ("Naranjas", 25))
conexion.execute("insert into articulos(descripcion, precio) values(?,?)", ("Peras", 34))
conexion.execute("insert into articulos(descripcion, precio) values(?,?)", ("Bananas", 30))
conexion.commit()
conexion.close()