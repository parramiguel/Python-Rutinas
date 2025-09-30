from datetime import datetime

def sacar_datetime(dia, mes, año="2022"):
    """
    dia, mes y año son string
    devuelve datetime
    """
    fecha_string = dia + mes + año
    fecha = datetime.strptime(fecha_string, "%d%m%Y")
    return fecha

dia_tonto = "hola Angelita, Feliz Cumpleaños"

if __name__ == "__main__":

    dia_nacimiento = input("Escribe tu día de nacimiento: ")
    mes_nacimiento = input("Escribe tu mes de nacimiento (año, mes, día): ")
    año_nacimiento = input("Escribe tu año de nacimiento (año, mes, día): ")


    print(sacar_datetime("08", "02"))


    hoy = datetime.now()
    nacimiento = sacar_datetime(dia_nacimiento, mes_nacimiento, año_nacimiento)

    cumpleaños = sacar_datetime(dia_nacimiento, mes_nacimiento, str(hoy.year))

    if hoy > cumpleaños:
        cumpleaños = sacar_datetime(dia_nacimiento, mes_nacimiento, str(hoy.year + 1))

    days = cumpleaños - hoy 
    print(days.days)
