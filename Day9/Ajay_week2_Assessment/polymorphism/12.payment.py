class Payment:
    
    def process_payment(self, amount):
        pass
    
class CreditCardPayment(Payment):
    
    def process_payment(self, amount):
        print(f"Credit card payment of ${amount} processed.")
        
class PayPalPayment(Payment):
    
    def process_payment(self, amount):
        print(f"PayPal payment of ${amount} processed.")
        
class BitcoinPayment(Payment):
    
    def process_payment(self, amount):
        print(f"Bitcoin payment of ${amount} processed.")
        
if __name__ == "__main__":
    
    credit_card = CreditCardPayment()
    credit_card.process_payment(100)
    
    paypal = PayPalPayment()
    paypal.process_payment(200)
    
    bitcoin = BitcoinPayment()
    bitcoin.process_payment(300)
    