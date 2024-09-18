''''# condigo \ansi
#\033[estilo;texto;fundom]
\033[0;33;44m]

# codigo para estilo
0 sem estilo
1 - Negrito
4 - sublinhado
7 - negativo, invertido

# codigo para txto
30 - branco
31 - vermelho
32 - verde
33 - amarelo
34 - azul
35 - roxo
36 - azul claro
37 - cinza

# plano de fundo
40 até 47 igual acima'''

#\033[0; 30; 41m
#letrapreta com fundo branco \033[7;30m

print('\033[4;31;43molá mundo\033[m')
print('\033[7;30;44m Eduardo de abreu\033[m')

a = 3
b = 5
print('Os valore são \033[32m{}\033[m e \033[34m{}\033[m'.format(a, b))
nome = 'Eduardo'
print('prazer em te conhecer {}{}{}'.format('\033[4;34m', nome,'\033[m'))

nome2 ='Abreu'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'petrobranco':'\033[7;30m'}
print('prazer em te conhecer {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
