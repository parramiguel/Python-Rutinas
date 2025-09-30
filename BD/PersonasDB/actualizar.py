import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='personas_db'
)

cursor = personas_db.cursor()
sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
valores = ('Victor', 'Capuccio', 45, 5)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha modificado la información...')
personas_db.close()
