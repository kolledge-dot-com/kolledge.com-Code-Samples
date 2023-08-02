# How to stop a Thread in Python :
import time
def task():
   while True:
       print("Thread is running")
       time.sleep(1)


import threading
def main():
   # Create the thread
   thread = threading.Thread(target=task)
   # Start the thread
   thread.start()
   # Wait for user input
   input("Press Enter to stop the thread\n")
   # Stop the thread
   thread.join()