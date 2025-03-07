using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Account
{
    public virtual void CalculateInterest()
    {
        Console.WriteLine("Calculating interest for account");
    }
}

public class SavingsAccount : Account
{
    public override sealed void CalculateInterest()
    {
        Console.WriteLine("Calculating interest for savings account");
    }
}

public class test6
{
    public static void Main()
    {
        Account acc = new SavingsAccount();
        acc.CalculateInterest();
    }
}