print('*** Sistema de Envíos ***')

# Definimos las tarifas de envío por kilogramo
TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

# Solicitamos los valores de destino y peso al usuario
destino = input('Ingresa el destino del paquete (nacional/internacional) N/I: ')
peso = float(input('Ingresa el peso del paquete (en kg): '))

# Cálculo del envío del paquete
costo_envio = None
destino = destino.strip().lower()
if destino == 'n':
    costo_envio = peso * TARIFA_NACIONAL
elif destino == 'i':
    costo_envio = peso * TARIFA_INTERNACIONAL
else:
    print('Destino no válido. Ingresa el valor de nacional o internacional (N/I')

# Mostramos el costo de envío sólo si es un valor válido
if costo_envio is not None:
    print(f'El costo de envío {destino} del paquete es: ${costo_envio:.2f}')