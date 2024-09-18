'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
listap = []
listai = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Deseja continuar [S/N]? '))
    if resp in 'Nn':
        break
for c in lista:
    if c % 2 == 0:
        listap.append(c)
    else:
        listai.append(c)
print(f' A lista completa q vc digitou é {lista}')
print(f'A lista dos numeros pares é: {listap}')
print(f'A lista dos numeros impares é {listai}')
