using System;

namespace CSharpPractice2
{
    class BankAccount
    {
        private double balance;

        public BankAccount(double initialBalance)
        {
            balance = initialBalance;
        }

        public void Deposit(double amount)
        {
            balance += amount;
        }

        public void Withdraw(double amount)
        {
            if (amount > balance)
            {
                Console.WriteLine("Insufficient Balance");
                return;
            }
            balance -= amount;
        }

        public double GetBalance()
        {
            return balance;
        }
    }
}
