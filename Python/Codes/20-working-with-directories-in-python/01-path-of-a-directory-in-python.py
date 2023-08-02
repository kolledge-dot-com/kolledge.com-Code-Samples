# get the current working directory in Python
import os

current_dir = os.getcwd()
print(current_dir)



#  Join a Path in Python
import os
path = os.path.join("C:", "Users", "username", "Documents")

print(path)




# split a path in Python
import os
path = "C:/Users/username/Documents"

split_path = os.path.split(path)
print(split_path)



# test if a Path is a Directory
import os
path = "C:/Users/username/Documents"

is_directory = os.path.isdir(path)

print(is_directory)