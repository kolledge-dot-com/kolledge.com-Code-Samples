# Using the submit() method :
from concurrent.futures import ThreadPoolExecutor
import time

def task(num):
   print("Task %s started." % num)
   time.sleep(1)
   print("Task %s completed." % num)

# Create a thread pool with 5 threads
with ThreadPoolExecutor(max_workers=5) as executor:
   # Submit 10 tasks to the thread pool
   for i in range(1, 11):
       executor.submit(task, i)