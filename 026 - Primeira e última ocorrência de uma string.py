#crie um prg de q leia uma frase e mostre, qtds de 'A', em q posição ela apaece primeiro e em q posição aparce por ultimo
f = str(input('Digite um frase')).upper().strip()
print('sua frase possui a letra A {} vezes '.format(f.count('A')))
print('E aparece em primeiro na posição {}'.format(f.find('A')+1))
print('e por ultimo na posção {}'.format(f.rfind('A')+1))

