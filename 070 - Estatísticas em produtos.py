''' Crie um prg que leia o nome e o preço de varios produtos. O prog deverá perguntar se o usuarios vai continuar
e no final mostre:
[A] - Qual o total gasto da compra
[B] - quantos produtos custam mais de R$ 1.000
[C] - qual o nome do produto mais barato'''
totcomp = 0
prdmil = 0
menor= 0
cont = 0
barato = ' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto:R$ '))
    cont += 1
    totcomp += preco
    if preco > 1000:
        prdmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra é de R$ {totcomp:.2f}')
print(f'Temos o total de {prdmil} produtos mais de R$ 1.000')
print(f'O produto mais barato custa R$ {menor}')