#crie um prog q leia o nome idade e sexo de 4 pessoas e mostre a media de idade, nome do homem mais velho e
# quantas mulhers tem menos de 20 anos
somaidade = 0
media = 0
maioridadehomen = 0
nomevelho = ''
tmulher20 = 0
for pess in range(1,5):
    print('---- {}° PESSOA-----'.format(pess))
    nome = str(input('Digite o nome da pessoa: '.format(pess))).strip()
    idade = int(input('Digite a idade da pessoa: '.format(pess)))
    sexo = str(input('Digite [M/F] {}° : '.format(pess))).strip().upper()
    somaidade = somaidade + idade
    if pess == 1 and sexo in 'Mn':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        tmulher20 += 1
media = somaidade / 4
print('a média de idade é {}'.format(media))
print('o homem mais velho tem {} anos e se chama {}'.format(maioridadehomen, nomevelho))
print('são {} mulheres menores de 20 anos'.format(tmulher20))


