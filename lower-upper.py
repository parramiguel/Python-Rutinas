string = input("Introduce un String:")

print(f"\n¿Todas las letras están en minúsculas?: {string.islower()}")
string = string.lower()
print(f"String en minúsculas: {string}")

print(f"\n¿Todas las letras están en mayúsculas?: {string.isupper()}")
print(f"String en mayúsculas: {string.upper()}")
print(f"String original: {string}")
