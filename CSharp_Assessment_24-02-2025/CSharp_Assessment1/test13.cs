using System;
public class BankingSystem
{
    public static double InterestRate { get; set; }

    public static double SetInterestRate(double rate)
    {
        InterestRate = rate;
        return InterestRate;
    }

    public static double CaluculateInterest(double amount)
    {
        return amount * InterestRate;
    }

}

public class test13
{
    public static void Main()
    {
        BankingSystem.SetInterestRate(0.05);
        Console.WriteLine("Interest rate: {0}", BankingSystem.InterestRate);
        double interest = BankingSystem.CaluculateInterest(1000);
        Console.WriteLine("Interest: {0}", interest);
        BankingSystem.SetInterestRate(5.0);
        Console.WriteLine("Interest rate: {0}", BankingSystem.InterestRate);
        interest = BankingSystem.CaluculateInterest(1000);
        Console.WriteLine("Interest: {0}", interest);
    }
}