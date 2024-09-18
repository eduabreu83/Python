#um professor quer sortear um dos seus 4 alunos para apagar o quadro,faça um prg que ajude excolher 1 deles escrevendo o nome.
import random
a1 = str(input(' primeiro aluno'))
a2 = str(input('Segundo aluno'))
a3 = str(input('Terceiro aluno'))
a4 = str(input('quarto aluno'))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('o Aluno sorteado foi {}'.format(escolhido))



