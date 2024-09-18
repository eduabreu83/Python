#faça um programa q leia um numero qualquer e mostre seu fatorial
# EX: 5! 5X5X3X2X1 = 120
'''from math import factorial
print('>>>' * 20)
n = int(input('Digite um numero inteiro para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

#modo tradicional
n1 = int(input('Digite um numero inteiro para calcular o fatorial: '))
c = n1
f1 = 1
print('Calculando o fatorial de {}! '.format(n1), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f1 *= c
    c -= 1
print('{}'.format(f1))




