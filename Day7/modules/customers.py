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