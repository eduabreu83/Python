'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
 na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
lp = ('Lapis', 1.25, 'Borracha', 2, 'Caneta', 3)
print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(lp)):
    if pos % 2 == 0:
        print(f'{lp[pos]:.<30}', end='')
    else:
        print(f'R$ {lp[pos]:>7.2f}')
print('-'* 40)

