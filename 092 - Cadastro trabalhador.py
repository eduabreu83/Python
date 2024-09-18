'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
 em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
  contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nasc.: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Nº CTPS (0 não tem): '))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de Contatratação: '))
    dados['salario'] = float(input('Salario: R$ '))
    dados['Aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')