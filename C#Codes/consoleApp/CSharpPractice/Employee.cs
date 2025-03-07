using System;

class Employee
{
    public string Name { get; set; }
    public int ID { get; set; }
    public double Salary { get; protected set; }

    public Employee(string name, int id, double salary)
    {
        Name = name;
        ID = id;
        Salary = salary;
    }

    public virtual void DisplayInfo()
    {
        Console.WriteLine($"ID: {ID}, Name: {Name}, Salary: {Salary:C}");
    }
}

class FullTimeEmployee : Employee
{
    public FullTimeEmployee(string name, int id, double salary)
        : base(name, id, salary) { }
}

class PartTimeEmployee : Employee
{
    private double hourlyRate;
    private int hoursWorked;

    public PartTimeEmployee(string name, int id, double hourlyRate, int hoursWorked)
        : base(name, id, 0)
    {
        this.hourlyRate = hourlyRate;
        this.hoursWorked = hoursWorked;
        CalculateSalary();
    }

    private void CalculateSalary()
    {
        Salary = hourlyRate * hoursWorked;
    }
}

