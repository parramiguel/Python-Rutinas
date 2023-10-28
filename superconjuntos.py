A = {1, 2, 3, 4, 5}
B = {1, 2, 3, 4, 5}

print(f"Conjunto A: {A}\nConjunto B: {B}\n")
print("¿A es superconjunto de B? \n")

es_superconjunto = A.issuperset(B)
print("Utilizando el método issuperset():", es_superconjunto)

es_superconjunto = A >= B
print("Utilizando el operador >=:", es_superconjunto)

es_superconjunto = A > B
print("Utilizando el operador >:", es_superconjunto)
