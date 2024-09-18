#crie um prg que leia um numero N inteiro qualquer e mostre na tela os N primeiros elementos de uma seq fibonacci
#ex: 0 1 1 2 3 5 8
n = int(input('Quanto termos de Fibonacci vc quer: '))
t1 = 0
t2 = 1
cont = 3
print('{} -- {} '.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print('-- {} '.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print('FIM')
# o t1 e t2 acima é para andar o calculo na sequencia.