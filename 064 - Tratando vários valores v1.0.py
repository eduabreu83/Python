#crie um prg q leia VARIOS NUMEROS INTEIROS, o Prg só vai parar quando digitar 999, q é a condição de parada
# no final mostre QUANTOS NUMEROS foram digitados e a SOMA entre eles, DESCONSIDERANDO O FLAG
n = 0
c = 0
soma = 0
n = int(input('Digite um numero e [999 para parar]'))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um numero e [999 para parar]'))
print('vc digitou {} e a soma entre eles é {}'.format(c, soma))
