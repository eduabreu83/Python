#crie um prg que faça o computador jogar jokenpo com vc
from random import randint
from time import sleep
i = ('Pedra', 'Papel', 'Tesoura')
c = randint(0,2)
print('{:=^40}'.format('JOGO DO JOKENPÔ'))
print('Escolha as opções abaixo')
print('[0] - Pedra')
print('[1] - Papel')
print('[2] - Tesoura')
j = int(input('Qual é a sua jogada'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔÔÔ !!! ')
sleep(1)
print('* -' * 12)
print('O computador escolheu {}'.format(i[c]))
print('O Jogador escolheu {}'. format(i[j]))
print('* -' * 12)
if c == 0: # Computador jogou Pedra
    if j == 0:
        print('Empatou')
    elif j == 1:
        print('Jogador venceu')
    elif j == 2:
        print('Computador venceu')
    else:
        print('Jogada Invalida')

elif c ==1: # Computador jogou Papel
    if j == 0:
        print('computador venceu')
    elif j == 1:
        print('Empatou')
    elif j == 2:
        print('Jogador venceu')
    else:
        print('Jogada Invalida')

elif c == 2: # Computador jogou Tesoura
    if j == 0:
        print('Jogador venceu')
    elif j == 1:
        print('Computador venceu')
    elif j == 2:
        print('Empatou')
    else:
        print('Jogada Invalida')
