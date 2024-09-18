#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor
n1 = int(input('Digite um numero: '))
a = int(n1-1)
s = int(n1+1)
print('O antecessor do numero é {}, e o sucessor é {}'.format(a, s))

#outra maneira de se fazer é no print -  sem variaveis
n2 = int(input('Digite um numero: '))
print('Analisando o valor de {}, o antecessor do numero é {}, e o sucessor é {}'.format(n2, (n2-1), (n2+1)))
