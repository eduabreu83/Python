'''faça um programa que mostre a tabuada de varios numeros , um de cada vez, para cada valor digitado pelo usuario.
O progrma será interronpido quando o numero for negativo'''
while True:
    n = int(input('Digite um N° para saber a tabuada'))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('Tabuada encerrada!!')
