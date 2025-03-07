using System;

public class Maths
{
    public void Display()
    {
        Console.WriteLine("I'm from parent class");
    }
}

public class Algorithm : Maths
{
    public void Display()
    {
        Console.WriteLine("I'm from child class");
    }
}