using System;
public class Vehicle
{
    public virtual void start()
    {
        Console.WriteLine("Vehicle started");
    }
}

public class Car : Vehicle
{
    public override void start()
    {
        Console.WriteLine("Car started");
    }
}

public class Bike : Vehicle
{
    public override void start()
    {
        Console.WriteLine("Bike started");
    }
}

public class test5
{
    public static void Main()
    {
        Car car = new Car();
        car.start();
        Bike bike = new Bike();
        bike.start();
    }
}