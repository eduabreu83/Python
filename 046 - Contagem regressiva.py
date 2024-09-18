#contagem regressiva de 10 até 0 com intervalo a cada 1 segundo
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Fim')
