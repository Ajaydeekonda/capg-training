namespace InherTest
{
    class Vehicle
    {
        public string Brand { get; set; }
        public int Speed { get; set; }


        public Vehicle(string brand, int speed)
        {
            Brand = brand;
            Speed = speed;
        }

        public void DisplayInfo()
        {
            Console.Write($"Brand: {Brand}, Speed: {Brand}");
        }
    }

    class Car : Vehicle
    {
        public string CarName { get; set; }

        public Car(string carName, string brand, int speed) : base(brand, speed)
        {
            CarName = carName;
        }

        public void Display()
        {
            Console.Write($"\nName: {CarName}, ");
            base.DisplayInfo();
        }

    }

    class Bike : Vehicle
    {
        public string BikeName { get; set; }

        public Bike(string carName, string brand, int speed) : base(brand, speed)
        {
            BikeName = carName;
        }
        public void Display()
        {
            Console.Write($"\nName: {BikeName}, ");
            base.DisplayInfo();
        }

    }

    class VehicleMain
    {
        public static void Main(string[] args)
        {
            Car car = new Car("Punch", "Tata", 150);
            car.Display();
            Bike bike = new Bike("Glamour", "Hero", 120);
            bike.Display();
        }
    }
}
