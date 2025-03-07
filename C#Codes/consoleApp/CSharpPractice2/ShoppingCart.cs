using System;
using System.Collections.Generic;

namespace CSharpPractice2
{
    class ShoppingCart
    {
        private List<string> items = new List<string>();

        public void AddItem(string item)
        {
            if (!string.IsNullOrWhiteSpace(item))
            {
                items.Add(item);
            }
        }

        public void RemoveItem(string item)
        {
            items.Remove(item);
        }

        public List<string> GetItems()
        {
            return new List<string>(items);
        }
    }
}
