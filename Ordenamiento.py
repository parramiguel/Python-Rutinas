my_list = [8, 10, 6, 2, 4]  # lista a ordenar
my_list2 = [8, 10, 6, 2, 4]
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("Lista original",my_list2)
print("Lista ordenada",my_list)
