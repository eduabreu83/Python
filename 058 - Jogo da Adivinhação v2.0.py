#MELHORE O JOGO 028 ONDE O COMP VAI PENSAR ENTRE 0 A 10. SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR
# MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSARIOS PARA VENCER
from random import randint
c = randint(0, 10)
print('+-' * 20 )
print('Vou pensar em um numero entre 0 e 10, tente adivinhar....')
print('*-' * 20)
acertou  = False
palpites = 0
while not acertou:
    j = int(input('Em qual numero eu pensei?'))
    palpites += 1
    if j == c:
        acertou = True
    else:
        if j < c:
            print('Mais... tente novamente.')
        elif j > c:
             print('Menos... tente novamente.')
print('vc acertou com {} tentativas. Parabens!!!'.format(palpites))
