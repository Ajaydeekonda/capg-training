import pandas as pd
"""
with open('Day12/Temp.csv', 'w', encoding='utf-8') as file:
    file.write('Name,Age,Country\n') 
    
    while True:
        N = input("Enter 1 to continue or -1 to exit: ")
        
        if int(N) == -1: 
            break
        
        name = input("Enter name: ")
        age = input("Enter age: ")
        country = input("Enter Country name: ")
        
        file.write(",".join([name, age, country]) + "\n") 
"""

"""
data = []
n = int(input("Enter the number of records: "))

for i in range(n):
    Name = input("Enter Name: ")
    Age = int(input("Enter Age: "))  # Convert Age to an integer
    Country = input("Enter Country: ")
    
    data.append({'Name': Name, 'Age': Age, 'Country': Country})  # Correct dictionary format

df = pd.DataFrame(data)
df.to_csv('Day12/Temp2.csv', index=False) 
""" 


"""
df = pd.read_csv('Day12/Temp.csv')
print(df)
print(df.sort_values(by='Age',ascending=False))
"""
