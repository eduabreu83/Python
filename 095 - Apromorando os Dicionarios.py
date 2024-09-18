'''Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador'''
jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do Jogador: '))
    tot = int(input(f'Quantos jogos {jogador["nome"]} jogou?: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantas gols ele fez na partida {c+1} ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar [S/N]?: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!! Resndonda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com cod {busca} !')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR:  {time[busca] ["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} !')
        print('-' *40)
print('<<< VOLTE SEMPRE >>>')