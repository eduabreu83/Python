'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
 com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita varias devido ao *n)
    :param sit: valor condicional, indicando se deve ou não adicionar a situação
    :return: dicionario com varios informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação']  = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'RUIM'
    return r


# prg Principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
#help(notas)
