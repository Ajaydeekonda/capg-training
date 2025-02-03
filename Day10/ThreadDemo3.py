import threading
import time

def single_task():
    count =0
    for i in range(200):
        count+=1
    print("1.complete")
    
def sec_task():
    count =0
    for i in range(100000):
        count+=1
    
    print("2.complete")
    
Thread1 = threading.Thread(target=single_task)
Thread2 = threading.Thread(target=sec_task)
Thread2.start()
Thread1.start()

print("main")