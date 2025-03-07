namespace CsharpTest
{
    class Person
    {
        public string name;
        public int age;
        public Person(string name,int age) 
        {
            this.name = name;
            this.age = age;
        }

        public virtual void GetDetails()
        {
            Console.WriteLine($"Person's Name: {this.name}\nPerson's age: {this.age}");
        }
    }

    class student: Person
    {
        public string rollno;
        public string standard;
        public student(string rollno,string name,int age,string standard) :base(name,age)
        {
            this.rollno = rollno;
            this.standard = standard;
        }

        public override void GetDetails()
        {
            Console.WriteLine($"Details\nRollNo: " +
                $"{this.rollno}\nName: {this.name}\n" +
                $"Age: {this.age}\nStandard: {this.standard}");
        }

    }

    class Teacher: Person
    {
        public string id;
        public string department;
        public Teacher(string id, string name, int age, string department) : base(name, age)
        {
            this.id = id;
            this.department = department;
        }

        public override void GetDetails()
        {
            Console.WriteLine($"Details:\nId: {this.id}\nName: {this.name}\n" +
                $"Age: {this.age}\nDepartment: {this.department}");
        }
    }

    class PersonMain
    {
        public static void Main(string[] args)
        {
            Person P = new student("22h55a6203", "Ajay", 22, "IV/II");
            P.GetDetails();
        }
    }
}
