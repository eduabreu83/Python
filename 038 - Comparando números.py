#Escreva um prg q leia 2 numeros inteiros e compare mostrando na tela uma msg
# o valor 1 é maior o 2 é maior e não existe quando os 2 forem iguais
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero'))
if n1 > n2:
    print("O primeiro numero digitado é maior que o segundo")
elif n2 > n1:
    print("o Segundo numero é maior que o primeiro")
else:
    print('os 2 numeros são iguais')

