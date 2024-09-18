#crie um prg q pergunte a distancia da viagem e calcule o preço cobrando 0,50 por km até 200k e 0.45 para viagens acima
d = float(input('Qual a distancia da sua viagem?'))
c1 = 0.50
c2 = 0.45
dm = 200
if d <= dm:
        t1 = c1 * d
        print('o valor da sua passagem será de R$ {:.2f}'.format(t1))
else:
        t2 = c2 * d
        print('o valor da sua passagem sera de R$ {:.2f}'.format(t2))
