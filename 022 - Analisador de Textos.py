#Crie um progrma q leia o nome de uma pessoa, em amiuscula, minisculas, qtd de letras no 1º nome, qtd de letras sem espaço
# como foi feito
n = str(input('Digite se nome')).strip()
print('Seu nome em maiusculo é {}.'.format(n.upper()))
print('Seu nome em minusculas é {}'.format(n.lower()))
print('Seu nome tem ao todo tem {}'.format(len(n) - n.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(n.find(' ')))
s = n.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(s[0], len(s[0])))

