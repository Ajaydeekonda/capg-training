using System;
public abstract class Shape
{
    public abstract double CalulateArea();
}

public class Circle : Shape
{
    private double _radius;
    public Circle(double radius)
    {
        _radius = radius;
    }
    public override double CalulateArea()
    {
        return Math.PI * _radius * _radius;
    }
}

public class Rectangle : Shape
{
    private double _length;
    private double _breadth;
    public Rectangle(double length, double breadth)
    {
        _length = length;
        _breadth = breadth;
    }
    public override double CalulateArea()
    {
        return _length * _breadth;
    }
}


public class test4
{
    public static void Main()
    {
        Circle c = new Circle(5);
        Rectangle r = new Rectangle(5, 10);
        Console.WriteLine("Area of Circle is {0}", c.CalulateArea());
        Console.WriteLine("Area of Rectangle is {0}", r.CalulateArea());
    }
}