using System;
public class BankAccount
{
    public string AccountNo { get; set; }
    public int Balance { get; set; }
    public string Name { get; set; }

    public void deposit(int amount)
    {
        Balance += amount;
        Console.WriteLine("Deposited Successful");
    }
    public void withdraw(int amount)
    {
        if (amount > Balance)
        {
            Console.WriteLine("Insufficient Balance");
            return;
        }
        if (amount < 0)
        {
            Console.WriteLine("Enter positive amount");
            return;
        }
        Balance -= amount;
        Console.WriteLine("Withdrawal Successful");
    }


    public void display()
    {
        Console.WriteLine($"AccountNo:{AccountNo}\nAccount Holder Name: {Name}\nBalance: {Balance}");
    }
}