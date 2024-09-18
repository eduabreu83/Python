#dev um prg q leia o primeiro termo e a razão de uma progressão aritimetica. no final mostre 10 primeiros
# termos dessa progressão

# d foi a formula matematica para achar o decimo termo da PA

t = int(input('Digite o 1° termo'))
r = int(input('Digite a Razão'))
d = t + (10 - 1) * r
for c in range(t, d + r, r):
    print('{}'.format(c), end=' - ')
print('ACABOU')


