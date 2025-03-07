using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Vehicle
{
    public string brand { get; set; }
    public float speed { get; set; }

    public void DisplayInfo()
    {
        Console.WriteLine("Brand: " + brand);
        Console.WriteLine("Speed: " + speed);
    }

    public Vehicle(string brand, float speed)
    {
        this.brand = brand;
        this.speed = speed;
    }
}

public class Car : Vehicle
{
    public Car(string brand, float speed) : base(brand, speed)
    {
    }
}

public class Bike : Vehicle
{
    public Bike(string brand, float speed) : base(brand, speed)
    {
    }
}

public class test1
{
    public static void Main()
    {
        Car car = new Car("Toyota", 100);
        Bike bike = new Bike("Yamaha", 50);
        car.DisplayInfo();
        bike.DisplayInfo();
    }
}