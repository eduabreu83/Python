#refaça desafio009 mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando o laço FOR
n1 = int(input('Qual o numero'))
for c in range(1, 11):
    print('{} x {} = {}'.format(n1, c, (n1 * c)))
