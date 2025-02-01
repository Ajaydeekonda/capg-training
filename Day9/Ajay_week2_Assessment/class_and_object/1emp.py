class Employee:
    
    def __init__(self,id,name,department):
        self.id  = id
        self.name = name
        self.department = department
        
    def display(self):
        print("Employee ID:",self.id)
        print("Employee Name:",self.name)
        print("Employee Department:",self.department)
    
    
if __name__ == "__main__":
    id,name,department = input("Enter the Employee ID, Name and Department separated by spaces: ").split()
    emp = Employee(id,name,department)
    emp.display()
    