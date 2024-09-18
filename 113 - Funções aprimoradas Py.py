'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
 de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[031mUsuario preferiu não digitar o numero.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[031mUsuario preferiu não digitar o numero.\033[m')
            return 0
        else:
            return n



#prg princ
n1= leiaint('Digite um numero Inteiro: ')
n2 = leiafloat('Digite um numero Real: ')
print(f'O valor inteiro é {n1} e o real é {n2}')