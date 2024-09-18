#listas podem ser mutaveis diferentes das tuplas que são representadas por () parenteses
#Listas são mutaveis e são representados por [] colchetes

#comando para adicionar itens na lista
.append('item')
.insert(0,'item')

#comando para apagar um item
del lista[3]
.pop(3) # se utilizar sem indice apagará o ultimo da ordem
.remove('Item')

if 'pizza' in lanche:
    lanche.remove('pizza')

valores = list(range(4,11))

valores = [8,2,5,4,2,9,3,0]
valores.sort()
valores.sort(reverse=True) #para ordenar decrescente
len(valores) # tamanho da lista

num = [2,5,9,1]
num[2] =3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
#num.pop(2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o numero 5')
#num.remove(4)
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print('=' * 30)

valores1 =list()
for cont in range(0,5):
    valores1.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores1):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

print('=' * 30)

a = [2, 3, 4, 7]
b = a[:] #regra de fatiamento que faz um cópia e não cria ligação
b[2] = 8 #troca a segunda posição para o valor 8
print(f'Lista A: {a}')
print(f'lISTA b: {b}


