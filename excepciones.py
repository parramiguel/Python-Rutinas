try:
    
    numero = int(input("Ingresa un número: "))
    resultado = 50 // numero
    print(f"50 / {numero} =", resultado)
    
except ValueError as ve:
    print(f"Debes ingresar un número: {ve}")
except ZeroDivisionError as zde:
    print(f"No puedes dividir por cero: {zde}")  
except Exception as e:
    print(f"Operación no valida: {e}")

else:
    print("else: - ¡Operación exitosa!")

finally:
    print("finally - ¡Fin del programa.")
    
