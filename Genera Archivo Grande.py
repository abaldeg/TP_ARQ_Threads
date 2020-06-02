import random
import string

def genera_archivo_aleatorio(nombre,tamaño):
    """generate big random letters/alphabets to a file
    :param filename: the filename
    :param size: the size in bytes
    :return: void
    """
    
    try:
        chars = ''.join([random.choice(string.ascii_letters) for i in range(tamaño)]) #1
        with open(nombre, 'w') as a:
                    a.write(chars)
    finally:
        a.close()
    

genera_archivo_aleatorio("C:\\Users\\abald\\OneDrive\\Documentos\\GitHub\\TP_ARQ_Threads\\archivos.txt",10)