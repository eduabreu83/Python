pessoas = {'Nome': 'Eduardo', 'Sexo': 'M', 'Idade': 37}
print(pessoas['Nome'])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]}')
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
print('-='*30)
for k in pessoas.keys():
    print(k)
print('-='*30)
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('-='*10, 'Criando Dic. dentro da Lista', '-=' *10)
Brasil = []
estado = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
Brasil.append(estado)
Brasil.append(estado2)
print(Brasil[0]['uf'])
print(Brasil[1]['Sigla'])
print('-='*30)

print('-='*10, 'Dicas e problemas', '-=' *10)
estados = {}
Brasil2 = []
for c in range(0, 3):
    estados['uf'] = str(input('Unidade federativa: '))
    estados['Sigla'] = str(input('Sigla do estado: '))
    Brasil2.append(estados.copy())
for e in Brasil2:
    print(e)
print('-='*30)
for e in Brasil2:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')
print('-='*30)
for e in Brasil2:
    for v in e.values():
        print(v, end=' ')
    print()






