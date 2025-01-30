from orders import Orders
class Order_Items(Orders):
    def __init__(self):
        """
        This class inherits from Orders.
        Initialize an empty list to store order items.
        """
        super().__init__()  # Inherit from Orders class
        self.order_items_list = []
    
    def add_order_item(self, **kwargs):
        """
        Method to add an order item. The order item details are passed as keyword arguments.
        """
        # Append the order item details as a dictionary to the order items list
        self.order_items_list.append(kwargs)

    def display_order_items(self):
        """
        Method to display the order items list.
        It will print all the details of each order item in the list.
        """
        print("\nOrder Items Details:")
        for item in self.order_items_list:
            print(f"Order ID: {item['order_id']}, Item ID: {item['item_id']}, "
                  f"Product ID: {item['product_id']}, Quantity: {item['quantity']}, "
                  f"List Price: {item['list_price']}, Discount: {item['discount']}")