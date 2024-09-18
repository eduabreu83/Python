'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

n1 = (int(input('Digite o 1º numero: ')),int(input('Digite o 2º numero: ')),
      int(input('Digite o 3º numero: ')),int(input('Digite o 4º numero: ')))
print(f'Vc digitou os numeros: {n1}')
print(f'O numero 9 foi digitado {n1.count(9)} vezes')
if 3 in n1:
    print(f'O Numero 3 apareceu na posição {n1.index(3)}')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram ', end='')
for n in n1:
    if n % 2 == 0:
        print(n, end=' ')




