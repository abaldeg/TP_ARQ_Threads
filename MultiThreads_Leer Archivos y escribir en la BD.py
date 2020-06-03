from threading import Thread
import pyodbc
import time

server = r'.\sql_2019_dev'
database = 'MultiThread'
username = 't1'
password = 't1'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password, timeout=1)
cursor = cnxn.cursor()
path="C:\\Users\\abald\\OneDrive\\Documentos\\GitHub\\TP_ARQ_Threads\\archivos\\"

def insertar_BD(path,nombre):
    """
    Lee archivo de texto e inserta cada línea como un registro en la BD SQL
    """

    try:       
        cantlineas=0
        #chars = ''.join([random.choice(string.ascii_letters) for i in range(tamaño*tamaño)]) #1
        tsql = "INSERT INTO " + nombre + "(linea) VALUES (?);"       
        archentrada=open(path+nombre+".txt","rt")
        for linea in archentrada:
            with cursor.execute(tsql,linea):
                print ('Insertado OK!'+nombre)
            cantlineas+=1
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo: ", mensaje)
    except OSError as mensaje:
        print("Error: ", mensaje)
    else:
        print("Copia Finalizada. Lineas procesadas: ", cantlineas)        
    finally:
        try:
            a.close()
        except NameError:
            pass

# Crea thread 1 y lo referencia con t1
t1 = Thread(target=insertar_BD, args=(path, "archivo_t1",))
# Crea thread 2 y lo referencia con t2
t2 = Thread(target=insertar_BD, args=(path, "archivo_t2",))

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