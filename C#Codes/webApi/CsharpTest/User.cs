namespace CsharpTest
{
    class User
    {
        public string Username { get; set; }
        public string Role { get; set; }

        public User(string username, string role)
        {
            Username = username;
            Role = role;
        }

        public virtual void AccessControl()
        {
            Console.WriteLine($"{Username} has basic user access.");
        }
    }

    
    class Admin : User
    {
        public Admin(string username) : base(username, "Admin")
        {
        }

        public override void AccessControl()
        {
            Console.WriteLine($"{Username} (Admin) has full access to all system features.");
        }
    }

    
    class Customer : User
    {
        public Customer(string username) : base(username, "Customer")
        {
        }

        public override void AccessControl()
        {
            Console.WriteLine($"{Username} (Customer) has limited access to customer-related features.");
        }
    }

    class UserMain
    {
        public static void Main(string[] args)
        {
            User adminUser = new Admin("Alice");
            adminUser.AccessControl();
            Console.WriteLine();
            User customerUser = new Customer("Bob");
            customerUser.AccessControl();
        }
    }
}
