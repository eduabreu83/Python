#faça um prg que leia um numero inteiro e diga se ele é ou não um numero primo
n = int(input('Digite um numero: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(n, t))
if t == 2:
    print('O numero é PRIMO')
else:
    print('O numero não é PRIMO')


