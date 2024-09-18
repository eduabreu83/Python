#Escreva um prg para aprovar um emprestimo bancario. o prg vai perguntar o valod da casa, o salario qtd para pagar
#Calcule o valor da prestação mensal sabendo que não pode exceder 30% do valor do salario ou então sera negado

i = float(input('Qual o valor do imóvel de compra?'))
s = float(input('Qual é o seu salario atual'))
q = int(input('Qual a quantidade de meses que gostaria de financiar?'))
pr = i/q
p = (s * 30)/100
if p >= pr:
    print('Seu financiamento esta APROVADO o valor não compromete 30% do seu salario')
    print('O Valor da prestação será de R$ {:.2f}'.format(pr))
    print('30% do seu salario corresponde a R$ {:.2f}'.format(p))
else:
    print('Sua prestação é maior de 30% do seu salario portanto a solicitação esta REPROVADA')


