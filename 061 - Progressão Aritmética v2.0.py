#refaça o desafio 51, lendo o primeiro termo e ao razão de uma PA, mostranso os 10 primeiros termos da PA usando a
#estrutura while
t1 = int(input('Digite o 1° termo'))
r = int(input('Digite a Razão'))
termo = t1
c = 1
while c <= 10:
    print('{} - '.format(termo), end='')
    termo += r
    c += 1
print('ACABOU')

