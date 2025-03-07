namespace CsharpTest
{
    public class BankAccount
    {
        private int balance;

        public void deposit(int amount)
        {
            if (amount <= 0)
            {
                Console.WriteLine("\nEnter a valid positive amount to deposit.\n");
                return;
            }

            this.balance += amount;
            Console.WriteLine($"\nDeposited successfully.\nBalance amount = {balance}\n");
        }

        public void withdraw(int amount)
        {
            if (amount <= 0)
            {
                Console.WriteLine("\nEnter a valid positive amount to withdraw.\n");
                return;
            }

            if (amount > this.balance)
            {
                Console.WriteLine("\nInsufficient balance.\n");
                return;
            }

            this.balance -= amount;
            Console.WriteLine($"\nWithdrawal successful.\nBalance amount = {balance}\n");
        }

        public static void Main(string[] args)
        {
            BankAccount account = new BankAccount();

            while (true)
            {
                Console.WriteLine("Enter options:\n1. Deposit amount\n2. Withdraw amount\n3. Exit\n");
                Console.Write("Enter your choice: ");
                int option = Convert.ToInt32(Console.ReadLine());

                if (option == 1)
                {
                    Console.Write("\nEnter the amount to deposit: ");
                    int amount = Convert.ToInt32(Console.ReadLine());
                    account.deposit(amount);
                }
                else if (option == 2)
                {
                    Console.Write("\nEnter the amount to withdraw: ");
                    int amount = Convert.ToInt32(Console.ReadLine());
                    account.withdraw(amount);
                }
                else if (option == 3)
                {
                    Console.WriteLine("\nExiting the program. Thank you!\n");
                    break;
                }
                else
                {
                    Console.WriteLine("\nEnter a valid option (1, 2, or 3).\n");
                }
            }
        }
    }
}
