# Multi-threaded program in python :
import threading
import time

def worker(num):
   """Thread worker function"""
   time.sleep(1)
   print(f'Worker {num} executed')

threads = []
for i in range(5):
   t = threading.Thread(target=worker, args=(i,))
   threads.append(t)
   t.start()