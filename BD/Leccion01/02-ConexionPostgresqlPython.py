import psycopg
conexion = psycopg.connect(
    user="postgres",
    password="admin",
    host="localhost",
    port="5432",
    dbname="test_db"
)
# print(conexion)
cursor = conexion.cursor()
sentencia = "SELECT * FROM persona"
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()
