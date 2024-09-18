#faça um prg q leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
a1 = float(input('Informe o valor do Angulo'))
s = math.sin(math.radians(a1))
cs = math.cos(math.radians(a1))
tg = math.tan(math.radians(a1))
print('O valor de seno é {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(s,  cs,  tg, ))

