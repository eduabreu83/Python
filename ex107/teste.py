'''Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from ex107 import moeda

p = float(input('Digite o preço do produto R$: '))
print(f'O dobro de {p} do produto é {moeda.dobro(p)}')
print(f'A metade de {p} do produto é {moeda.metade(p)}')
print(f'O produto de valor {p} com aumento de 10% é {moeda.aumentar(p, 10)}')
print(f'O produto de valor {p} com 35% de desconto é {moeda.diminuir(p, 35)}')
