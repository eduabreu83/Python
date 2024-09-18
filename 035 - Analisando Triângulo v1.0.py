#crie um prg q leia o comprimento de 3 retas e diga ao usuario se pode formar um triangulo
a = float(input('Digite um valor para a 1º reta'))
b = float(input('Digite um valor para a 2º reta'))
c = float(input('Digite um valor para a 3º reta'))
if a < b + c and b < a + c and c < a + b:
    print('As retas acima digitadas formam um triangulo')
else:
    print('as retas acima digitadas NÃO formam um triangulo')


