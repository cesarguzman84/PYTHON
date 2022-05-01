import sqlite3 as sql

def createBD():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers(
        name text,
        followers integer,
        subs integer
        )"""
    )
    conn.commit()
    conn.close()
    
    
def insertRow(nombre, folowers, subs):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion =f"INSERT INTO streamers VALUES ('{nombre}', {followers}, {subs})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    
    
if __name__== "__main":
    #createBD()
    #createTable()
    insertRow("Ibai", 700000, 250000)
    
    