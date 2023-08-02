# Code sample for Python Package
#my_package/__init__.py   (folder name and __init__.py file)
def greeting(name):
   print("Hello, " + name)
def farewell(name):
   print("Goodbye, " + name)

# main.py
from my_package import greeting, farewell
greeting("John")
farewell("John")