import psycopg2

with psycopg2.connect(
    user="postgres", password="postgres",
    host="localhost", port="5432", dbname="test_db"
) as conexion:
    with conexion.cursor() as cursor:
        entrada = input("Proporciona los id's a buscar (ej. 1,2,3): ")
        # Ej. ids: ('1', '2')
        ids = tuple(entrada.split(','))
        # Ej. SELECT * FROM persona WHERE id_persona IN (%s, %s)
        sentencia = f"SELECT * FROM persona WHERE id_persona IN ({', '.join(['%s']*len(ids))})"
        print(f'sentencia: {sentencia}')
        cursor.execute(sentencia, ids)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
