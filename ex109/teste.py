'''Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from ex109 import moeda

p = float(input('Digite o preço do produto R$: '))
print(f'O dobro de {moeda.moeda(p)} do produto é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} do produto é {moeda.metade(p, True)}')
print(f'O produto de valor {moeda.moeda(p)} com aumento de 10% é {moeda.aumentar(p, 10, True)}')
print(f'O produto de valor {moeda.moeda(p)} com 35% de desconto é {moeda.diminuir(p, 35, True)}')
