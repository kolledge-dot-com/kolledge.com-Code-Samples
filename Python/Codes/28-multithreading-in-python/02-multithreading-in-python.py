# Creating a thread class :
import threading


class CustomThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"Thread {self.name} running")