namespace InherTest
{
    class Employee
    {
        public string Name { get; set; }
        public int Salary { get; set; }

        public Employee(string name, int salary) 
        {
            Name = name;
            Salary = salary;
        }
    }

    class Manager : Employee
    {
        public int Bonus { get; set; }

        public Manager(string name, int salary, int bonus): base(name, salary)
        {
            Bonus = bonus;
        }

        public void displayDetails()
        {
            Console.WriteLine($"Name: {base.Name}, Salary: {base.Salary}, Bonus: {Bonus}");
        }
    }


    class EmployeeMain
    {
        public static void Main(string[] args)
        {
            Manager man = new Manager("Ajay", 100000, 20000);
            man.displayDetails();
        }
    }
}
