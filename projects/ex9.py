"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

from os import system
from random import choice

lista_palavras = [
    'perfume', 'fogo', 'gato', 'cachorro'
    ]

palavra = choice(lista_palavras)
letras_acertadas = ''
tentativas = 0

print('Pensando na palavra...')

while True:

    tentativa = input('\nSua tentativa: ')

    if len(tentativa) != 1:
        print('\nPor favor, digite apenas uma letra.')
        continue
    
    if tentativa in palavra:
        letras_acertadas += tentativa

    palavra_formada = ''

    for l in palavra:
        if l in letras_acertadas:
            palavra_formada += l
        else:
            palavra_formada += '*'

    print(palavra_formada)

    tentativas += 1

    if palavra_formada == palavra:
        system('cls')
        
        print(f'PARABÉNS! Você acertou.\n'
              f'A palavra era {palavra}\n'
              f'Número de tentativas: {tentativas}'
              )
        
        palavra = choice(lista_palavras)
        letras_acertadas = ''
        tentativas = 0
