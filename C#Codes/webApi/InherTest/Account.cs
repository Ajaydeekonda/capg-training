
namespace InherTest
{
    class Account
    {
        public virtual double CalculateInterest()
        {
            return 0;
        }
    }

    sealed class SavingsAccount : Account
    {   
        public string Bank { get; set; }
        public string AccountNumber { get; set; }

        public int Balance { get; set; }
        public int AccountAge { get; set; }

        public SavingsAccount(string bank,string acc,int bal,int accAge)
        {
            Bank = bank;
            AccountNumber = acc;
            Balance = bal;
            AccountAge = accAge;
        }

        public override double CalculateInterest()
        {
            double rate = AccountAge < 5 ? 0.03 : 0.05;
            return Balance * rate;
        }
    }

    class AccountMain
    {
        public static void Main(string[] args)
        {
            SavingsAccount sv = new SavingsAccount("Kotak", "868839826", 40000, 3);
            Console.WriteLine(sv.CalculateInterest());
        }
    }
}
