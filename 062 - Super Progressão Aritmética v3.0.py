#melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos.
#o prog encerra quando ele disser que quer mostrar 0 termos
t1 = int(input('Digite o 1° termo'))
r = int(input('Digite a Razão'))
termo = t1
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} - '.format(termo), end='')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Digite mais termos'))
print('programa finalizado com o total de {} progressões'.format(total))

