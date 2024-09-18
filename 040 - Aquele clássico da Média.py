#crie um prg q leia 2 notas de um aluno e calcule sua média, mostrando uma mensagem no final acordo com a média atingida
# < q 5 reprovada - entre 5 a .6,9 recuperação e superior a 7 aprovado
n1 = float(input('Digite sua 1° nota: '))
n2 = float(input('Digite sua 2° nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Vc foi repovado se burrão sua média foi {}'.format(m))
elif m > 5 and m <= 6.9:
    print('Vc esta de recuparação, vai perder as ferias trouxa, média foi {}'.format(m))
elif m >= 7:
    print('Aeee Parabens vai passar as ferias no litoral, suma média foi {}'.format(m))

