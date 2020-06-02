import pyodbc
server = r'.\sql_2019_dev'
database = 'MultiThread'
username = 't1'
password = 't1'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print ('Inserting a new row into table')
#Insert Query
tsql = "INSERT INTO Empleados (Nombre, Lugar) VALUES (?,?);"
with cursor.execute(tsql,'Juan Martín Del Potro','Argentina'):
    print ('Insertado OK!')