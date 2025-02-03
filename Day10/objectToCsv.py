import csv

with open('./Day10/example.csv','a')as file:
    # if line is file.read()
    file.write("id"+","+"name"+","+"age"+","+"department"+","+"salary"+"\n")
class Employee:
    
    def __init__(self,id,name,age,department,salary):
        self.id = id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
        
        # with open('./Day10/example.csv','a')as file:
        #     file.write(f"{self.id}"+",")
        #     file.write(f"{self.name}"+",")
        #     file.write(f"{self.age}"+",")
        #     file.write(f"{self.department}"+",")
        #     file.write(f"{self.salary}"+"\n")
        
        with open("./Day10/example.csv",'a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.id,self.name,self.age,self.department,self.salary])
            
        
        
if __name__ == "__main__":
    
    emp = Employee(101,"Ajay",23,"EEE",25000)
               