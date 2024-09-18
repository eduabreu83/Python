nome = str(input('Qual é o seu nome'))
if nome == 'Eduardo':
    print('Nome lindo')
elif nome == 'Mayra' or nome == 'Maria' or nome== 'Davi':
    print('Seu nome é polular no Brasil')

elif nome in 'Pedro Ana Jessica Julina':
    print('Seu nome é feminino')

else:
    print('Seu nome é bem normal')

print('Tenha um bom dia, {}!'.format(nome))
