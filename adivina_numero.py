import random

print("Bienvenido a 'Adivina el Número Secreto'")
print("He seleccionado un número entre 1 y 100. ¡Adivina cuál es!")

numero_secreto = random.randint(1, 100)
intentos_maximos = 10
adivinanza = 0

for intento in range(1, intentos_maximos + 1):
    print(f"\nIntento {intento}/{intentos_maximos}")

    try:

        adivinanza = int(input("Ingresa tu adivinanza: "))

        if adivinanza < numero_secreto:
            print("El número es mayor.")
        elif adivinanza > numero_secreto:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! ¡Has adivinado el número secreto ({numero_secreto}) en {intento} intentos!")
            break

    except ValueError:
        print("Debes ingresar un número entero.")
    except Exception as e:
        print(f"Debes ingresar un número entero: {e}")

if adivinanza != numero_secreto:
    print(f"\nLo siento el número secreto era {numero_secreto}. ¡Mejor suerte la próxima vez!")

input ("Presiona Enter para salir.")

