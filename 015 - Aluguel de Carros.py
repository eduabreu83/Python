#Aluguem de Carros
di = int(input('quantos dias de uso do Carro'))
km = float(input('Quantos km foram rodados?'))
cd = 60
ck = 0.15
diaria = di * cd
custokm = km * ck
total = diaria + custokm
print('o custo das suas diarias é o valor de R$ {:.2f} e por KM rodado é {:.2f} no total de {:.2f}'.format(diaria, custokm, total))
