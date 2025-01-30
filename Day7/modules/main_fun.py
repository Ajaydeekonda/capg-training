from customers import Customers
from orders import Orders
from order_items import Order_Items
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


if __name__ == "__main__":
    main()