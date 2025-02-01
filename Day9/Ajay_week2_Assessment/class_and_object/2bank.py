class Bank:
    
    def __init__(self, account_no, account_holder_name, balance):
        self.account_no = account_no
        self.account_holder_name = account_holder_name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def display(self):
        print("Account Number:",self.account_no)
        print("Account Holder Name:",self.account_holder_name)
        print("Balance:",self.balance)
        
        
if __name__ == "__main__":
    account_no = input("Enter the Account Number: ")
    account_holder_name = input("Enter the Account Holder Name: ")
    balance = input("Enter the Balance: ")
    bank = Bank(account_no, account_holder_name, int(balance))
    
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            amount = int(input("Enter the amount to deposit: "))
            print("Balance after deposit:",bank.deposit(amount))
        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            print("Balance after withdrawal:",bank.withdraw(amount))
        elif choice == 3:
            bank.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice")