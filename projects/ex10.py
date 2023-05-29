"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Mário')

indices = range(len(lista))

for i in indices:
    print(i, lista[i])
