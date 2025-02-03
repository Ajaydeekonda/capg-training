import threading
import time

def single_task():
    print("Started")
    time.sleep(10)
    print("Ended")
    
    
thread = threading.Thread(target=single_task)
thread.start()
thread.join()
print("thread executed successfully")