# crie um prg que leia a velocidade de um carro e se ele passar 80km/h mostre q ele foi multado e q a multa vai custar 7 reias
# por cada km acima do limite
vl = float(input('Digite a velocidade aferida'))
l = 80
c = 7
if vl <= l:
    print('Velocidade dentro do Limite permitido')
else:
    t = (vl - l) * c
    print('Vc foi multado e o valor da multa será {:.1f}'.format(t))

#resolução do curso com condição simples
v = float(input('Digite a velocidade aferida'))
if v > 80:
    m = (v - 80) * 7
    print('Multado!! vc vai pagar uma multa de {}'.format(m))
