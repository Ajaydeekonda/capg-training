using System;
public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }

    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }

    public virtual void GetDetails()
    {
        Console.WriteLine("Name: {0}, Age: {1}", Name, Age);
    }
}

public class Student : Person
{
    public int RollNo { get; set; }

    public Student(string name, int age, int rollno) : base(name, age)
    {
        RollNo = rollno;
    }

    public override void GetDetails()
    {
        Console.WriteLine("Name: {0}, Age: {1}, RollNo: {2}", Name, Age, RollNo);
    }
}

public class Teacher : Person
{
    public string Subject { get; set; }

    public Teacher(string name, int age, string subject) : base(name, age)
    {
        Subject = subject;
    }

    public override void GetDetails()
    {
        Console.WriteLine("Name: {0}, Age: {1}, Subject: {2}", Name, Age, Subject);
    }
}

public class test6
{
    public static void Main()
    {
        Person s = new Student("John", 20, 1);
        Person t = new Teacher("Smith", 30, "Maths");
        s.GetDetails();
        t.GetDetails();
    }
}
