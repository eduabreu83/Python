'''Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from ex110 import moeda

p = float(input('Digite o preço do produto R$: '))
moeda.resumo(p, 20, 50)

