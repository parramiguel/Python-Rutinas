conjunto_A = {1, 2, 3}
conjunto_B = {3, 4, 5}

print(conjunto_A)
print(conjunto_B, "\n")

# Utilizando el método union()
union_conjuntos = conjunto_A.union(conjunto_B)

# Utilizando el operador |
union_conjuntos_operador = conjunto_B | conjunto_A

print("Unión de conjuntos utilizando el método union():", union_conjuntos)
print("Unión de conjuntos utilizando el operador |:", union_conjuntos_operador)
