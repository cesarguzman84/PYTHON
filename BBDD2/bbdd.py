import sqlite3

#Creamos una coneccion a la base de datos

conexion = sqlite3.connect("ejemplo.db")





#Para crear una tabla, creamos una variable tipo cursor

conexion = sqlite3.connect("ejemplo.db")

#creamos el cursor

cursor = conexion.cursor()

conexion.close()

