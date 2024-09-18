#Escreva um prg q leia o ano de um jovem e informe se ele ainda vai se alistar, se é hora dele se alistar ou que ja passou
#da hora de se alistar
# o programa tb deve mostrar quanto tempo falta para ele se alistar.
from datetime import date
a = int(input("Digite seu ano de nascimento"))
c = date.today().year - a
l = 18
r = (l - c) * 1

if c < l:
    print("Sua idade atual é de {} anos, portanto ainda falta {} anos para seu alistamento".format(c, r))

elif c == l:
    print("Este ano vc deve se alistar")
else:
    print("Vc ja passou da hora de se alistar")