for c in range(0, 7, 2):
    print(c)
print('Fim')

n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('Fim')

i = int(input('Digite um numero de inicio'))
f = int(input('Digite um numero de Fim '))
p = int(input('Digite um numero para o passo'))
for c in range(i, f+1, p):
    print(c)
print('Fim')

s = 0
for b in range(0, 4):
    n = int(input('Digite um N°'))
    s+=n
print('A soma deles é de {}'.format(s))

