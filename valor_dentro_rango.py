print ( '**** valor dentro del rango ****')

MINIMO = 0
MAXIMO = 5

#Solicitamos el valor entre 0 y 5
dato = int(input(f'Proporciona un dato entre {MINIMO} y {MAXIMO}: '))

# verificamos si el valor se encuentra dentro del rango
#esta_dentro_rango = dato >= MINIMO and dato <= MAXIMO
esta_dentro_rango = MINIMO <= dato <= MAXIMO
print(f'Valor esta dentro del rango? {esta_dentro_rango}')