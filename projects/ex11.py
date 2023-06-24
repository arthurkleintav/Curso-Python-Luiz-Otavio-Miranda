"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os
os.system('cls')

lista = []

while True:
    
    print('Selecione uma opção.')
    user_input = input('[i]nserir [a]pagar [l]istar: ')

    if user_input.lower().strip()[0] == 'i':
        os.system('cls')
        valor = input('Valor: ').title()
        lista.append(valor)
        print(f'\033[36mÍtem "{valor}" adicionado na lista com sucesso!\033[m')

    elif user_input.lower().strip()[0] == 'a':
        os.system('cls')

        if len(lista) == 0:
            print('\033[31mA lista está vazia.\033[m')
            continue

        indice = input('Índice: ')

        try:
            int_indice = int(indice)
        except:
            print('\033[31mPor favor, digite um índice válido.\033[m')
            continue

        if not indice.isnumeric() or int_indice >= len(lista) or int_indice < 0:
            print('\033[31mPor favor, digite um índice válido.\033[m')
            continue

        print(f'\033[36mÍtem "{lista[int_indice]}" apagado da lista com sucesso!\033[m')
        lista.pop(int_indice)

    elif user_input.lower().strip()[0] == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('\033[31mA lista está vazia.\033[m')
            continue

        else:
            for i, p in enumerate(lista):
                print('\033[32m', i, p, '\033[m')

    else:
        print('\033[31mPor favor, selecione uma opção válida.\033[m')
