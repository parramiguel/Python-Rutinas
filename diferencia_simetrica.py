conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

print(conjunto_A)
print(conjunto_B, "\n")

diferencia_simetrica = conjunto_A.symmetric_difference(conjunto_B)
print("Diferencia Simétrica conjunto_A.symmetric_difference(conjunto_B):", diferencia_simetrica)

diferencia_simetrica_operador = conjunto_B ^ conjunto_A
print("Diferencia Simétrica conjunto_B ^ conjunto_A:", diferencia_simetrica_operador)
