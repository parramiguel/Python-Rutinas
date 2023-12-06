try:

    num = int(input("Ingresa un número entero para convertirlo a romano: "))
    if 0 < num < 4000:

        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        D = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        U = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        print(f"{M[num // 1000]}{C[(num % 1000) // 100]}{D[(num % 100) // 10]}{U[num % 10]}")

    else:
        print("El número ingresado debe estar en un rango entre 1 y 3999")

except ValueError:
    print("Debes ingresar un valor entero.")
except Exception as e:
    print("Valor no válido: ", e)
