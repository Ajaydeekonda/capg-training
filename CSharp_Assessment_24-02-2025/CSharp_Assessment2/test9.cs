using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Product
{
    public string Name { get; set; }
    public double Price { get; set; }
    public Product(string name, double price)
    {
        Name = name;
        Price = price;
    }

    public virtual void GetDiscountedPrice(float Discount)
    {

    }
}

public class ElectronicProduct : Product
{
    public ElectronicProduct(string name, double price) : base(name, price)
    {
    }
    public override void GetDiscountedPrice(float Discount)
    {
        Console.WriteLine("Discounted price for electronic product: " + Price * Discount);
    }
}

public class ClothingProduct : Product
{
    public ClothingProduct(string name, double price) : base(name, price)
    {
    }
    public override void GetDiscountedPrice(float Discount)
    {
        Console.WriteLine("Discounted price for clothing product: " + Price * Discount);
    }
}

public class test9
{
    public static void Main()
    {
        Product electronicProduct = new ElectronicProduct("Laptop", 100000);
        Product clothingProduct = new ClothingProduct("Shirt", 5000);
        electronicProduct.GetDiscountedPrice(0.9f);
        clothingProduct.GetDiscountedPrice(0.8f);
    }
}