# open a file in read mode
file = open("example.txt", "r")
print(file.read())
file.close()



# open a file in write mode
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()



# open a file in append mode
file = open("example.txt", "a")
file.write("\nHello, World Again!")
file.close()



# open a file with relative path
import os

file_path = os.path.join("directory", "example.txt")
file = open(file_path, "r")
print(file.read())
file.close()



# open a file using with statement
with open("example.txt", "r") as file:
   print(file.read())



# open a file for multiple operations
with open("example.txt", "r+") as file:
   print(file.read())
   file.write("\nAdded a new line!")




# open a binary file
with open("binaryfile.png", "rb") as file:
   print(file.read())



# Handle the FileNotFoundError
import os

file_path = os.path.join("directory", "example.txt")

if os.path.exists(file_path):
   file = open(file_path, "r")
   print(file.read())
   file.close()
else:
   print("File does not exist.")