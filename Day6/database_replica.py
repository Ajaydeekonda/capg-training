import datetime

# Base class - Customers
class Customers:
    def __init__(self):
        # Initialize an empty list to store customers
        self.customer_list = []
    
    def add_customer(self, **kwargs):
        """
        Method to add a customer. We use **kwargs to accept a variable number of arguments.
        Args:
        - kwargs: The customer's details as keyword arguments.
        """
        # Append the customer details as a dictionary to the customer list
        self.customer_list.append(kwargs)

    def display_customers(self):
        """
        Method to display the customer list.
        It will print all the details of each customer in the list.
        """
        print("\nCustomer Details:")
        for customer in self.customer_list:
            print(f"Customer ID: {customer['cust_id']}, Name: {customer['name']}, "
                  f"Phone: {customer['phone']}, Email: {customer['email']}, "
                  f"Address: {customer['address']}")

# Derived class - Orders
class Orders(Customers):
    def __init__(self):
        """
        This class inherits from Customers.
        Initialize an empty list to store orders.
        """
        super().__init__()  # Inherit from Customers class
        self.orders_list = []
    
    def add_order(self, **kwargs):
        """
        Method to add an order. The order details are passed as keyword arguments.
        A timestamp for order date is automatically added when the order is created.
        """
        order_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current date and time
        kwargs['order_date'] = order_date  # Add current date to the order
        # Append the order details as a dictionary to the orders list
        self.orders_list.append(kwargs)

    def display_orders(self):
        """
        Method to display the order list.
        It will print all the details of each order in the list.
        """
        print("\nOrder Details:")
        for order in self.orders_list:
            print(f"Order ID: {order['order_id']}, Customer ID: {order['cust_id']}, "
                  f"Status: {order['order_status']}, Date: {order['order_date']}, "
                  f"Store ID: {order['store_id']}, Staff ID: {order['staff_id']}")

# Derived class - Order_Items
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

# Main Program
def main():
    """
    Main function to handle user input and interact with the classes.
    It allows the user to add customers, orders, and order items and displays the results.
    """
    # Create instances of each class
    customers = Customers()
    orders = Orders()
    order_items = Order_Items()

    # User input for Customers
    n = int(input("Enter number of customers: "))  # Number of customers
    for _ in range(n):
        cust_id = int(input("Enter customer ID: "))  # Customer ID
        name = input("Enter customer name: ")  # Customer Name
        phone = input("Enter customer phone: ")  # Customer Phone
        email = input("Enter customer email: ")  # Customer Email
        address = input("Enter customer address: ")  # Customer Address
        customers.add_customer(cust_id=cust_id, name=name, phone=phone, email=email, address=address)  # Add customer

    # User input for Orders
    m = int(input("\nEnter number of orders: "))  # Number of orders
    for _ in range(m):
        order_id = int(input("Enter order ID: "))  # Order ID
        cust_id = int(input("Enter customer ID for the order: "))  # Customer ID for this order
        order_status = input("Enter order status (e.g., Pending, Shipped, Delivered): ")  # Order Status
        store_id = int(input("Enter store ID: "))  # Store ID
        staff_id = int(input("Enter staff ID: "))  # Staff ID
        orders.add_order(order_id=order_id, cust_id=cust_id, order_status=order_status, store_id=store_id, staff_id=staff_id)  # Add order

    # User input for Order Items
    o = int(input("\nEnter number of order items: "))  # Number of order items
    for _ in range(o):
        order_id = int(input("Enter order ID for the item: "))  # Order ID
        item_id = int(input("Enter item ID: "))  # Item ID
        product_id = int(input("Enter product ID: "))  # Product ID
        quantity = int(input("Enter quantity: "))  # Quantity
        list_price = float(input("Enter list price: "))  # List Price
        discount = float(input("Enter discount percentage: "))  # Discount Percentage
        order_items.add_order_item(order_id=order_id, item_id=item_id, product_id=product_id, quantity=quantity, list_price=list_price, discount=discount)  # Add order item

    # Display all data
    customers.display_customers()  # Display all customers
    orders.display_orders()  # Display all orders
    order_items.display_order_items()  # Display all order items

# Run the main function
if __name__ == "__main__":
    main()
