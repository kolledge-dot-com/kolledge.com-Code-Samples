# delete a File in python using os.remove() function
import os

os.remove("/path/to/file")


# delete a file in python using rmtree() function
import shutil

shutil.rmtree("/path/to/directory")




# remove file using os.unlink() Method
import os

os.unlink("/path/to/file")



# Using the Pathlib Module to remove file
from pathlib import Path

file = Path("/path/to/file")
file.unlink()



# Delete all files from a directory
import os

for file in os.listdir("/path/to/directory"):
   os.remove(os.path.join("/path/to/directory", file))




# deleting files that match a pattern
import glob
import os

for file in glob.glob("/path/to/directory/*.txt"):
   os.remove(file)



# delete files with specific extension
import os

for file in os.listdir("/path/to/directory"):
    if file.endswith(".txt"):
        os.remove(os.path.join("/path/to/directory", file))




# delete file whose name starts with specific string
import os

for file in os.listdir("/path/to/directory"):
   if file.startswith("text"):
       os.remove(os.path.join("/path/to/directory", file))



# delete file whose name contains a specific letters
import os

for file in os.listdir("/path/to/directory"):
   if "sample" in file:
       os.remove(os.path.join("/path/to/directory", file))




# deleting files matching a pattern from all subfolders
import os

for root, dirs, files in os.walk("/path/to/directory"):
   for file in files:
       if file.endswith(".txt"):
           os.remove(os.path.join(root, file))







