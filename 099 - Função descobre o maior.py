'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os numeros..... ')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')

#prg principal
maior(2, 8, 10, 95, 100)
maior(5, 56, 85, 1)
maior(52, 5, 7)
maior(2, 0)
maior(1)
maior()
