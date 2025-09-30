print(' * * * SISTEMA DE TIENDA EN LINEA CON DESCUENTO * * * ')

#Condiciones

MONTO_COMPRA_DESCUENTO = 1000

monto_compra = float(input('Digite monto de su compra: '))
es_miembro = input('Miembro S/N: ')

descuento = 0

# verificar datos digitados
if monto_compra >= MONTO_COMPRA_DESCUENTO and es_miembro.strip().lower() == 'si':
    descuento = 0.1 # descuento de 10%
elif es_miembro.strip().lower() == 'si':
    descuento = .05 # descuento de 5%
elif monto_compra >= MONTO_COMPRA_DESCUENTO:
    descuento = .03 # descuento de 3%
else:
    descuento = 0

# Calculos respectivos para montos finales
if descuento !=0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(f'\n felicidades has obtenido un descuento del {descuento * 100:.0f}%')
    print(f'Monto de la compra ${monto_compra:.2f}')
    print(f'Monto de descuento: ${monto_descuento:.2f}')
    print(f'Monto final de la compra con descuento: ${monto_final:.2f}')
else:
    print('NO OBTUVISTE NINGUN DESCUENTO')
    print('****** TE INVITAMOS HACERTE MIEMBR0')
    print(f'Monto final de la compra: {monto_compra:.2f}')
