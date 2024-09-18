#FAÇA UM PRG Q LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES 'M' OU 'F'. CASO ESTEJA ERRADO PEÇA A DIGITAÇÃO
#NOVAMENTE ATÉ TER UM VALOR CORRETO

s = str(input('Digite seu sexo [M/F]')).upper()[0].strip()
while s not in 'MmFf':
      s = str(input('Dados invalidos. por favor insira o correto:')).strip().upper()[0]
print('Vc informou {}'.format(s))
