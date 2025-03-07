using System;

class Vehicle
{
    public virtual void StartEngine()
    {
        Console.WriteLine("Starting vehicle engine...");
    }
}

class Car : Vehicle
{
    public override void StartEngine()
    {
        Console.WriteLine("Car engine started with key ignition.");
    }
}

class Motorcycle : Vehicle
{
    public override void StartEngine()
    {
        Console.WriteLine("Motorcycle engine started with button press.");
    }
}
