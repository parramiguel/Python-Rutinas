import psycopg2

with psycopg2.connect(
    user="postgres", password="postgres",
    host="localhost", port="5432", dbname="test_db"
) as conexion:
    with conexion.cursor() as cursor:
        sentencia = "DELETE FROM persona WHERE id_persona=%s"
        entrada = input("Proporciona el id_persona a eliminar: ")
        valores = (entrada,)
        cursor.execute(sentencia, valores)
        registros_eliminados = cursor.rowcount
        print(f"Registros eliminados: {registros_eliminados}")
