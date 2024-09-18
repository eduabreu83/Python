n = str(input('Digite seu nome completo: ')).strip().upper()
d = n.split()
print(len(d))
print('a letra A aparace {} vezes no seu nome'.format(n.count('A')))
print('Seu nome tem {} letras'.format(len(n) - n.count(' ')))


