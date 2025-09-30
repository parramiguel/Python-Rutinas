import psycopg2

conexion = psycopg2.connect(
    user="postgres", password="postgres",
    host="localhost", port="5432", dbname="test_db"
)
cursor = conexion.cursor()
conexion.autocommit = False
try:
    sentencia_insert = (
        "INSERT INTO persona (nombre, apellido, email) "
        "VALUES (%s, %s, %s)"
    )
    valores_insert = ("Rocio", "Mijares", "rmijares@mail.com")
    cursor.execute(sentencia_insert, valores_insert)
    sentencia_update = (
        "UPDATE persona "
        "SET nombre=%s, apellido=%s, email=%s "
        "WHERE id_persona=%s"
    )
    valores_update = ("Juan Carlos", "Juarez", "jcjuarez@mail.com", 1)
    cursor.execute(sentencia_update, valores_update)
    conexion.commit()
    print("Transacción completada exitosamente")
except Exception as e:
    conexion.rollback()
    print("Ocurrió un error. Se hizo rollback de la transacción:", e)
finally:
    cursor.close()
    conexion.close()
