teste = []
teste.append('Eduardo')
teste.append(37)
galera = []
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

'''ou'''

galera = [['Eduardo', 37], ['Ana', 21], ['Davi',1], ['Livia', 4] ]
print(galera[3][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

galera = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maior de idade e temos {totmen} menores de idade')





