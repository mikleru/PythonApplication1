import pyodbc

driver = '{ODBC Driver 17 for SQL Server}'
server = '(localdb)\MSSQLLocalDB'
db = 'DebitCard_Data'
user = ''
pw = ''

# con = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+db+';UID='+user+';PWD='+pw)
con = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+db)
cur = con.cursor()
try:
    cur.execute('''
        SELECT * 
        FROM DC_Balance 
        WHERE Account like '54784_'
    ''')

# Показываем результат.
    result = cur.fetchall()
    for item in result:
        if item[2]<=10: print(item[0],' ',item[2])
except pyodbc.DatabaseError as err:
    print('Error: ',err)

# Close connection.
cur.close()
con.close()
