# List all files of a directory in Python
import os

files = os.listdir("/path/to/directory")
print(files)




# List Files in a Directory that match a specific pattern :
import glob

files = glob.glob("/path/to/directory/*.txt")
print(files)




# List only Files from a Directory
import os

files = [file for file in os.listdir("/path/to/directory") if os.path.isfile(os.path.join("/path/to/directory", file))]

print(files)



# Using Generator Expression to List Files of a Directory
import os

files = (file for file in os.listdir("/path/to/directory") if os.path.isfile(os.path.join("/path/to/directory", file)))

for file in files:
    print(file)



# List both Files and Directories
import os

files = os.listdir("/path/to/directory")
print(files)




# Using os.walk() to List All Files in Directory and Subdirectories
import os

for root, dirs, files in os.walk("/path/to/directory"):
   for file in files:
       print(os.path.join(root, file))



# Use os.scandir() to Get Files of a Directory
import os

with os.scandir("/path/to/directory") as directory:
   for entry in directory:
       if entry.is_file():
           print(entry.name)



# Using Glob Module to List Files of a Directory

import glob

files = glob.glob("/path/to/directory/*.txt")
print(files)



# Use Pathlib Module to List Files of a Directory
from pathlib import Path

files = [file.name for file in Path("/path/to/directory").iterdir() if file.is_file()]
print(files)