import psycopg2

with psycopg2.connect(
    user="postgres", password="postgres",
    host="localhost", port="5432", dbname="test_db"
) as conexion:
    with conexion.cursor() as cursor:
        id_persona = input("Proporciona el valor de id_persona: ")
        sentencia = "SELECT * FROM persona WHERE id_persona = %s"
        cursor.execute(sentencia, (id_persona,))
        registro = cursor.fetchone()
        print(registro)

