class Employee:
    
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def display_employee_info(self):
        self.details = {
            "Name": self.name,
            "Age": self.age,
            "Salary": self.salary
        }
        return self.details


if __name__ == "__main__":
    employees= {}
    i=1
    while True:
        choice = input("Do you want to add an employee? (Y/N): ")
        if choice == "N":
            break
        Name = input("Enter the name of the employee: ")
        Age = int(input("Enter the age of the employee: "))
        Salary = int(input("Enter the salary of the employee: "))
        employees[f"emp{i}"] = Employee(Name,Age,Salary)
        i+=1
    
    for emp in employees:
        print(employees[emp].display_employee_info())
    
    
    
    