# crie um prg que pergunte o seu salario e calcule um aumento, para salarios maior que 1200 + 10% para inferiores 15%
s = float(input('qual é o seu salario? '))
b = 1250
a1 = 10
a2 = 15
if s >= b:
    s1 = s + (s * a1)/100
    print(('seu novo salario é {:.2f}'.format(s1)))
else:
    s2 = s + (s * a2)/100
    print(('seu novo salario é {:.2f}'.format(s2)))

#resolvido pelo curdo
sal = float(input('Qual o valor do seu salario R$: '))
if sal <=1250:
    novo = sal + (sal * 15)/100
else:
    novo = sal + (sal * 10)/100
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora'.format(sal, novo))

