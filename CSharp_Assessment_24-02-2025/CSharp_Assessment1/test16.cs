using System;

namespace VehicleFactoryPattern
{
    public interface IVehicle
    {
        void Drive();
    }

    public class Car : IVehicle
    {
        public void Drive()
        {
            Console.WriteLine("Driving a car.");
        }
    }

    public class Bike : IVehicle
    {
        public void Drive()
        {
            Console.WriteLine("Riding a bike.");
        }
    }

    public class VehicleFactory
    {
        public IVehicle GetVehicle(string vehicleType)
        {
            switch (vehicleType.ToLower())
            {
                case "car":
                    return new Car();
                case "bike":
                    return new Bike();
                default:
                    throw new ArgumentException("Invalid vehicle type");
            }
        }
    }

    public class test16
    {
        static void Main(string[] args)
        {
            VehicleFactory factory = new VehicleFactory();

            IVehicle car = factory.GetVehicle("car");
            car.Drive();

            IVehicle bike = factory.GetVehicle("bike");
            bike.Drive();
        }
    }
}
