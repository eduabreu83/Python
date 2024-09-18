#a confederação nacional de natação precisa de um programa q leia o ano de nasc e mostre sua categoria
# até 9 anos MIRIM, ate 14 Infantil, 19 junior, 20 senior e maior de MASTER
from datetime import date
ano = int(input('Digite o ano do nadador'))
at = date.today().year
c = at - ano
if c <= 9:
    print('o Nadador tem {} anos e sua categoria é a MIRIM'.format(c))
elif c > 9 and c <= 14:
    print('O nadador tem {} anos e sua categoria é a INFANTIL'.format(c))
elif c > 14 and c <= 19:
    print('O nadador tem {} anos e sua categoria é a JUNIOR'.format(c))
elif c <= 25:
    print('O nadador tem {} anos e sua categoria é a SENIOR'.format(c))
elif c > 25:
    print('O nadador tem {} anos e sua categoria é a MASTER'.format(c))
