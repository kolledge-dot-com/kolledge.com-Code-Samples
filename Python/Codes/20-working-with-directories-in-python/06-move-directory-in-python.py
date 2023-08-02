# Moving a file in Python
import os

source_file = "/path/to/source/file"
destination_file = "/path/to/destination/file"
os.rename(source_file, destination_file)




# move multiple files in Python
import shutil

source_directory = "/path/to/source/directory"
destination_directory = "/path/to/destination/directory"

for file_name in os.listdir(source_directory):
   source = os.path.join(source_directory, file_name)
   destination = os.path.join(destination_directory, file_name)
   shutil.move(source, destination)




# move all files from a directory in Python :
import os
import shutil

source_directory = "/path/to/source/directory"
destination_directory = "/path/to/destination/directory"

for file_name in os.listdir(source_directory):
   source = os.path.join(source_directory, file_name)
   destination = os.path.join(destination_directory, file_name)
   if os.path.isfile(source):
       shutil.move(source, destination)




# move files matching a pattern (Wildcard) :
import glob
import os

source_directory = "/path/to/source/directory"
destination_directory = "/path/to/destination/directory"

for file_name in glob.glob(os.path.join(source_directory, "*.txt")):
   shutil.move(file_name, destination_directory)




# move files based on file extension
import os
import shutil

source_directory = "/path/to/source/directory"
destination_directory = "/path/to/destination/directory"

for file_name in os.listdir(source_directory):
    if file_name.endswith(".txt"):
        source = os.path.join(source_directory, file_name)
        destination = os.path.join(destination_directory, file_name)
        shutil.move(source, destination)




# move files based on filename
import os
import shutil

source_directory = "/path/to/source/directory"
destination_directory = "/path/to/destination/directory"

for file_name in os.listdir(source_directory):
   if "sample" in file_name:
       source = os.path.join(source_directory, file_name)
       destination = os.path.join(destination_directory, file_name)
       shutil.move(source, destination)



# move file and rename in Python :

import os

source_file = "/path/to/source/file"
destination_file = "/path/to/destination/file2"
os.rename(source_file, destination_file)
