#faça um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada
n0 = int(input('Informe um numero para sua tabuada: '))
t1 = n0*1
t2 = n0*2
t3 = n0*3
t4 = n0*4
t5 = n0*5
t6 = n0*6
t7 = n0*7
t8 = n0*8
t9 = n0*9
t10 = n0*10
print('{} x 1 é = {}'.format(n0, t1))
print('{} x 2 é = {}'.format(n0, t2))
print('{} x 3 é = {}'.format(n0, t3))
print('{} x 4 é = {}'.format(n0, t4))
print('{} x 5 é = {}'.format(n0, t5))
print('{} x 6 é = {}'.format(n0, t6))
print('{} x 7 é = {}'.format(n0, t7))
print('{} x 8 é = {}'.format(n0, t8))
print('{} x 9 é = {}'.format(n0, t9))
print('{} x 10 é = {}'.format(n0, t10))

#outra forma de fazer é no format
n1 = int(input('Qual o numero'))
print('{} x 1 é = {:2}'.format(n1, n1*1))
print('{} x 2 é = {:2}'.format(n1, n1*2))
print('{} x 3 é = {:2}'.format(n1, n1*3))

