import psycopg2

with psycopg2.connect(
    user="postgres", password="postgres",
    host="localhost", port="5432", dbname="test_db"
) as conexion:
    with conexion.cursor() as cursor:
        sentencia_insert = (
            "INSERT INTO persona (nombre, apellido, email) "
            "VALUES (%s, %s, %s)"
        )
        valores_insert = ("Alex", "Rojas", "arojas@mail.com")
        cursor.execute(sentencia_insert, valores_insert)
        sentencia_update = (
            "UPDATE persona "
            "SET nombre=%s, apellido=%s, email=%s "
            "WHERE id_persona=%s"
        )
        valores_update = ("Juan", "Perez", "jperez@mail.com", 1)
        cursor.execute(sentencia_update, valores_update)
print("Termina la transacción, se hizo commit")

