using System;

public interface IDiscountStrategy
{
    decimal ApplyDiscount(decimal total);
}

public class NoDiscount : IDiscountStrategy
{
    public decimal ApplyDiscount(decimal total)
    {
        return total;
    }
}

public class PercentageDiscount : IDiscountStrategy
{
    private readonly decimal _percentage;

    public PercentageDiscount(decimal percentage)
    {
        _percentage = percentage;
    }

    public decimal ApplyDiscount(decimal total)
    {
        return total - (total * _percentage / 100);
    }
}

public class FixedAmountDiscount : IDiscountStrategy
{
    private readonly decimal _amount;

    public FixedAmountDiscount(decimal amount)
    {
        _amount = amount;
    }

    public decimal ApplyDiscount(decimal total)
    {
        return total - _amount;
    }
}

public class ShoppingCart
{
    private IDiscountStrategy _discountStrategy;

    public void SetDiscountStrategy(IDiscountStrategy discountStrategy)
    {
        _discountStrategy = discountStrategy;
    }

    public decimal CalculateTotal(decimal total)
    {
        return _discountStrategy.ApplyDiscount(total);
    }
}

class test20
{
    static void Main(string[] args)
    {
        ShoppingCart cart = new ShoppingCart();

        Console.WriteLine("Enter total amount:");
        decimal total = Convert.ToDecimal(Console.ReadLine());

        Console.WriteLine("Choose discount type: 1. No Discount 2. Percentage Discount 3. Fixed Amount Discount");
        int choice = Convert.ToInt32(Console.ReadLine());

        switch (choice)
        {
            case 1:
                cart.SetDiscountStrategy(new NoDiscount());
                break;
            case 2:
                Console.WriteLine("Enter discount percentage:");
                decimal percentage = Convert.ToDecimal(Console.ReadLine());
                cart.SetDiscountStrategy(new PercentageDiscount(percentage));
                break;
            case 3:
                Console.WriteLine("Enter discount amount:");
                decimal amount = Convert.ToDecimal(Console.ReadLine());
                cart.SetDiscountStrategy(new FixedAmountDiscount(amount));
                break;
            default:
                Console.WriteLine("Invalid choice");
                return;
        }

        decimal finalTotal = cart.CalculateTotal(total);
        Console.WriteLine($"Final total after discount: {finalTotal}");
    }
}
