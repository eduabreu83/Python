'''Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(larg,  comp):
    a = larg * comp
    print(f'A area de terreno {larg} x {comp} é de {a} m²')


#prg inc
print('Controle de Terrenos')
print('-='* 30)
l = float(input('Digite a Largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
area(l, c)