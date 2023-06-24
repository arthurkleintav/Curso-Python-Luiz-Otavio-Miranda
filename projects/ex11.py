"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []

while True:
    print('Selecione uma opção.')
    user_input = input('[i]nserir [a]pagar [l]istar: ')

    if user_input.lower().strip()[0] == 'i':
        os.system('cls')
        valor = input('Valor: ').title()
        lista.append(valor)

    elif user_input.lower().strip()[0] == 'a':
        os.system('cls')

        if len(lista) == 0:
            print('A lista está vazia.')
            continue
        
        indice = input('Índice: ')
        int_indice = int(indice)

        if not indice.isnumeric() or int_indice >= len(lista) or int_indice < 0:
            print('Por favor, digite um índice válido.')
            continue
        lista.pop(int_indice)
    
    elif user_input.lower().strip()[0] == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('A lista está vazia.')
            continue
        else:
            for i, p in enumerate(lista):
                print(i, p)
    

        
            
