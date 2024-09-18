#escreva um programa q leia um numero inteiro qq e peça para o usuario escolher qual será a base de conversão
# 1 para binario 2 para octal e 3 para hexadecimal
n = int(input('Digita um numero inteiro'))
print('Digite 1 para opção Binaria')
print('Digite 2 para opção Octal')
print('Digite 3 para opção de hexadecimal')
o = int(input('Digite a opção aqui:'))
if o == 1:
    print('o Valor {} em binario é {} '.format(n, bin(n)[2:]))
elif o == 2:
    print("o valor {} em octal é {}".format(n, oct(n)[2:]))
elif o == 3:
    print("o valor {} em hexadecial é {}".format(n, hex(n)[2:]))
else:
    print("opção invalida insira um numero valido")


