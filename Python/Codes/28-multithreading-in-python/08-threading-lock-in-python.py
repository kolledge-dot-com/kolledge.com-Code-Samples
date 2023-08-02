# use Lock to Prevent the Race Condition :
import threading

# A shared variable
balance = 100

# A Lock for the balance variable
lock = threading.Lock()

def withdraw(amount):
   global balance
   # Acquire the lock
   lock.acquire()
   balance = balance - amount
   # Release the lock
   lock.release()

def deposit(amount):
   global balance
   # Acquire the lock
   lock.acquire()
   balance = balance + amount
   # Release the lock
   lock.release()

# Create two threads
t1 = threading.Thread(target=withdraw, args=(50,))
t2 = threading.Thread(target=deposit, args=(100,))

# Start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()

# Print the final balance
print("Final balance:", balance)