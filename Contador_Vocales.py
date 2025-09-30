print(" ***** Contador de vocales ****")

cadena = "Hola Mundo"
vocales = "aeiouAEIOU"
contador = 0

for caracter in cadena:
    if caracter in vocales:
        contador += 1

print(f"La cantidad de vocales en la cadena -->{cadena}<-- es: {contador}")