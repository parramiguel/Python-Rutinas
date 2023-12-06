print("Bienvenido a la Tienda Virtual")

catalogo = {
    "Camiseta": 20,
    "Jeans": 40,
    "Zapatos": 60,
    "Sombrero": 10
}

carrito = []

while True:
    print("\nMenú:")
    print("1. Agregar productos al carrito")
    print("2. Ver carrito")
    print("3. Realizar el pago y salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\nProductos disponibles:")
        [print(f"• {producto} ${precio}") for producto, precio in catalogo.items()]
        producto = input("Ingrese el nombre del producto que desea agregar: ").title()

        if producto in catalogo:
            carrito.append(producto)
            print(f"Producto '{producto}' agregado al carrito.")

    elif opcion == "2":
        print("\nCarrito:")
        for producto in  set(carrito):
            cantidad = carrito.count(producto)
            precio_unitario = catalogo[producto]
            print(f"{cantidad} {producto} - ${precio_unitario} c/u")

    elif opcion == "3":
        total_a_pagar = sum(catalogo[producto] for producto in carrito)
        print(f"Total a pagar: ${total_a_pagar}")

        try:

            monto_pagado = float(input("Ingrese el monto con el que pagará: "))
            cambio = monto_pagado - total_a_pagar

            if cambio >= 0:
                mensaje_cambio = f"Su cambio es: ${round(cambio, 2)}" if cambio > 0 else "¡Exacto! No se requiere cambio."
                print(f"Gracias por su compra. {mensaje_cambio}")
                break
            else:
                print("El monto ingresado es insuficiente. Por favor, ingrese un monto válido.")

        except Exception as e:
            print("Monto inválido. Por favor, ingrese un monto válido.")

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

















































        
