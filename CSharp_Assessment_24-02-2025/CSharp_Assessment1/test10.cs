using System;
public class User
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
        Console.WriteLine("Username: {0}, Role: {1}", Username, Role);
    }
}

public class Admin : User
{
    public Admin(string username, string role) : base(username, role)
    {
    }
    public override void AccessControl()
    {
        Console.WriteLine("Username: {0}, Role: {1}, Access: Full", Username, Role);
    }
}

public class Customer : User
{
    public Customer(string username, string role) : base(username, role)
    {
    }
    public override void AccessControl()
    {
        Console.WriteLine("Username: {0}, Role: {1}, Access: Limited", Username, Role);
    }
}

public class test10
{
    public static void Main()
    {
        User a = new Admin("John", "Admin");
        User c = new Customer("Smith", "Customer");
        a.AccessControl();
        c.AccessControl();
    }
}