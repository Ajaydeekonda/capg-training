using System;

namespace CsharpTest
{
    class Product
    {
        public string Name { get; set; }
        public double Price { get; set; }

        public Product(string name, double price)
        {
            Name = name;
            Price = price;
        }

        public virtual double GetDiscountedPrice() => Price;
    }

    class ElectronicProduct : Product
    {
        public ElectronicProduct(string name, double price) : base(name, price) { }

        public override double GetDiscountedPrice() => Price * 0.90;
    }

    class ClothingProduct : Product
    {
        public ClothingProduct(string name, double price) : base(name, price) { }

        public override double GetDiscountedPrice() => Price * 0.80;
    }

    class ProductMain
    {
        static void Main()
        {
            Product laptop = new ElectronicProduct("Laptop", 1000);
            Product shirt = new ClothingProduct("Shirt", 50);

            Console.WriteLine($"{laptop.Name} Discounted Price: {laptop.GetDiscountedPrice()}");
            Console.WriteLine($"{shirt.Name} Discounted Price: {shirt.GetDiscountedPrice()}");
        }
    }
}
