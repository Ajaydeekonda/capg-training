using System;

namespace Basics1
{
    public class BankAccount
    {
    }
}

namespace Basics
{
    public class BankAccount
    {
        private string accountId;
        public string AccountHolder { get; set; }
        public decimal Balance { get; private set; }

        public string AccountId
        {
            get => $"DDDDFFWDW{accountId}DDDDDDD";
            set
            {
                if (value.Length == 10)
                    accountId = value;
                else
                    Console.WriteLine("Account ID must be 10 characters long");
            }
        }

        public BankAccount(string accountId, string accountHolder, decimal initialBalance)
        {
            AccountId = accountId;
            AccountHolder = accountHolder;
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

        public decimal GetBalance() => Balance;

        public override string ToString()
        {
            return $"Account Holder: {AccountHolder}, Balance: {Balance:C}";
        }
    }

    class Program
    {
        static void Main()
        {
            BankAccount acc = new BankAccount("1234567890", "John Doe", 1000);
            acc.Deposit(500);
            acc.Withdraw(200);
            Console.WriteLine(acc);
        }
    }
}
