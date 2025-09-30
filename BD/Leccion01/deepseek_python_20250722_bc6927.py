import psycopg2
from psycopg2 import DatabaseError

connection = None
cursor = None

try:
    # Establecer conexión especificando la codificación del cliente
    connection = psycopg2.connect(
        host='localhost',
        user="postgres",
        password="admin",
        port="5432",
        database="test_db",
        client_encoding='UTF8'
    )
    print("Conexión exitosa")

    cursor = connection.cursor()
    sentencia = "SELECT * FROM persona"
    cursor.execute(sentencia)
    registros = cursor.fetchall()
    
    # Función para manejar la decodificación de strings
    def safe_decode(data):
        if isinstance(data, str):
            return data
        elif isinstance(data, (bytes, bytearray)):
            try:
                return data.decode('utf-8')
            except UnicodeDecodeError:
                return data.decode('latin-1')
        elif data is None:
            return 'NULL'
        else:
            return str(data)

    # Imprimir registros
    for registro in registros:
        decoded_registro = tuple(safe_decode(item) for item in registro)
        print(decoded_registro)

except Exception as ex:
    print(f"Error: {ex}")
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
print("La conexión ha finalizado")