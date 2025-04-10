import mysql.connector  
myDb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Surya@558'
)
print(myDb)
cursor=myDb.cursor()
cursor.execute('select * from revature.student')
for row in cursor:
    print(row)