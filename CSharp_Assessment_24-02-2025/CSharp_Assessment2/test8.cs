using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Person
{

}
public class Student : Person
{
}

public class test8
{
    public static void Main()
    {
        Student student = new Student();
        Person person = student;
        Console.WriteLine(person is Student);
        Student student1 = (Student)person;
        Console.WriteLine(student1 is Person);
    }
}