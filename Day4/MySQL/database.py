import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dikonda9@",
)

c = db.cursor()

c.execute("show databases;")

for i in c:
    print(i)

c.execute("use employee_db")

c.execute("insert ")
    

