'''Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
 B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

ltemp = []
lista = []
mai = men = 0
while True:
    ltemp.append(str(input('Digite o nome: ')))
    ltemp.append(float(input('Digite seu peso: ')))
    if len(lista) == 0:
        mai = men = ltemp[1]
    else:
        if ltemp[1] > mai:
            mai = ltemp[1]
        if ltemp[1] < men:
            men = ltemp[1]
    lista.append(ltemp[:])
    ltemp.clear()
    resp = str(input('Deseja continar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Os dados foram {lista}')
print(f'Vc cadastrou {len(lista)} pessoas')
print(f'O maior peso cadastrado foi {mai} Kg. Peso de ', end='')
for peso in lista:
    if peso[1] == mai:
        print(f'{peso[0]}', end= '')
print()
print(f'O menor peso cadastado foi {men} kg. Peso de ', end='')
for peso in lista:
    if peso[1] == men:
        print(f'{peso[0]}', end= '')
print()


