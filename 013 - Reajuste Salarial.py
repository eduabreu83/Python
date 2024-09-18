#faça um algoritimo que aumente o salario em 15%
s1 = float(input('Qual o seu salario ?'))
a1 = 10
c1 = s1 + (s1*a1/100)
d2 = s1 - (s1*a1/100)
print(('seu novo salario é {:.2f}'.format(c1)))
print(('seu novo salario com desconte é {:.2f}'.format(d2)))


