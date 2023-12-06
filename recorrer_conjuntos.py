nums = {1, 2, 3, 4, 5}

# Recorrer conjunto utilizando for
print("Recorriendo conjunto con el ciclo for")
for elemento in nums:
    print(elemento)


# Recorrer conjunto con el ciclo while
print("\n\nRecorriendo conjunto con el ciclo while")
conjunto_lista = list(nums)

indice = 0
while indice < len(conjunto_lista):
    elemento = conjunto_lista[indice]
    print(elemento)
    indice += 1
