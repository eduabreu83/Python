#crie um prg q leia seis numeros inteiros e mostre a soma apenas daqueles q forem PARES,
# se o valor digitado for IMPAR, desconsidere-o
s = 0
co = 0
for c in range(1, 7):
    n = int(input('Digite o {}° numero'.format(c)))
    if n % 2 == 0:
        s = s + n
        co = co + 1
print('vc informou o numero {} e a soma é {}'.format(co, s))

