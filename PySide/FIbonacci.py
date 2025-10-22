def main():
    print("=== CALCULADORA DE FIBONACCI ===")

    while True:
        print("\nOpciones:")
        print("1. Calcular un término específico")
        print("2. Ver una secuencia")
        print("3. Salir")

        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            try:
                n = int(input("Ingresa el término que quieres calcular: "))
                if n < 0:
                    print("Por favor ingresa un número no negativo")
                else:
                    resultado = fibonacci_iterativo(n)
                    print(f"F({n}) = {resultado}")
            except ValueError:
                print("Por favor ingresa un número válido")

        elif opcion == "2":
            try:
                cantidad = int(input("¿Cuántos términos quieres ver?: "))
                if cantidad <= 0:
                    print("Por favor ingresa un número positivo")
                else:
                    secuencia = secuencia_fibonacci(cantidad)
                    print(f"Secuencia de Fibonacci (primeros {cantidad} términos):")
                    print(secuencia)
            except ValueError:
                print("Por favor ingresa un número válido")

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor selecciona 1, 2 o 3.")


# Funciones auxiliares (las mismas de arriba)
def fibonacci_iterativo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


def secuencia_fibonacci(cantidad):
    secuencia = []
    a, b = 0, 1
    for i in range(cantidad):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia


if __name__ == "__main__":
    main()