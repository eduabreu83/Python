''' faça um prg que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER
mostrando o total de vitorias consecutivas que ele conquistou no final do jogo'''
from random import randint
print('-'*20)
print('JOGAR PAR OU ÍMPAR')
print('-'*20)
v = 0
while True:
    jog = int(input('Escolha um numero...: '))
    comp = randint(0, 10)
    total = jog + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR? [P/I]: ')).strip().upper()[0]
    print(f'Vc jogou {jog} e o computador jogou {comp} e o Total {total}', end= ' ')
    print('DEU PAR' if total % 2 ==0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 ==0:
            print('VC VENCEU!!')
            v += 1
        else:
            print('VC PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VC VENCEU!!')
            v += 1
        else:
            print('VC PERDEU')
            break
        print('Vamos jogar novamente....')
print(f'GAME OVER!! VC venceu {v} vezes !!')




