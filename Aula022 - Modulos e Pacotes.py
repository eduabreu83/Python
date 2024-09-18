from uteis import numeros

#prg prncipal
num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O dobro do {num} é {numeros.dobro(num)}')
print(f'O triplo do {num} é {numeros.triplo(num)}')
