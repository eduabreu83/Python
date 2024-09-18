# elabora um programa q calcule o valor a ser pago por um produto,considerando seu preço normal e condição de pagamento
#a vista dnheiro ou cheque 10% de desconto
# a vista no cartão 5% de desconto
# até 2x no cartão = preço normal
# 3x ou mais no cartão 20% de juros
print('{:=^40}'.format('LOJAS DE ABREU'))
vp = float(input('Qual o valor do produto que deseja comprar'))
print("Veja as opções de pagamento e escolha a desejada")
print('1 - para a vista dinheiro ou cheque - 10%')
print('2 - Avista no cartão - 5%')
print('3 - 2 para 2x no cartão, $ igual')
print('4 - 3 para 3x no cartão + 20%')
cd = int(input('Digite sua opção de pagamento'))
op1 = vp - (vp * 10)/100
op2 = vp - (vp * 5)/100
op4 = vp + (vp * 20)/100
if cd == 1:
    print('Para o pgto a vista o valor sera de R${:.2f} com 10% desconto'.format(op1))
elif cd == 2:
    print('Para o pgto a vista no cartão o valor sera de R${:.2f} com 5% de desconto'.format(op2))
elif cd == 3:
    print('Para o pgto em 3x no cartão o valor sera de R${:.2f}'.format(op4))
elif cd == 4:
    print('Para o pgto em 3x no cartão o valor sera de R${:.2f}'.format(op4))
else:
    print('Opção invalida para pagamento, seleciona a opção correta novamente')

