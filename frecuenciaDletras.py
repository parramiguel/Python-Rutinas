frase = input("Ingrese una frase: ")
dicc = {}
for posicion in frase:
    dicc[posicion] = frase.count(posicion)
print(dicc)
