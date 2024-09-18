#escreva um prg q faça o computador pensar em numero de 0 a 5 e pça para o usuario descobrir qual o numero
# o prg deverá escrever na tela se o usuario acertou ou não
import random
d = int(input('Digite um numero de 0 a 5: '))
ns = [0, 1, 2, 3, 4, 5]
n = random.choice(ns)
print(n)
if d == n:
   print('acertou miseravi')
else:
    print('Errrooooooouuuu')

# resolução do curso
from random import randint
from time import sleep
c = randint (0, 5)
print('+-' * 20 )
print('Vou pensar em um numero entre 0 e 5, tente adivinhar....')
print('*-' * 20)
j = int(input('Em qual numero eu pensei?'))
sleep(3)
if j ==c:
    print('Acertou miseravi!!!!')
else:
    print('Errou o numero que pensei foi {} e vc disse {}'.format(c, j))
