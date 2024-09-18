#faça um prg que calcule a soma entre todos os numeros impares que são multiplos de 3
# e que se encontram no intervalo de 1 a 500
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print('A soma de todos os {} valores é {}'.format(cont, s))


