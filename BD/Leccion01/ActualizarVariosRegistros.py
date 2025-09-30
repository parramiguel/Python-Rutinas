import psycopg2

with psycopg2.connect(
    user="postgres", password="postgres",
    host="localhost", port="5432", dbname="test_db"
) as conexion:
    with conexion.cursor() as cursor:
        sentencia = (
            "UPDATE persona "
            "SET nombre=%s, apellido=%s, email=%s "
            "WHERE id_persona=%s"
        )
        valores = (
            ("Juan", "Perez", "jperez@mail.com", 4),
            ("Ivonne", "Gutierrez", "igutierrez@mail.com", 7)
        )
        cursor.executemany(sentencia, valores)
        registros_actualizados = cursor.rowcount
        print(f"Registros actualizados: {registros_actualizados}")

