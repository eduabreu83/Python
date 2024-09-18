'''Crie um programa que leia varios numeros inteitors pelo teclado. O programa só vai parar quando o usuario
digitar o valor 999, no final mostre quantos numeros foram digitados e a soma entre eles desconsiderando o FLAG'''
c = 0
soma = 0
while True:
    n = int(input('Digite um numero e [999 para parar]'))
    if n == 999:
        break
    soma += n
    c += 1
print(f'vc digitou {c} e a soma entre eles é {soma}')
