#crie um prg que leia o nome completo de uma pessoa e mostre o 1º e o ultimo nome separdamante.
n = str(input('Digite seu nome completo')).strip()
n = n.split()
print(n[0])
print(n[1])
print(n[2])
print(len(n))
print('seu primeiro nome é {}'.format(n[0]))
print(('Seu ultimo nome é {}'.format(n[len(n)-1])))

