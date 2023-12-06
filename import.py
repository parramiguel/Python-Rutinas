# Importar un módulo completo
print("Importar un módulo completo")

import math
print(math.sqrt(25))
print(math.sin(30))

# Importar un módulo con un alias
print("\nImportar un módulo con un alias")

import math as m
print(m.sqrt(25))
print(m.tan(30))

# Importar solo lo necesario de un módulo
print("\nImportar solo lo necesario de un módulo")

from math import sqrt, sin
print(sqrt(25))
print(sin(30))

# Importar todo de un módulo (evitar en general)
print("Importar todo de un módulo (evitar en general)")

from math import *
print(tan(30))
print(sin(30))
print(sqrt(25))




