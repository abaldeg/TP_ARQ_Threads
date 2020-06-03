/****** Script for SelectTopNRows command from SSMS  ******/

while 1=1
begin
	SELECT [linea]
	FROM [MultiThread].[dbo].[archivo_t1] with(tablock)
  end