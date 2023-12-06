import random

print("Piensa en un número entre 1 y 100. Yo trataré de adivinarlo.")

intentos = 0
adivinanza_minima = 1
adivinanza_maxima = 100
adivinanza_actual = 0

while True:
    intentos += 1
    adivinanza_actual = random.randint(adivinanza_minima, adivinanza_maxima)

    print(f"¿Es {adivinanza_actual} tu número?")
    respuesta = input("Ingresa 'mayor', 'menor' o 'correcto': ").lower()

    if respuesta == "correcto":
        print(f"¡Adiviné tu número ({adivinanza_actual}) en {intentos} intentos!")
        break
    elif respuesta == "mayor":
        adivinanza_minima = adivinanza_actual + 1
    elif respuesta == "menor":
        adivinanza_maxima = adivinanza_actual - 1
    else:
        print("Respuesta no válida. Ingresa 'mayor', 'menor' o 'correcto'.")
