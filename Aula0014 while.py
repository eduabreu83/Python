for c in range(1, 10)
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c = c +1
print('Fim')

#os 2 jeitos acima da no mesmo resultado, mas o while é usado quando não sabemos o limete mas temo uma decisão.
n = 1
while n != 0: # sinal de diferente
    n = int(input('Digite um valor'))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor'))
    r = str(input('Quer continuar [S/N]?: ')).upper()
print('Fim')

n = 1
par = imp = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            imp += 1
print('Vc digtou {} n° pares e {} n° impares'.format(par, imp))

