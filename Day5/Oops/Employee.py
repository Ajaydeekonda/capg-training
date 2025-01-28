class Emp:
    def __init__(self,_id,Name,Age,salary,designation,contact,address,date_of_joining):
        self._id = _id
        self.Name = Name
        self.Age = Age
        self.salary = salary
        self.designation = designation
        self.contact = contact
        self.address = address
        self.date_of_joining = date_of_joining
    
    def emp_check_in():
        print("Employee checked in")
    
    def emp_check_out():
        print("Employee checked out")
        
    def update_contact(num):
        self.contact = num
        
    def update_address(ad):
        self.address = ad
        
    
    
    
    
    
    