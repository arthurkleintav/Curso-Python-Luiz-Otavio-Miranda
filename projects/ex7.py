''' CALCULADORA COM WHILE '''

while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite o operador [+ - * /] ')
 
    if num_1.isdigit() and num_2.isdigit():
        num_1 = float(num_1)
        num_2 = float(num_2)
    else:
        print('Por favor, informe números válidos.')
        continue

    operadores_validos = '+-*/'

    if operador not in operadores_validos:
        print('Por favor, digite um operador válido.')
        continue

    if len(operador) > 1:
        print('Por favor, digite apenas 1 operador.')
        continue

    if operador == '+':
        calc = num_1 + num_2
    elif operador == '-':
        calc = num_1 - num_2
    elif operador == '*':
        calc = num_1 * num_2
    elif operador == '/':
        calc = num_1 / num_2
    
    print(f'O resultado de {num_1} {operador} {num_2} é igual a {calc}')

    sair = input('Deseja sair do programa? [S/N] ').upper()

    if sair == 'S':
        break
