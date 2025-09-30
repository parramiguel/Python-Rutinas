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
        valores = ("Angela Maria", "Galea Caldera", "agalea@gmail.com", 1)
        cursor.execute(sentencia, valores)
        registros_actualizados = cursor.rowcount
        print(f"Registros actualizados: {registros_actualizados}")

