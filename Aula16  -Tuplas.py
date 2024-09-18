lanche = ('coca', 'pao', 'batata','suco')

for count in range(0, len(lanche)):
    print(f'Eu vou comer{lanche[count]} na posiçao {count}')

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posiçao {pos}')

print('Comi pra caramba')

print(sorted(lanche))

a = (2,5,4)
b = (5,8,1,2)
c = a + b
d = b + a
print(c,d)
print(c.count(5))
print(c.index(2))

