using System;

namespace VehicleFactory
{
    public interface IVehicle
    {
        void Drive();
    }

    public class Car : IVehicle
    {
        public void Drive()
        {
            Console.WriteLine("Car is moving...");
        }
    }

    public class Bike : IVehicle
    {
        public void Drive()
        {
            Console.WriteLine("Bike is running...");
        }
    }

    class VehicleFactory
    {
        public static IVehicle GetVehicle(string type)
        {
            if (type == "Car") return new Car();
            if (type == "Bike") return new Bike();
            return null;
        }
    }

    class VehicleFactoryMain
    {
        static void Main()
        {
            Console.Write("Enter vehicle type (Car/Bike): ");
            string type = Console.ReadLine();

            IVehicle vehicle = VehicleFactory.GetVehicle(type);

            if (vehicle != null)
                vehicle.Drive();
            else
                Console.WriteLine("Invalid vehicle type");
        }
    }
}
