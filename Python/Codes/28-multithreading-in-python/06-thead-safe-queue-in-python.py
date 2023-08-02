# Implementing Python Thread-Safe Queue :
import threading
import queue

def worker(q):
   while True:
       item = q.get()
       if item is None:
           break
       print("Processing item", item)
       q.task_done()

# Create a queue and worker threads
q = queue.Queue()
threads = []
for i in range(5):
   t = threading.Thread(target=worker, args=(q,))
   t.start()
   threads.append(t)

# Add items to the queue
for item in range(10):
   q.put(item)

# Wait for all tasks on the queue to be completed
q.join()

# Stop worker threads
for i in range(5):
   q.put(None)
for t in threads:
   t.join()