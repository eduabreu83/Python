#crie um prgpara ler 7x o anos de 7 pessoas, no fianl mostre quantas pessoas ainda não atingiram a maioridade e quantas ja
from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for pess in range(1, 8):
    ano = int(input('em q ano a {}° pessoa nasceu: '.format(pess)))
    idade = atual - ano
    if idade >= 21:
        tmaior += 1
    else:
        tmenor += 1
print('Ao todo tivemos {} maiores e {} menores'.format(tmaior, tmenor))
