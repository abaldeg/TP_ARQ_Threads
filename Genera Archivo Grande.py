import random
import string
import time
from threading import Thread

tamaño=1024

def genera_archivo_aleatorio(nombre,tamaño):
    """generate big random letters/alphabets to a file
    :param filename: the filename
    :param size: the size in bytes
    :return: void
    """
    
    try:
        #chars = ''.join([random.choice(string.ascii_letters) for i in range(tamaño*tamaño)]) #1
        chars = ' '.join( [str(time.time()) + ': ' + random.choice(string.ascii_letters) + '\n' for i in range(tamaño*tamaño)]) #1
        
        with open(nombre, 'wt') as a:
                    a.write(chars)
    finally:
        try:
            a.close()
        except NameError:
            pass       
    
# Crea thread 1 y lo referencia con t1
t1 = Thread(target=genera_archivo_aleatorio, args=("C:\\Users\\abald\\OneDrive\\Documentos\\GitHub\\TP_ARQ_Threads\\archivos\\archivo_t1.txt",tamaño,))
# Crea thread 2 y lo referencia con t2
t2 = Thread(target=genera_archivo_aleatorio, args=("C:\\Users\\abald\\OneDrive\\Documentos\\GitHub\\TP_ARQ_Threads\\archivos\\archivo_t2.txt",tamaño,))

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
#genera_archivo_aleatorio("C:\\Users\\abald\\OneDrive\\Documentos\\GitHub\\TP_ARQ_Threads\\archivos\\archivos.txt",tamaño)
