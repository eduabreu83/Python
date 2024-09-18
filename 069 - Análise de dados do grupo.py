''' crie um prg que leia a idade e o Sexo de varias pessoas. A cada pessoa cadastrada, o prg deverá perguntar
se o usuario quer ou não continuar. no final mostre:
[A] - quantas pessoas tem mais de 18 anos
[B] - quantos homens foram cadastrados
[C] - quantas mulheres tem menos de 20 anos'''
maioridade = 0
homens = 0
tmulher20 = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]')).strip().upper()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        tmulher20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
       break
print(f'Temos {maioridade} pessoas maiores de 18 anos')
print(f'Temos {homens} cadastrados')
print(f'e são {tmulher20} mulheres menores de 20 anos')