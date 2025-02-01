class message:
    def __init__(self, msg):
        self.msg = msg

class error(message):
    def __init__(self, msg):
        self.msg = msg

class warning(message):
    def __init__(self, msg):
        self.msg = msg
        
class info(message):
    def __init__(self, msg):
        self.msg = msg
        
i = info("This is an info message")
e = error("This is an error message")
w = warning("This is a warning message")

def logger(msg:message):
    print(msg.msg)
    
logger(i)
logger(e)
logger(w)