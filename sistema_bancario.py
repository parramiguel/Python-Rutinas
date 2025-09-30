print('**** SISTEMA BANCARIO ****')

salir_sistema_txt = input('Desea salir del sistema (S/N): ')
salir_sistema = salir_sistema_txt.strip().lower() == 's'

if not salir_sistema:
    print('CONTINUAMOS DENTRO DEL SISTEMA')
else:
    print('SALIMOS DEL SISTEMA')