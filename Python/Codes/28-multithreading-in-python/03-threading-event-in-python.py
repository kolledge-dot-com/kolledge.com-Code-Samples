# Creating Python Threading Event :
import threading

# Create the event object
event = threading.Event()

# Define the worker function
def worker():
   print("Worker waiting for event")
   event.wait()
   print("Worker continuing to run")

# Start the worker thread
thread = threading.Thread(target=worker)
thread.start()

# Wait for a user input
input("Press any key to trigger the event\n")

# Set the event
event.set()