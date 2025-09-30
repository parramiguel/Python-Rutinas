import psycopg2

with psycopg2.connect(
    user="postgres", password="postgres",
    host="localhost", port="5432", dbname="test_db"
) as conexion:
    with conexion.cursor() as cursor:
        entrada = input("Proporciona los id_persona a eliminar separados por coma: ")
        valores = tuple(entrada.split(','))
        placeholders = ','.join(['%s'] * len(valores))
        sentencia = f"DELETE FROM persona WHERE id_persona IN ({placeholders})"
        cursor.execute(sentencia, valores)
        registros_eliminados = cursor.rowcount
        print(f"Registros eliminados: {registros_eliminados}")