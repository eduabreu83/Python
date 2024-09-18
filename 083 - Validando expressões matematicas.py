'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

exp = str(input('Digite sua expressão: '))
pilha = []
for s in exp:
    if s == '(':
        pilha.append('(')
    elif s == (')'):
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão esta incorreta')
