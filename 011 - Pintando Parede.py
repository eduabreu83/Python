#Faça um programa que leia a largura e a altura em metros, calcule a sua area e a quantidade de tinta necessaria
#para pinta-la. sabendo que cada litro de tinta peinta uma area de 2m².
a1 = float(input('Qual a altura da parade?'))
l1 = float(input('Qual a largura da sua parede?'))
r0 = a1*l1
m2 = r0/2
print('a parede tem a dimensão de {}m² x {}m² com o total de {}m²'.format(a1, l1, r0))
print('para pintar essa parede vc precisa de {} litros de tinta'.format(m2))

