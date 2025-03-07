using System;
public interface IPrintable
{
    void Print();
}

public interface ISerializable
{
    void Serialize();
}

public class Report : IPrintable, ISerializable
{
    public void Print()
    {
        Console.WriteLine("Printing report");
    }
    public void Serialize()
    {
        Console.WriteLine("Serializing report");
    }
}

public class test9
{
    public static void Main()
    {
        Report r = new Report();
        r.Print();
        r.Serialize();
    }
}