namespace CsharpTest
{
    class Vehicle
    {
        public virtual void start()
        {
            Console.WriteLine("Start the Vehicle");
        }
    }

    class Car: Vehicle
    {
        public override void start()
        {
            Console.WriteLine("Start the Car");
        }
    }

    class Bike: Vehicle
    {
        public override void start()
        {
            Console.WriteLine("Start the Bike");
        }
    }

    class VehicleMain
    {
        public static void Main(string[] args)
        {
            Vehicle v = new Vehicle();
            v.start();
            Car car = new Car();
            car.start();
            Bike bike = new Bike();
            bike.start();
        }
    }
}
