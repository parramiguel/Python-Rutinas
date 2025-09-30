from random import randint

print("**** GENERADOR DE ID ÚNICO ****")

nombre = input("Dame tu nombre: ")
apellido = input("Dame tu apellido: ")
anio_nacimiento = input("¿CuáL es tu año de nacimiento (YYYY)? ") # Y - Year

# Normalizar los valores
nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
anio_nacimiento_2 = anio_nacimiento.strip()[2:] # También puede ser [2:4]

# Generar el valor aleatorio
aleatorio = randint(1000, 9999)

# Generamos el valor único
id_unico = f"{nombre_2}{apellido_2}{anio_nacimiento_2}{aleatorio}"

print(f'''\nHola {nombre},
    tu nuevo número de identificación (ID) generado por el sistema es:
    {id_unico}
    FELICIDADES!''')