class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        print(self.message)
        
class Email(Notification):
    def __init__(self, message):
        self.message = message
        
    def send(self):
        print(f"Email: {self.message}")
        
class SMS(Notification):
    def __init__(self, message):
        self.message = message
        
    def send(self):
        print(f"SMS: {self.message}")
        
if __name__ == "__main__":
    
    email = Email("This is an email message")
    email.send()
    sms = SMS("This is an sms message")
    sms.send()
        