print("Ingresa año a calcular: ")
año = int(input())

# año = 2023 # el año que queremos comprobar

if not año % 4:
	if not año % 100:     # divisible entre 4 y 100
		if not año % 400:  # divisible entre 4, 100 y 400
			print("Es bisiesto")
		else:              # divisible entre 4 y 100 y no entre 400
			print("No es bisiesto")
	else:                 # divisible  entre 4 y no entre 100
		print("Es bisiesto" , año)
else:                    # no divisible entre 4
	print("No es bisiesto el año" , año)
