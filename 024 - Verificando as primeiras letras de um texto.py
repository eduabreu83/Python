#crie um prg q leia o nome da uma cidade e diga se ela começa ou não com o nome santo
cid = str(input('Qual o nome da cidade? ')).strip()
print(cid[:5].upper() == 'SANTO')



