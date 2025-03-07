namespace CsharpTest
{
    class Bank
    {
        public static int interestRate = 10;

        public static void setInterestRate(int interestRate)
        {
            Bank.interestRate = interestRate;
        }
    }

    class BankMain
    {
        public static void Main(string[] args)
        {
            Bank bank = new Bank();
            Bank.setInterestRate(20);
            Console.WriteLine(Bank.interestRate);
        }
    }
}
