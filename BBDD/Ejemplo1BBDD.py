import sqlite3

miConexion=sqlite3.connect("PrimeraBase") # Abrir conexion a la BBDD

miCursor=miConexion.cursor() #Crear cursor o puntero

#miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") #Crear la tabla

#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALÓN', 15, 'DEPORTES')")

#variosProductos=[
#    ("Camiseta", 10, "Deportes"),
#    ("Jarrón", 90, "Cerámica"),
#    ("Camión", 20, "Juguetería"),
#]


#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)

#miConexion.commit()

miCursor.execute("SELECT*FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

for producto in variosProductos:
    
    print(producto)

miConexion.commit()


miConexion.close() # Cerrar conexion a la BBDD