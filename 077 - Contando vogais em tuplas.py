'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('Eduardo', 'Mayra', 'Davi', 'Livia')
for vogal in palavras:
    print(f'\nNa Palavra {vogal.upper()} temos: ', end='')
    for letra in vogal:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
