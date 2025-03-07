using System;

abstract class Transaction
{
    public string TransactionId { get; set; }
    public double Amount { get; set; }
    public string TransactionType { get; set; }

    public Transaction(string transactionId, double amount, string transactionType)
    {
        TransactionId = transactionId;
        Amount = amount;
        TransactionType = transactionType;
    }

    public abstract void Execute();
}

class ATM
{
    private double balance;

    public ATM(double initialBalance)
    {
        balance = initialBalance;
    }

    public void Deposit(double amount)
    {
        balance += amount;
        Console.WriteLine($"Deposited: {amount}. New Balance: {balance}");
    }

    public void Withdraw(double amount)
    {
        if (amount > balance)
        {
            Console.WriteLine("Insufficient funds.");
            return;
        }
        balance -= amount;
        Console.WriteLine($"Withdrawn: {amount}. New Balance: {balance}");
    }

    public void CheckBalance()
    {
        Console.WriteLine($"Current Balance: {balance}");
    }
}
