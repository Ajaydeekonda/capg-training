using System;
using System.Collections.Generic;
using System.Linq;

class Product
{
    public string Name { get; set; }
    public double Price { get; set; }
    public int StockQuantity { get; set; }

    public Product(string name, double price, int stockQuantity)
    {
        Name = name;
        Price = price;
        StockQuantity = stockQuantity;
    }
}

class ShoppingCart
{
    private List<Product> products = new List<Product>();

    public void AddProduct(Product product)
    {
        products.Add(product);
    }

    public void RemoveProduct(Product product)
    {
        products.Remove(product);
    }

    public double CalculateTotalPrice()
    {
        return products.Sum(p => p.Price);
    }
}
