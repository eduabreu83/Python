'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Deseja continuar [S/N]? '))
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Vc digitou {len(lista)} elementos...')
lista.sort(reverse=True)
print(f'OS valore em ordem descrecente são {lista}')
if 5 in lista:
    print('o numero 5 faz parte da lista')
else:
    print('O numero 5 não faz parte da lista')



