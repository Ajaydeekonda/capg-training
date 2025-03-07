using System;
using System.Linq;
using System.Collections.Generic;

public class Hello
{
    static void Main(string[] args)
    {
        List<Employee> employees = new List<Employee> {
            new Employee { Id = 1, Name = "John", Age = 30 },
            new Employee { Id = 2, Name = "Sara", Age = 25 },
            new Employee { Id = 3, Name = "Mike", Age = 35 }
        };

        var youngEmployees = from e in employees
                             where e.Age < 30
                             select e;

        foreach (var employee in youngEmployees)
        {
            Console.WriteLine($"Name: {employee.Name}, Age: {employee.Age}");
        }
    }
}

public class Employee
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int Age { get; set; }
}
