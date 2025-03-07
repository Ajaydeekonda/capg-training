using System;

namespace CsharpTest
{
    public interface IDiscountStrategy
    {
        double ApplyDiscount(double price);
    }

    public class NoDiscount : IDiscountStrategy
    {
        public double ApplyDiscount(double price) => price;
    }

    public class PercentageDiscount : IDiscountStrategy
    {
        private double _percentage;
        public PercentageDiscount(double percentage) => _percentage = percentage;
        public double ApplyDiscount(double price) => price - (price * _percentage / 100);
    }

    public class FixedAmountDiscount : IDiscountStrategy
    {
        private double _amount;
        public FixedAmountDiscount(double amount) => _amount = amount;
        public double ApplyDiscount(double price) => price - _amount;
    }

    class ShoppingCart
    {
        private IDiscountStrategy _discountStrategy;

        public ShoppingCart(IDiscountStrategy discountStrategy)
        {
            _discountStrategy = discountStrategy;
        }

        public double GetFinalPrice(double price)
        {
            return _discountStrategy.ApplyDiscount(price);
        }
    }

    class ShoppingCartMain
    {
        static void Main()
        {
            Console.Write("Enter price: ");
            double price = Convert.ToDouble(Console.ReadLine());

            Console.Write("Choose discount (None, Percentage, Fixed): ");
            string choice = Console.ReadLine();

            IDiscountStrategy discountStrategy = choice switch
            {
                "Percentage" => new PercentageDiscount(10),
                "Fixed" => new FixedAmountDiscount(50),
                _ => new NoDiscount()
            };

            ShoppingCart cart = new ShoppingCart(discountStrategy);
            Console.WriteLine($"Final Price: {cart.GetFinalPrice(price)}");
        }

    }
}