#refaça o execicio 35 acrescentando o recurso de mostrar q tipo de triangulo será formado
#equilatero todos os lados iguais - isosceles doi lados iguais e Escaleno todos os lados diferentes
a = float(input('Digite um valor para a 1º reta'))
b = float(input('Digite um valor para a 2º reta'))
c = float(input('Digite um valor para a 3º reta'))
if a < b + c and b < a + c and c < a + b:
    print('As retas acima digitadas formam um triangulo')
    if a == b == c:
        print('Equilatero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isosceles ')
else:
    print('as retas acima digitadas NÃO formam um triangulo')