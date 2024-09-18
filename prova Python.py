#pergunta 1
#Para calcular a raiz quadrada temos q utilizar a função from math import sqrt

'''''#Pergunta 2
p = 4**2
p2 = 3*5
print('o resultado é {}'.format(p + p2))

#pergunta 3
p3 = 19//2
p4 = 19%2
print('o resultado é {} e {}'.format(p3,p4))

#pergunta4
n = str(input('Digite seu nome completo')).strip()
print(len(n))

#pergunta5

letras = ()
letras = ('j', 'x')
print(letras.index('x'))

pessoas = [['Pedro', 25], ['Maria', 12], ['José', 25]]
print(pessoas[2][1])'''

for x in range(2, 11, 3):
    print(x, end=' ')
    if x == 3:
        break
    else:
        x = x-1
else:
    print("erro")








