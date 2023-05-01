"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


try:
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        print(f'O número {num} é par.')
    else:
        print(f'O número {num} é ímpar.')
except:
    print('O valor informado não é um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print('-=' * 15)

try:
    hora = int(input('Que horas são? '))
    if 0 <= hora <= 11:
        print('Bom dia!')
    elif 12 <= hora <= 17:
        print('Boa tarde!')
    elif 18 <= hora <= 23:
        print('Boa noite!')
except:
    print('Por favor, digite um horário válido.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print('-=' * 15)

primeiro_nome = input('Qual é o seu primeiro nome? ')

tamanho_nome = len(primeiro_nome)

if tamanho_nome <= 4:
    print('Seu nome é curto.')
elif 5 <= tamanho_nome <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande!')
