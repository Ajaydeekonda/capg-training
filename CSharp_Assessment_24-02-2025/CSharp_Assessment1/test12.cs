using System;
public class Department
{
    public string Manager { get; set; }

    public Department(string manager)
    {
        Manager = manager;
    }

    public Department(Department other)
    {
        Manager = other.Manager;
    }

    public Department ShallowCopy()
    {
        return (Department)this.MemberwiseClone();
    }
}

public class test12
{
    public static void Main()
    {
        Department d = new Department("John");
        Console.WriteLine("Manager: {0}", d.Manager);

        Department d1 = d.ShallowCopy();
        d1.Manager = "Smith";
        Console.WriteLine("Manager after shallow copy: {0}", d.Manager);

        Department d2 = new Department(d);
        d2.Manager = "Alice";
        Console.WriteLine("Manager after deep copy: {0}", d.Manager);
        Console.WriteLine("Manager in deep copied object: {0}", d2.Manager);
    }
}

