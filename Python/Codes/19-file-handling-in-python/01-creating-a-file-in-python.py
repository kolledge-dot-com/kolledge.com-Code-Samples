# create a file in a specific directory
import os

directory = r'C:\Users\MyUser\Documents'
filename = 'example.txt'
filepath = os.path.join(directory, filename)

file = open(filepath, "w")
file.close()



# create a file if it does not exists
import os
filepath = 'example.txt'

if not os.path.exists(filepath):
   file = open(filepath, 'w')
   file.close()



# create a new file using with statement
with open("newfile.txt", "w") as file:
   file.write("This is a new file.")




# create file with a datetime
import datetime

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"example_{formatted_time}.txt"

file = open(filename, 'w')
file.close()




# create a file with permission
import os

filename = "example.txt"

# read and write permission for owner, group, and others
permission = 0o666

os.mknod(filename, mode=permission)