def check_balance(balance):
    print(f"Your current balance is: ${balance}")
    return balance

def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"${amount} has been deposited.")
    else:
        print("Deposit amount must be positive.")
    return balance

def withdraw(balance, amount):
    if amount <= 0:
        print("Withdrawal amount must be positive.")
    elif amount > balance:
        print("Insufficient balance for this withdrawal.")
    else:
        balance -= amount
        print(f"${amount} has been withdrawn.")
    return balance

def atm_menu():
    balance = 0 
    
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Please choose an option (1-4):")

        
        if choice.isdigit():
            choice = int(choice)

            if choice == 1:
                balance = check_balance(balance)
            elif choice == 2:
                deposit_amount = int(input("Enter amount to deposit: $"))
                balance = deposit(balance, deposit_amount)
            elif choice == 3:
                withdraw_amount = int(input("Enter amount to withdraw: $"))
                balance = withdraw(balance, withdraw_amount)
            elif choice == 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice! Please select a valid option (1-4).")
        else:
            print("Invalid input! Please enter a valid number (1-4).")

if __name__ == "__main__":
    atm_menu()
