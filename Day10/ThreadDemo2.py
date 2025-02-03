import threading
import time

def single_task():
    
    print("1.started")
    time.sleep(3)
    print("1.ended")
    
def sec_task():
    print("2.started")
    time.sleep(10)
    print("2.ended")
    
def third_task():
    print("3.started")
    time.sleep(4)
    print("3.ended")
    
thread1 = threading.Thread(target=single_task)
thread2 = threading.Thread(target=sec_task)
thread3 = threading.Thread(target=third_task)

thread1.start()
thread2.start()
thread3.start()
print("Finished")
