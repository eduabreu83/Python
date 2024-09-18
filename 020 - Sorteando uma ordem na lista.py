from random import shuffle
a1 = str(input(' primeiro aluno'))
a2 = str(input('Segundo aluno'))
a3 = str(input('Terceiro aluno'))
a4 = str(input('quarto aluno'))
lista = [a1, a2, a3, a4]
ordem = shuffle(lista)
print(lista)
