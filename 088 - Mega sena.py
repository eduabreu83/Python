'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
lista =[]
jogos = []
print('-='* 15)
print('     Jogo mega sena     ')
print('-='* 15)
qtd = int(input('Qual a quantidade de jogos vc quer?'))
qtj = int(input('Qual a quantidade de numeros? '))
tot = 1
while tot <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= qtj:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sortenado {qtd} jogos com {qtj} cada', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('-=' * 5, '< Boa Sorte>', '-= ' * 5)


