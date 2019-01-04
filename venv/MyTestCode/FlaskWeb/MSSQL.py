# https://docs.microsoft.com/en-us/sql/connect/python/pymssql/python-sql-driver-pymssql?view=sql-server-2017

import pymssql  

conn = pymssql.connect(server='localhost', user='PythonTest', password='PTTest01!', database='TSR')  
cursor = conn.cursor()  
cursor.execute('select * from [dbo].[Functions]')  
row = cursor.fetchone()  
while row:  
    print(str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()  