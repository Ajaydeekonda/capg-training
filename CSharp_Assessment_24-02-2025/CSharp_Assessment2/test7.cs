using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public interface ISwimmable
{
    void Swim();
}

public interface IFlyable
{
    void Fly();
}

public class Duck : ISwimmable, IFlyable
{
    public void Swim()
    {
        Console.WriteLine("Duck is swimming");
    }
    public void Fly()
    {
        Console.WriteLine("Duck is flying");
    }
}

public class test7
{
    public static void Main()
    {
        Duck duck = new Duck();
        duck.Swim();
        duck.Fly();
    }
}