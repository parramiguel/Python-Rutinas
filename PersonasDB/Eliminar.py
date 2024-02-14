import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='personas_db'
)
cursor = personas_db.cursor()
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
valores = (2,)
cursor.execute(sentencia_sql,valores)
personas_db.commit()
print('Se ha eliminado con éxito...')
personas_db.close()