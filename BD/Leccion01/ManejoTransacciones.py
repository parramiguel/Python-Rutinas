import psycopg2

conexion = psycopg2.connect(
    user="postgres", password="postgres",
    host="localhost", port="5432", dbname="test_db"
)
cursor = conexion.cursor()
conexion.autocommit = False
try:
    sentencia = (
        "INSERT INTO persona (nombre, apellido, email) "
        "VALUES (%s, %s, %s)"
    )
    valores = ("Maria", "Esparza", "mesparza@mail.com")
    cursor.execute(sentencia, valores)
    conexion.commit()
    print("Transacción completada exitosamente")
except Exception as e:
    conexion.rollback()
    print("Ocurrió un error. Se hizo rollback de la transacción:", e)
finally:
    cursor.close()
    conexion.close()
