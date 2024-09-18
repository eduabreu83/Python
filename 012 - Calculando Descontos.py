#faça um programa que leia o preço de um produto e morte seu novo preço com 5% de desconto
p1 = float(input('qual o valor do produto? R$ '))
d = 5
c = p1 - (p1*d/100)
print('Seu produto custará {:.2f}'.format(c))

