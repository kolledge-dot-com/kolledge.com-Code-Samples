# Creating a Daemon Thread in python :
import threading
import time

def daemon():
   while True:
       print("Daemon thread is running.")
       time.sleep(1)

# Creating a daemon thread using the setDaemon() method
d = threading.Thread(target=daemon)
d.setDaemon(True)
d.start()

# Wait for user input
input("Press any key to exit.\n")