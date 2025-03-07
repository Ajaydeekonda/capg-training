namespace CSharpPractice2
{
    class InventoryItem
    {
        private string itemName;
        private int stockQuantity;

        public InventoryItem(string name, int quantity)
        {
            itemName = name;
            stockQuantity = quantity >= 0 ? quantity : 0;
        }

        public void Restock(int amount)
        {
            if (amount > 0)
                stockQuantity += amount;
        }

        public void Sell(int amount)
        {
            if (amount > 0 && stockQuantity >= amount)
                stockQuantity -= amount;
        }

        public int GetStock()
        {
            return stockQuantity;
        }
    }

}
