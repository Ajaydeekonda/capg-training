from abc import ABC,abstractmethod

class Mail(ABC):
    
    @abstractmethod
    def send(self):
        pass
    
class Email(Mail):
    
    def send(self):
        print("Email")
        
    def receive(self):
        print("receive")
    
# class SMS(Email):
    
#     def display(self):
#         print("SMS")
    
# e = Email()
# e.send()
# s = SMS()
# s.display()

class SMS(Mail):
    
    def send(self):
        print("SMS")
        
class whatsApp(Mail):
    
    def send(self):
        print("WhatsApp")

e = Email()
s = SMS()
w = whatsApp()
w.send()
