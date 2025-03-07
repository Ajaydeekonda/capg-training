

namespace CsharpTest
{
    class Person
    {
        public void Show() => Console.WriteLine("I am a Person");
    }

    class Student : Person
    {
        public void Study() => Console.WriteLine("I am a Student");
    }

    class CastingExample
    {
        static void Main()
        {
            Student student = new Student();
            Person person = student;
            Student studentAgain = (Student)person;

            studentAgain.Show();
            studentAgain.Study();
        }
    }
}
