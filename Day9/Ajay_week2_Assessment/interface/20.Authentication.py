from abc import ABC,abstractmethod

class UserAuthentication(ABC):
    
    @abstractmethod
    def register(self,username,password):
        pass
    
    @abstractmethod
    def login(self,username,password):
        pass
    
    @abstractmethod
    def logout(self):
        pass
    
class GoogleAuth(UserAuthentication):
    
    def __init__(self):
        self.users = {}
    
    def register(self,username,password):
        self.users[username] = password
    
    def login(self,username,password):
        if username in self.users and self.users[username] == password:
            print("Login successful")
        else:
            print("Login failed")
            
    def logout(self):
        print("Logout successful")
        
class FacebookAuth(UserAuthentication):
    
    def __init__(self):
        self.users = {}
    
    def register(self,username,password):
        self.users[username] = password
    
    def login(self,username,password):
        if username in self.users and self.users[username] == password:
            print("Login successful")
        else:
            print("Login failed")
            
    def logout(self):
        print("Logout successful")
        
        
if __name__ == "__main__":
    
    google = GoogleAuth()
    google.register("user1","password1")
    google.register("user2","password2")
    google.login("user1","password1")
    google.login("user2","password2")
    google.logout()
    
    facebook = FacebookAuth()
    facebook.register("user1","password1")
    facebook.login("user1","password1")
    facebook.logout()