namespace CSharpPractice2
{
    class Employee
    {
        public string Name { get; private set; }
        public double Salary { get; private set; }
        public int Id { get; private set; }

        public Employee(string name, double salary, int id)
        {
            Name = name;
            Salary = salary;
            Id = id;
        }

        public void IncreaseSalary(double percentage)
        {
            Salary += Salary * (percentage / 100);
        }
    }
}
