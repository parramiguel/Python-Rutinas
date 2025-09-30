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
        database="test_db"
    )
    print("Conexión exitosa")

    # Establecer la codificación UTF-8 para la conexión
    connection.set_client_encoding('UTF8')

    cursor = connection.cursor()
    sentencia = "SELECT * FROM persona"
    cursor.execute(sentencia)
    registros = cursor.fetchall()
    
    # Imprimir registros manejando posibles problemas de codificación
    for registro in registros:
        # Convertir cada elemento del registro a string manejando la codificación
        registro_str = []
        for item in registro:
            if isinstance(item, str):
                try:
                    registro_str.append(item)
                except UnicodeEncodeError:
                    registro_str.append(item.encode('utf-8', errors='replace').decode('utf-8'))
            elif item is None:
                registro_str.append('NULL')
            else:
                registro_str.append(str(item))
        print(tuple(registro_str))

except Exception as ex:
    print(f"Error: {ex}")
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
print("La conexión ha finalizado")