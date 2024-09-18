''' crie um prg q simule o funcionamento de um caixa eletronico. No inicio perguntando ao usuarios qual será o
valor sacado (numero inteiro) e o prg vai informar quantas CEDULAS  de cada valor serão entregues
COSIDERE QUE O CAIXA SÓ TERA CEDULAS DE 50 20 10 E 1 REAL '''
from time import sleep
print('=' * 30)
print('{:^30}'.format('MEU BANCO'))
print('=' * 30)
valor = int(input('Digite o Valor a ser sacado R$: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Temos o total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            print('Estamos contando sua grana... aguarde alguns segundos.....')
            for c in range(3, -1, -1):
                sleep(2)
                print(f'{c}...', end=' ')
            break
print('  Retire seu dinheiro...')
sleep(2)
print('O valor foi entregue... não gaste com besteira...')

