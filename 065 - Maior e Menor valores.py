#crie um prg q leia VARIOS NUMEROS inteiros. no final mostre a MEDIA ENTRE ELES e qual foi o MAIOR e o MENOR
#O prg deve perguntar ao usuario se ele quer ou não continuar a digitar valores
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('vc digitou {} numeros e a média foi {:.2f}'.format(quant, media))
print('o maior valor foi {} e o menor foi {}'.format(maior, menor))

