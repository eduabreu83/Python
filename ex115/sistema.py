from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do sitema'])
    if resposta == 1:
        #'Opção 1' de listar o conteudo do arquivo
        leraquivo(arq)
    elif resposta == 2:
        #opção2 cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sitema... Até logo')
        break
    else:
        print('\033[31mErro Digite uma opção valida!\033[m')
    sleep(2)

