# multi thread
#-----------------
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

# Crea thread 1 y lo referencia con t1
t1 = Thread(target=countdown, args=(COUNT//2,))
# Crea thread 2 y lo referencia con t2
t2 = Thread(target=countdown, args=(COUNT//2,))

# Marca de tiempo
start = time.time()
t1.start()  # inicia thread1
t2.start()  # inicia thread2
t1.join()   # espera a que thread1 retorne/termine
t2.join()   # espera thread2
# Marca de tiempo final
end = time.time()

# tiempo consumido
print('Tiempo consumido en segundos -', end - start)