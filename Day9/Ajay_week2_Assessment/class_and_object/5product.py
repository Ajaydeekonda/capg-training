class Product:
    
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
        
    def check_availability(self,quantity):
        if quantity > self.stock:
            return "Out of Stock"
        return "In Stock"

if __name__ == "__main__":
    name = input("Enter the Product Name: ")
    price = float(input("Enter the Price: "))
    stock = int(input("Enter the Stock: "))
    product = Product(name,price,stock)
    
    quantity = int(input("Enter the Quantity: "))
    print(product.check_availability(quantity))