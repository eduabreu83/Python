#crie um progrma que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira

import math
n1 = float(input('Digite um numero real '))
print('o numero inteiro {}para o numero real digitado é {}'.format(n1, math.trunc(n1)))

#ou
from math import trunc
n2 = float(input('Digite um numero real '))
print('O numero inteiro digitado é {} e seu numero real é {}'.format(n2, trunc(n2)))

#ou
n3 = float(input('Digite um numero real'))
print('O numero inteiro digitado é {} e seu numero real é {}'.format(n3, int(n3)))






