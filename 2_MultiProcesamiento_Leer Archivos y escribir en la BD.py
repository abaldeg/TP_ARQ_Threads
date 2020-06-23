import pyodbc
import time
from multiprocessing import Pool

path="C:\\Users\\abald\\OneDrive\\Documentos\\GitHub\\TP_ARQ_Threads\\archivos\\"

def insertar_BD(path,nombre):
    """
    Lee archivo de texto e inserta cada línea como un registro en la BD SQL
    """

    try:
        #Conexión en cada request
        server = r'localhost\sql_2019_dev'
        database = 'MultiThread'
        username = 't1'
        password = 't1'
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password, timeout=1)
        #cnxn.timeout = 1
        cursor = cnxn.cursor()                       
        cantlineas=0                     
        tsql = "INSERT INTO " + nombre + "(linea) VALUES (?);"         
        #tsql = "INSERT INTO Archivo_Identity" + "(linea) VALUES (?);"             
        archentrada=open(path+nombre+".txt","rt")
        for linea in archentrada:
            while True:
                try:
                    with cursor.execute(tsql,linea):
                        print('Insertado OK! / '+nombre)
                        break
                except pyodbc.DatabaseError:
                    print('Error en INSERT en '+nombre)
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

if __name__ == '__main__':
  
    pool = Pool(processes=4)
    start = time.time()
    r1 = pool.apply_async(insertar_BD, [path, "archivo_t1"])
    r2 = pool.apply_async(insertar_BD, [path, "archivo_t2"])
    r3 = pool.apply_async(insertar_BD, [path, "archivo_t3"])
    r4 = pool.apply_async(insertar_BD, [path, "archivo_t4"])     
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)