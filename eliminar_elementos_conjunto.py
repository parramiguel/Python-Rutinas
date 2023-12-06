# Utilizando el método remove()
print("---Utilizando el método remove():")
vocales = {"a", "e", "i", "o", "u"}

vocales.remove('i')

print("vocales.remove('i'):", vocales, "\n")

# Utilizando el método discard()
print("---Utilizando el método discard():")
vocales = {"a", "e", "i", "o", "u"}

vocales.discard('z')

print("vocales.discard('z'):", vocales, "\n")

# Evitar error utilizando el método remove()
print("---Evitar error utilizando el método remove():")
vocales = {"a", "e", "i", "o", "u"}

elemento = "z"
if elemento in vocales:
    vocales.remove(elemento)
    print("vocales.remove(elemento):", vocales, "\n")
else:
    print(f"{elemento} no está en el conjunto vocales.")


















































