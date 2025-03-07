namespace CSharpPractice2
{
    class Student
    {
        public string Name { get; private set; }
        public int Age { get; private set; }
        public double Grade { get; private set; }

        public Student(string name, int age, double grade)
        {
            Name = name;
            Age = age;
            Grade = grade;
        }

        public void UpdateGrade(double newGrade)
        {
            if (newGrade >= 0 && newGrade <= 100)
            {
                Grade = newGrade;
            }
        }
    }
}
