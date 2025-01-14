'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
 a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela
 o processo de cálculo do fatorial.'''

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero:
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostra ou não a conta
    :return: O valor do fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#prg principal
fat = int(input('Digite um numero para saber o fatorial: '))
print(fatorial(fat, show=True))
#help(fatorial())