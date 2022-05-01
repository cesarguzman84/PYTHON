#Ingresar y leer datos en la BD
#Para ingresar datos a una base de datos, primero debemos definir la estructura de la tabla donde se almacenarán los datos

import sqlite3

#Creamos una conexion a la base de datos

conexion = sqlite3.connect("ejemplo2.db")
cursor = conexion.cursor()


#CREATE TABLE:
#Creamos una tabla llamada estudiantes
cursor.execute("CREATE TABLE estudiantes(email VARCHAR(100), nombre VARCHAR(100), edad INTEGER)")

conexion.close()


#INSERT INTO para ingresar datos:
conexion= sqlite3.connect("ejemplo2.db")

cursor = conexion.cursor()

#Insertamos un registro en la tabla:
cursor.execute("INSERT INTO estudiantes VALUES('leidy@gmail.com', 'Leidy', '33')")

#Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()



