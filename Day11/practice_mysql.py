import mysql.connector
from mysql.connector import Error 

def connect_db():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = 'Dikonda9@',
            database = "employee_db"
        )
        print("Connected successfully")
        return connection  
    except Error as err:
        print(f"Something went wrong:{err}")
        
def create_table(connection):
    cursor = connection.cursor()
    try:
        query = "CREATE TABLE employees ( id INT NOT NULL PRIMARY KEY,name VARCHAR(255) NOT NULL,department VARCHAR(255) NOT NULL);"
        cursor.execute(query)
        print("Created table successfully")
        
    except Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()
        
def insert_values(connection):
    cursor = connection.cursor()
    try:
        query = "insert into employees (id,name,department) values (%s,%s,%s);"
        n = int(input("Enter the no. of records u want to Enter:"))
        data = []
        for i in range(n):
            id = input("Enter the Employee id:")
            name = input("Enter the name:")
            department = input("Enter the department:")
            data.append((id,name,department))
        cursor.executemany(query,data)
        connection.commit()
        print("Inserted successfully")
    except Error as err:
        print(f"Something went wrong:{err}")
    finally:
        cursor.close()
        
        


# conn = connect_db()
# create_table(conn)
# insert_values(conn)