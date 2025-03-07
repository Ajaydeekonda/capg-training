using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Vehiclee
{
    public string brand { get; set; }
    public float speed { get; set; }
    public virtual void DisplayInfo()
    {
        Console.WriteLine("Brand: " + brand);
        Console.WriteLine("Speed: " + speed);
    }
    public Vehiclee(string brand, float speed)
    {
        this.brand = brand;
        this.speed = speed;
    }
}

public class Carr : Vehiclee
{
    public Carr(string brand, float speed) : base(brand, speed)
    {
    }
    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine("This is a car");
    }
}

public class Bikee : Vehiclee
{
    public Bikee(string brand, float speed) : base(brand, speed)
    {
    }

    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine("This is a bike");
    }
}

public class test2
{
    public static void Main()
    {
        Vehiclee car = new Carr("Toyota", 100);
        Vehiclee bike = new Bikee("Yamaha", 50);
        car.DisplayInfo();
        bike.DisplayInfo();
    }
}
