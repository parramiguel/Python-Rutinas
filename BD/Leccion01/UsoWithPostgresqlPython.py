import psycopg2

with psycopg2.connect(
    user="postgres", password="postgres",
    host="localhost", port="5432", dbname="test_db"
) as conexion:
    with conexion.cursor() as cursor:
        sentencia = "SELECT * FROM persona"
        cursor.execute(sentencia)
        registros = cursor.fetchall()
        print(registros)
