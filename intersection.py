conjunto_A = {1, 2, 3,4,5}
conjunto_B = {4,5,6, 7, 8}

print(conjunto_A)
print(conjunto_B, "\n")

# Utilizando el método intersection()
interseccion_conjuntos = conjunto_A.intersection(conjunto_B)

# Utilizando el operador &
interseccion_conjuntos_operador = conjunto_B & conjunto_A

print("Intersección de conjuntos utilizando el método intersection():", interseccion_conjuntos)
print("Intersección de conjuntos utilizando el operador &:", interseccion_conjuntos_operador)
