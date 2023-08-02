# Implementing the start and stop pattern using Python context manager :
import threading


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        # Start thread
        pass

    def stop(self):
        # Stop thread
        pass


with MyThread() as t:
    # Thread is started
    # Do something
    pass

# Thread is stopped