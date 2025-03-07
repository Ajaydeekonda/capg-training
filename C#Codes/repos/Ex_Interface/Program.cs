using System;

// Interface 1
interface IFirst
{
    void CommonMethod();
    void FirstUniqueMethod();
}

// Interface 2
interface ISecond
{
    void CommonMethod();
    void SecondUniqueMethod();
}

// Child Class implementing both interfaces
class ChildClass : IFirst, ISecond
{
    // Implementing the common method for IFirst
    void IFirst.CommonMethod()
    {
        Console.WriteLine("CommonMethod from IFirst");
    }

    // Implementing the common method for ISecond
    void ISecond.CommonMethod()
    {
        Console.WriteLine("CommonMethod from ISecond");
    }

    // Implementing the unique method for IFirst
    public void FirstUniqueMethod()
    {
        Console.WriteLine("FirstUniqueMethod from IFirst");
    }

    // Implementing the unique method for ISecond
    public void SecondUniqueMethod()
    {
        Console.WriteLine("SecondUniqueMethod from ISecond");
    }
}

class Program
{
    static void Main()
    {
        //ChildClass obj = new ChildClass();

        //// Referencing the common method using IFirst
        //IFirst firstRef = obj;
        //firstRef.CommonMethod();
        //firstRef.FirstUniqueMethod();

        //// Referencing the common method using ISecond
        //ISecond secondRef = obj;
        //secondRef.CommonMethod();
        //secondRef.SecondUniqueMethod();

        //Maths maths = new Maths();
        //Maths alg = new Algorithm();
        //alg.Display();
        //maths.Display();
        int a = 10;



    }
}
