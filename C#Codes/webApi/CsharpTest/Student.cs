namespace CsharpTest
{
    class Student
    {
        private int rollNo;
        private string name;
        public Student(int rollno,string name)
        {
            if (rollno < 0 || string.IsNullOrEmpty(name))
            {
                Console.WriteLine("\nPlease Enter valid rollno and name.\n");
            }
            else
            {
                this.rollNo = rollno;
                this.name = name;
                display();
            }

        }

        private void display()
        {
            Console.WriteLine($"\nRollNo:{this.rollNo},Name:{this.name}");
        }

        public static void Main(string[] args)
        {
            Console.Write("Enter rollno: ");
            int rollno = Convert.ToInt32(Console.ReadLine());
            Console.Write("\nEnter student name: ");
            string name = Console.ReadLine();
            Student student = new Student(rollno, name);
        }
    }
}

