import time
import threading
import queue

def producer(q):
    
    for i in range(10):
        q.put(f"item {i}")
        print(f"Produced an item {i}\n")
def consumer(q):
    
    while True:
        if q.qsize() == 0:
            break
        item = q.get()
        if item is None:
            break
        print(f"Consumed {item}\n")
        time.sleep(2)
q = queue.Queue()

producer_thread = threading.Thread(target=producer,args=(q,))
consumer_thread = threading.Thread(target=consumer,args=(q,))
producer_thread.start()
consumer_thread.start()
producer_thread.join()
q.put(None)
consumer_thread.join()
# consumer_thread.join()

print("Produced and Consumed ")



        
    