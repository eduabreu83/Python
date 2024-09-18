def lin():
    print('-=' * 20)


#prg inicial
lin()
print('Eduardo de Abreu')
lin()
print('Livia de Abreu')
lin()

def mensagem(msg):
    print('-=' * 20)
    print(msg)
    print('-=' * 20)


#prg inicial
mensagem('Eduardo')
mensagem('Livia')
mensagem('Davi')

def soma(a, b):
    print(f'A= {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é = {s}')


#prg inicial
soma(8, 9)
soma(b=2, a=6)

lin()

#empacotar parametros
def contador1(* num):
     for valor in num:
        print(f'{valor} ', end=' ')


contador1(1, 3, 5, 6)
contador1(2, 3, 8, 7)


def contador2(* num2):
        lin()
        tam = len(num2)
        print(f'Recebi os valores {num2} e são ao todo {tam} numeros!!!')


contador2(2, 4, 8, 5)
contador2(1, 7, 10, 9)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

#desempacotamento
def soma2(* val):
    s = 0
    for num in val:
        s += num
    print(f'A soma dos valores {val} temo {s}')


soma2(1, 6, 8, 9)
soma2(8, 5, 4)


