class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado suma: {resultado:.2f}')

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado resta: {resultado:.2f}')

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado multiplicación: {resultado:.2f}')

    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f'Resultado división: {resultado:.2f}')


# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo Clase Artimética ***')
    aritmetica1 = Aritmetica(5.23, 7.35)
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.dividir()
    aritmetica1.multiplicar()
    # Segundo objeto
    aritmetica2 = Aritmetica(12.26, 16.49)
    print()
    aritmetica2.sumar()
    aritmetica2.restar()
    aritmetica2.dividir()
    aritmetica2.multiplicar()