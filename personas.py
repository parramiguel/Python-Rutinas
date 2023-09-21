personas = (("Eduardo", 26), ("María", 30), ("Gerardo", 20), ("Valentina", 22))
print(personas, "\n")

personas = list(personas)
longitud_lista = len(personas)

for i in range(longitud_lista):
    for j in range(i + 1, longitud_lista):

        if personas[i][1] > personas[j][1]:
            aux = personas[i]
            personas[i], personas[j] = personas[j], aux

print(f"La persona de menor edad es: {personas[0]}")
print(f"La persona de mayor edad es: {personas[-1]}")
