frase = 'Python é muito bom'

i = 0
maior = ''
qtd_maior = 0

while i < len(frase):
    
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd = frase.count(letra_atual)

    if i == 0 or qtd > qtd_maior:
        maior = letra_atual
        qtd_maior = qtd
    
    i += 1

print(maior, qtd_maior)
print('zzzzzz')