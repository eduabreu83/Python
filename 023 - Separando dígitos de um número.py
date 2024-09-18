#faça um programa que leia qq numero e que mostre ele separados
n = int(input('digite um numero '))
s = str(n)
print('A unidade é {}'.format(s[3]))
print('A dezena é {}'.format(s[2]))
print('A centena é {}'.format(s[1]))
print('A milhar é {}'.format(s[0]))

# jeito matematico para solucionar para menos digitos.
n1 = int(input('Digite um numero '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('A unidade é {}.'.format(u))
print('A dezena é {}'.format(d))
print('A centena é {}'.format(c))
print('A milhar é {}'.format(m))


