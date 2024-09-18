#Desafio 004 - faça um programa q leia algo pelo teclado e mostre na tela o seu tipo e todas
# as informações possivel sobre ela
n = input('Digite um valor: ')
print('o tipo primitivo desse valor é ', type(n))
print('valor tem espaço ?', n.isspace())
print('valor é numero?',n.isnumeric())
print('valor é texto?',n.isalpha())
print('valor é caixa alta?',n.isupper())
print('valor é alfa numrico?',n.isalnum())
