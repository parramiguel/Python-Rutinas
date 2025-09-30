import psycopg2
from psycopg2 import DatabaseError

connection = None
cursor = None

try:
    connection = psycopg2.connect(
        host='localhost',
        user="postgres",
        password="postgres",
        port="5432",
        database="test_db",
        # client_encoding='UTF8'

    )
    print("Conexión exitosa")

    cursor = connection.cursor()
    sentencia = "SELECT * FROM persona"
    cursor.execute(sentencia)
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)

except Exception as ex:
    print(f"Error: {ex}")
finally:
    if cursor is not None:
        cursor.close()
if connection is not None:
    connection.close()  # Se cerró la conexión a la base de datos
print("La conexión ha finalizado")
