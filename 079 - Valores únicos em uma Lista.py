'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

lista = []
while True:
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado na lista...')
    else:
        print('Valor não adicionado na lista...')
    r = str(input('Quer continuar? S/N: '))
    if r in 'Nn':
        break
print('=-'*30)
lista.sort()
print(f'Os numeros inseridos foram {lista}')
