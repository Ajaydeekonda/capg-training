namespace CsharpTest
{
    class Manager
    {
        public string Name { get; set; }

        public Manager(string name)
        {
            Name = name;
        }

        public Manager getClone()
        {
            return (Manager)this.MemberwiseClone();
        }
    }
    class Department
    {
        public string DepartmentName { get; set; }
        public Manager DepartmentManager { get; set; }

        public Department(string departmentName, Manager departmentManager)
        {
            DepartmentName = departmentName;
            DepartmentManager = departmentManager;
        }

        public Department ShallowCopy()
        {
            return (Department)this.MemberwiseClone();
        }

        public Department DeepCopy()
        {
            Department clonedDepartment = (Department)this.MemberwiseClone();
            clonedDepartment.DepartmentManager = new Manager(this.DepartmentManager.Name);
            return clonedDepartment;
        }
    }

    class DepartmentMain 
    {
        public static void Main(string[] args)
        {
            Manager m = new Manager("Ajay");
            Department d1 = new Department("EEE", m);
            Department shallowCopy = d1.ShallowCopy();
            Department deepCopy = d1.DeepCopy();

            Console.WriteLine($"Shallow Copy\nDepartment Name: {shallowCopy.DepartmentName}\n" +
                $"Manager Name: {shallowCopy.DepartmentManager.Name}");
            Console.WriteLine($"Deep Copy\nDepartment Name: {shallowCopy.DepartmentName}\n" +
                $"Manager Name: {deepCopy.DepartmentManager.Name}");
            m.Name = "Anirudh";
            Console.WriteLine($"Shallow Copy\nDepartment Name: {shallowCopy.DepartmentName}\n" +
               $"Manager Name: {shallowCopy.DepartmentManager.Name}");
            Console.WriteLine($"Deep Copy\nDepartment Name: {shallowCopy.DepartmentName}\n" +
                $"Manager Name: {deepCopy.DepartmentManager.Name}");
        }
    }

}
