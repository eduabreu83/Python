#faça um prg que leia 3 numeros e mostre qual é o maior e qual o menor
n1 = int(input('Digite o primeiro numero'))
n2 = int(input('Digite o segundo numero'))
n3 = int(input('Digite o terceiro numero'))
#verificar o menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3
print('o menor foi o {}'.format(menor))
#verificar o maior
maior = n1
if n2>n1 and n2>n3:
    mmaior = n2
if n3>n2 and n3>n1:
    maior = n3
print('o maior numero foi o {}'.format(maior))
