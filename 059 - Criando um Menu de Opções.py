#crie um prg que leia 2 valores e mostre um menu na tela 1 - para somar 2 para multiplicar 3 - Maior
# 4 -  novos numeros e 5 para sair -----  seu prg deverá realizar a operação solicitada a cada caso.
from time import sleep
v1 = int(input('Digite o valor 1: '))
v2 = int(input('Digite o valor 2: '))
op = 0
while op != 5:
    print('Escolha as opões baixo')
    print('''
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos Numeros
    [5] - Sair do Prg
    ''')
    op = int(input('>>>>>>>>Digite uma das opções acima: '))
    if op == 1:
        soma = v1 + v2
        print('A soma entre o valor {} e o valor {} é de {}'.format(v1, v2, soma))
    elif op == 2:
        mult = v1 * v2
        print('A multiplicação do valor {} x {} é de {}'.format(v1, v2, mult))
    elif op == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
            print('Entre o valor {} e {} o maior é {}'.format(v1, v2, maior))
    elif op == 4:
        print('>>>>>>>>>> Digite novos numeros')
        v1 = int(input('Digite o valor 1: '))
        v2 = int(input('Digite o valor 2: '))
    elif op == 5:
        print('Finalizando.....')
    else:
        print('opção invalida tente novamento')
    print('=-=' *10)
    sleep(2)
print('Fim do Programa! Volte sempre!! ')
