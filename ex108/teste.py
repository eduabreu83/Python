'''Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from ex108 import moeda

p = float(input('Digite o preço do produto R$: '))
print(f'O dobro de {moeda.moeda(p)} do produto é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} do produto é {moeda.moeda(moeda.metade(p))}')
print(f'O produto de valor {moeda.moeda(p)} com aumento de 10% é {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'O produto de valor {moeda.moeda(p)} com 35% de desconto é {moeda.moeda(moeda.diminuir(p, 35))}')
