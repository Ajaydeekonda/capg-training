using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Employee
{
    public string Name { get; set; }
    public float Salary { get; set; }

    public Employee(string name, float salary)
    {
        Name = name;
        Salary = salary;
    }
}

public class Manager : Employee
{
    public float bonus { get; set; }
    public Manager(string name, float salary, float Bonus) : base(name, salary)
    {
        bonus = Bonus;
    }
}

public class test3
{
    public static void Main()
    {
        Employee emp = new Manager("John", 1000, 500);
        Console.WriteLine("Name: " + emp.Name);
        Console.WriteLine("Salary: " + emp.Salary);
        Console.WriteLine("Bonus: " + ((Manager)emp).bonus);
    }
}