import threading
import time

def daemon():
    while True:
        print("Daemon thread is Executing....")
        time.sleep(2)
        
daemon_thread = threading.Thread(target=daemon,daemon=True,)
daemon_thread.start()
daemon_thread.join(5)
# time.sleep(10)
print("Main Executed\n")