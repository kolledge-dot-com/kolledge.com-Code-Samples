# create a directory in Python
import os
os.mkdir("new_directory")



# rename a Directory in Python
import os
os.rename("old_directory", "new_directory")



# delete an empty directory in Python
import os
os.rmdir("directory_to_be_deleted")



# delete a non-empty directory in Python
import shutil
shutil.rmtree("directory_to_be_deleted")



# traverse a directory recursively
import os

for root, dirs, files in os.walk("/path/to/directory"):
   print("Directory:", root)
   print("Sub-directories:", dirs)
   print("Files:", files)