using System;

public class BankAccount
{
    private double balance;

    public BankAccount(double initialBalance)
    {
        balance = initialBalance;
    }

    public void Debit(double amount)
    {
        if (balance >= amount)
        {
            balance -= amount;
        }
        else
        {
            Console.WriteLine("Insufficient funds");
        }
    }

    public void Credit(double amount)
    {
        balance += amount;
    }

    public double GetBalance()
    {
        return balance;
    }
}

public class test1
{
    public static void Main(string[] args)
    {
        BankAccount ba = new BankAccount(100.00);
        ba.Credit(100.00);
        ba.Debit(50.00);
        Console.WriteLine($"Current balance is ${ba.GetBalance()}"); 
    }
}
