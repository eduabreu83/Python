#faça um prg q leia o comprimento oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
# Maneira matematica de se resolver
c1 = float(input('Qual o valor do cateto oposto?'))
c2 = float(input('Qual o valor do cateto adjacente?'))
h1 = (c1 ** 2 + c2 ** 2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(h1))

# Maneira com modulos
import math
c3 = float(input('Qual o valor do cateto oposto?'))
c4 = float(input('Qual o valor do cateto adjacente?'))
hi = math.hypot(c3, c4)
print('O valor da hipotenusa é {:.2f}'.format(hi))