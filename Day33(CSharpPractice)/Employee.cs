using System;

namespace Basics
{
    public class Employee
    {
        public int Id { get; set; }
        public string Name { get; set; }

        public Employee(int id, string name)
        {
            Id = id;
            Name = name;
        }

        public override string ToString()
        {
            return $"ID: {Id}, Name: {Name}";
        }
    }

    class Program
    {
        static void Main()
        {
            Employee emp = new Employee(1, "John Doe");
            Console.WriteLine(emp);
        }
    }
}
