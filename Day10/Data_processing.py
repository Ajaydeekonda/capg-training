import threading
import time

data_chuncks = [
    list(range(200000)),
    list(range(300000)),
    list(range(400000))
]

def data_process(data):
    print(f"Size of the data is {len(data)}\n")
    start = time.time()
    res = sum(data)
    end = time.time()
    print(f"Sum after processing the data of size {len(data)}:{res}\n time taken : {end - start}ns")
    
threads = []

for chunck in data_chuncks:
    thread = threading.Thread(target=data_process,args=(chunck,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print("Finished")