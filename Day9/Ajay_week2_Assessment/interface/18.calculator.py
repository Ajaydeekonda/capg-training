from abc import ABC, abstractmethod

class ICalculator(ABC):
    
    @abstractmethod
    def add(self, num1, num2):
        pass
    
    @abstractmethod
    def subtract(self, num1, num2):
        pass
    
    @abstractmethod
    def multiply(self, num1, num2):
        pass
    
    @abstractmethod
    def divide(self, num1, num2):
        pass
    
class Calculator(ICalculator):
    
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        return num1 / num2
    
if __name__ == "__main__":
    
    choice = input("""Enter your choice: 
                   1. Add 
                   2. Subtract 
                   3. Multiply 
                   4. Divide: 
                   5. Exit \n""")
    
    calc = Calculator()
    while choice != '5':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        if choice == '1':
            print(f"Addition: {calc.add(num1, num2)}")
        elif choice == '2':
            print(f"Subtraction: {calc.subtract(num1, num2)}")
        elif choice == '3':
            print(f"Multiplication: {calc.multiply(num1, num2)}")
        elif choice == '4':
            print(f"Division: {calc.divide(num1, num2)}")
        else:
            print("Invalid choice")
            
        choice = input("""Enter your choice: 
                   1. Add 
                   2. Subtract 
                   3. Multiply 
                   4. Divide: 
                   5. Exit \n""")