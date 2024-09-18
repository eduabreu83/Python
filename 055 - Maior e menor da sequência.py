#crie um prg leia o peso de 5 pessas e mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O Maior peso lido foi {}'.format(maior))
print('O menor peso lido foi {}'.format(menor))

