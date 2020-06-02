# single thread
#-------------------
import time
from threading import Thread

# inicializa el contador
COUNT = 5000000

# declara la funcion encargada
# de disminuir en una unidad el contador
def countdown(n):
    while n>0:
        n -= 1

# tiempo de comienzo        
start = time.time()

# llama a la funcion que decrementa el contador hasta 0
countdown(COUNT)

# tiempo de terminación
end = time.time()

# Imprimi el tiempo consumido
print('Tiempo consumido en segundos -', end - start)