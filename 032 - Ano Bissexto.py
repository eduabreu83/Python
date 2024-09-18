#Faça um programa q diga se o ano é bissesto
from datetime import date
ano = int(input('Digite o ano para saber se é Bissesto: '))
if  ano == 0:
    ano  = date.today().year
if    ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissesto')
else:
    print('O ano NÃO é bissesto')


