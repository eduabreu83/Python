''''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares.No final, mostre os valores pares e ímpares em ordem crescente.'''
listan = [[], []]
valores = 0
for n in range(1, 8):
    valores = int(input(f'Digite o {n}º Numero: '))
    if valores % 2 == 0:
        listan[0].append(valores)
    else:
        listan[1].append(valores)
print(f'Os valores digitados foram {listan}')
listan[0].sort()
listan[1].sort()
print(f'Os Valores pares são {listan [0]}')
print(f'Os valores Impares são {listan[1]}')


