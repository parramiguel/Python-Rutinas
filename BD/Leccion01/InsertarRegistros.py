import psycopg2

with psycopg2.connect(
    user="postgres", password="postgres",
    host="localhost", port="5432", dbname="test_db"
) as conexion:
    with conexion.cursor() as cursor:
        sentencia = (
            "INSERT INTO persona (nombre, apellido, email) "
            "VALUES (%s, %s, %s)"
        )
        valores = ("Miguel José", "Parra Sojo", "ingparrasojo@gmail.com")
        cursor.execute(sentencia, valores)
        # conexion.commit()
        registros_insertados = cursor.rowcount
        print(f"Registros insertados: {registros_insertados}")
