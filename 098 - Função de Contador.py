'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:início,
fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 30)
    print(f'A contagem de {i} até  {f} em {p}')
    sleep(1.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont -= p
    print('FIM')


#prg inc
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem')
print('-=' * 30)
ini = int(input('Digite um numero de Inicio: '))
fim = int(input('Digite um numero de Fim:    '))
pas = int(input('Digite um numero do Passo:  '))
contador(ini, fim, pas)


