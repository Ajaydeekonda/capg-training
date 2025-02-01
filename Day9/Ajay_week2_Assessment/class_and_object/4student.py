class Student:
    
    def __init__(self,roll_no,name):
        self.roll_no = roll_no
        self.name = name
        
    def display(self):
        print("Roll Number:",self.roll_no)
        print("Name:",self.name)
        
if __name__ == "__main__":
    roll_no = input("Enter the Roll Number: ")
    name = input("Enter the Name: ")
    student = Student(roll_no,name)
    student.display()