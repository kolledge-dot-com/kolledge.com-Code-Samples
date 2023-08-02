# rename a file using rename() method
import os
os.rename("old_file_name.txt", "new_file_name.txt")




# Check whether file exists before renaming
import os
if os.path.exists("old_file_name.txt"):
   os.rename("old_file_name.txt", "new_file_name.txt")



# rename multiple files in python
import os
for file in os.listdir():
   os.rename(file, "new_" + file)



# Renaming files that matches a pattern
import glob
import os

files = glob.glob("*.txt")

for file in files:
   os.rename(file, "new_" + file)



# rename all files in a folder
import os

dir_path = "/path/to/folder"

for file in os.listdir(dir_path):
    os.rename(os.path.join(dir_path, file), os.path.join(dir_path, "new_" + file))




# rename only a list of files in a folder
import os

dir_path = "/path/to/folder"

files_to_rename = ["file1.txt", "file2.txt"]

for file in files_to_rename:
    os.rename(os.path.join(dir_path, file), os.path.join(dir_path, "new_" + file))




# Renaming files with a timestamp
import os
from datetime import datetime

time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

os.rename("file.txt", f"file_{time_stamp}.txt")




#  rename the extension of the files
import os

filename, extension = os.path.splitext("file.txt")

os.rename("file.txt", filename + ".docx")




#  rename an image file in python
from PIL import Image
image = Image.open("image.png")
image.save("new_image.jpg")



# rename and move a file in python
import shutil
import os

src = "/path/to/folder/file.txt"
dst = "/path/to/new/folder/new_file.txt"
shutil.move(src, dst)

os.rename(dst, "/path/to/new/folder/rename_new_file.txt")