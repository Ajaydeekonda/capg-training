using System;

namespace Basics
{
    public class Account
    {
        public string AccountId { private get; set; }
        public string AccountName { get; set; }
        public decimal Balance { get; private set; }

        public Account(string accountId, string accountName, decimal initialBalance)
        {
            AccountId = accountId;
            AccountName = accountName;
            Balance = initialBalance;
        }

        public void Deposit(decimal amount)
        {
            if (amount > 0)
                Balance += amount;
        }

        public bool Withdraw(decimal amount)
        {
            if (amount > 0 && amount <= Balance)
            {
                Balance -= amount;
                return true;
            }
            return false;
        }

        public decimal GetBalance()
        {
            return Balance;
        }

        public override string ToString()
        {
            return $"Account Name: {AccountName}, Balance: {Balance:C}";
        }
    }

    class Program
    {
        static void Main()
        {
            Account acc = new Account("A123", "John's Account", 500);
            acc.Deposit(200);
            acc.Withdraw(100);
            Console.WriteLine(acc);
        }
    }
}
