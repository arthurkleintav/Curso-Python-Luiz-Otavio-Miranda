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

palavra = 'perfume'
letras_acertadas = ''

print('Pensando na palavra...')

while True:

    if len(letras_acertadas) == len(palavra):
        break

    tentativa = input('\nSua tentativa: ')

    if len(tentativa) != 1:
        print('\nPor favor, digite apenas uma letra.')
        continue

    if tentativa in palavra:
        letras_acertadas += tentativa * palavra.count(tentativa)
    
    for l in palavra:
        if l in letras_acertadas:
            print(l, end='')
        else:
            print('*', end='')
