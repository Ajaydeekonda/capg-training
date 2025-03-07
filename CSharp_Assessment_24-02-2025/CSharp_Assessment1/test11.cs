using System;
public class ComplexNumber
{
    public double Real { get; set; }
    public double Imaginary { get; set; }
    public ComplexNumber(double real, double imaginary)
    {
        Real = real;
        Imaginary = imaginary;
    }
    public static ComplexNumber operator + (ComplexNumber c1, ComplexNumber c2)
    {
        return new ComplexNumber(c1.Real + c2.Real, c1.Imaginary + c2.Imaginary);
    }
}

public class test11
{
    public static void Main()
    {
        ComplexNumber c1 = new ComplexNumber(1, 2);
        ComplexNumber c2 = new ComplexNumber(2, 3);
        ComplexNumber c3 = c1 + c2;
        Console.WriteLine("Real: {0}, Imaginary: {1}", c3.Real, c3.Imaginary);
    }
}