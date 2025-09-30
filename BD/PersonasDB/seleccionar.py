import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='personas_db'
)

mi_cursor = personas_db.cursor()
mi_cursor.execute('SELECT * FROM personas')
resultado = mi_cursor.fetchall()
for persona in resultado:
    print(persona)

personas_db.close()