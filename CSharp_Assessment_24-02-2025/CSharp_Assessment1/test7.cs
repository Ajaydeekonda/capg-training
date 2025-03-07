using System;
public class Caluculator
{
    public int Add(int a, int b)
    {
        return a + b;
    }

    public int Add(int a, int b, int c)
    {
        return a + b + c;
    }

    public double Add(double a, double b)
    {
        return a + b;
    }

}

public class test7
{
    public static void Main()
    {
        Caluculator c = new Caluculator();
        Console.WriteLine(c.Add(1, 2));
        Console.WriteLine(c.Add(1, 2, 3));
        Console.WriteLine(c.Add(1.5, 2.5));
    }
}
