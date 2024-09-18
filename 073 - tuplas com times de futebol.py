'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
 do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

list = ('INTERNACIONAL','SAO PAULO','VASCO','FLUMINENSE','ATLETICO-MG','PALMEIRAS',
'FORTALEZA','BAHIA','FLAMENGO','SANTOS','CEARA','GREMIO','ATHLETICO','CORITIBA','BOTAFOGO',
'CORINTHIANS','BRAGANTINO','GOIAS','SPORT','ATLETICO-GO')

print('-' * 30)
print(f'Lista do Brasileirão 2020: , {list}')
print('-' * 30)
print(f'Os 5 primeiros times são: , {list[0:5]}')
print('-' * 30)
print(f'Os últimos 4 colocados: , {list[-4:]}')
print('-' * 30)
print(f'Times em ordem alfabética: {sorted(list)}')
print('-' * 30)
print(f'O Santos está na posição {list.index("SANTOS")}')


