def shoppingCart():
    cart = {}
    
    print("""Enter 'add' to add an item
'view' to view the cart
'Total' to calculate the Total price
'Exit' to Exit""")
    
    while True:
        choice = input("Enter your choice: ")
        if choice == "add":
            item = input("Enter the item name: ")
            price = float(input("Enter the price: $"))
            cart[item] = price
        if choice == "view":
            print("\nYour Cart:")
            for item, price in cart.items():
                print(f"{item}: ${price}")
        if choice == "total":
            total = sum(cart.values())
            print(f"\nTotal price: ${total}")
        if choice == "exit":
            print("\nExiting the shopping cart...")
            break
    
    
if __name__ == "__main__":
    shoppingCart()
            


