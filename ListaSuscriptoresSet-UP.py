print('*** Lista de Suscriptores ***')

#Definimos SET inicial

# suscriptores = {}
suscriptores = set() # Definimos un SET Vacio

numero_suscriptores = int(input("Digite Nro de suscriptores iniciales: "))

for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))

print(f'Lista de suscriptores iniciales: {suscriptores}')

#verifica si un suscriptor esta en la lista
nuevo_suscriptor = input('Digite nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'YA SE ENCUENTRA SUSCRIPTOR {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'nuevo suscriptor se ha agregado a lista {nuevo_suscriptor}')
print(f'Lista de suscriptores: {suscriptores}')

# Eliminamos un suscriptor
suscriptor_eliminar = input('Digite suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista')
print(f'Lista de suscriptores: {suscriptores}')

# Verificamos la cantidad total de suscriptores
print(f'Cantidad total suscriptores: {len(suscriptores)}')

# Mostramos todos los suscriptores
print(f'--- Lista de Suscriptores ---')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')